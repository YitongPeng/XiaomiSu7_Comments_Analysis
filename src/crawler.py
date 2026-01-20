import json
import requests
import time
import csv
import re
import datetime
import random
import os


def get_content(csv_writer, headers):
    """
    爬取微博评论数据

    参数:
        csv_writer: CSV文件写入器
        headers: HTTP请求头
    """
    max_id = 0
    max_id_type = 0

    for page in range(1, 281):  # 遍历1到280页
        print(f'正在爬取第{page}页！')

        if page == 1:
            url = 'https://m.weibo.cn/comments/hotflow?id=5017599890950579&mid=5017599890950579&max_id_type=0'
        else:
            url = f'https://m.weibo.cn/comments/hotflow?id=5017599890950579&mid=5017599890950579&max_id={max_id}&max_id_type={max_id_type}'

        print(url)

        try:
            resp = requests.get(url, headers=headers)
            resp.encoding = 'utf-8'
            max_id = resp.json()['data']['max_id']
        except KeyError:
            max_id_type += 1
            url = f'https://m.weibo.cn/comments/hotflow?id=5017599890950579&mid=5017599890950579&max_id={max_id}&max_id_type={max_id_type}'
            print(url)
            resp = requests.get(url, headers=headers)
            resp.encoding = 'utf-8'
            try:
                max_id = resp.json()['data']['max_id']
            except KeyError:
                break

        # 遍历响应数据中的评论数据
        for each in resp.json()['data']['data']:
            try:
                each = json.dumps(each, ensure_ascii=False)
                user = re.findall(r'"screen_name": "(.*?)",', each)[0]
                content = re.findall(r'"text": "(.*?)"', each)[0]
                content = re.sub(r'<.*', '', content)
                like_counts = re.findall(r'"like_count": (\d+),', each)[0]
                date_str = re.findall(r'"created_at": "(.*?)"', each)[0]
                date = datetime.datetime.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")
                date = date.strftime("%Y-%m-%d %H:%M:%S")
            except IndexError:
                continue

            print(user, content, like_counts, date)
            csv_writer.writerow([user, content, like_counts, date])

        # 随机延时，避免请求过快
        temp = random.randint(2, 4)
        time.sleep(temp)


if __name__ == '__main__':
    # 设置HTTP请求头
    # 注意：需要替换为你自己的Cookie才能运行
    headers = {
        "Cookie": "YOUR_COOKIE_HERE",  # 请替换为你的微博Cookie
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    # 设置输出路径（相对路径）
    output_path = os.path.join('..', 'data', 'raw', 'xiaomi.csv')

    # 打开CSV文件用于写入数据
    with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['username', 'content', 'likecount', 'date'])
        get_content(csv_writer, headers)
