import json  # 用于处理JSON数据
import requests  # 用于发送HTTP请求
import time  # 用于处理时间相关的操作
import csv  # 用于处理CSV文件
import re  # 用于正则表达式操作
import datetime  # 用于处理日期时间
import random  # 用于生成随机数


# 定义获取内容的函数
def get_content(csv_writer):
    max_id = 0  # 初始化max_id
    max_id_type = 0  # 初始化max_id_type
    for page in range(1, 281):  # 遍历1到280页
        print(f'正在爬取第{page}页！')  # 打印当前页数
        if page == 1:  # 如果是第一页
            url = 'https://m.weibo.cn/comments/hotflow?id=5017599890950579&mid=5017599890950579&max_id_type=0'
        else:  # 如果不是第一页，使用max_id和max_id_type构建URL
            url = f'https://m.weibo.cn/comments/hotflow?id=5017599890950579&mid=5017599890950579&max_id={max_id}&max_id_type={max_id_type}'
        print(url)  # 打印URL
        try: # 判断异常
            # 发送HTTP GET请求
            resp = requests.get(url, headers=headers)
            resp.encoding = 'utf-8'  # 设置响应编码
            max_id = resp.json()['data']['max_id']  # 获取max_id
        except KeyError:  # 如果KeyError异常
            max_id_type += 1  # 增加max_id_type
            url = f'https://m.weibo.cn/comments/hotflow?id=5017599890950579&mid=5017599890950579&max_id={max_id}&max_id_type={max_id_type}'
            print(url)  # 打印新的URL
            resp = requests.get(url, headers=headers)  # 发送新的HTTP GET请求
            resp.encoding = 'utf-8'  # 设置响应编码
            try:
                max_id = resp.json()['data']['max_id']  # 获取新的max_id
            except KeyError:  # 如果再次发生KeyError异常
                break  # 退出循环

        # 遍历响应数据中的评论数据
        for each in resp.json()['data']['data']:
            try:
                each = json.dumps(each, ensure_ascii=False)  # 将数据转换为JSON格式
                user = re.findall(r'"screen_name": "(.*?)",', each)[0]
                content = re.findall(r'"text": "(.*?)"', each)[0]
                content = re.sub(r'<.*', '', content)
                like_counts = re.findall(r'"like_count": (\d+),', each)[0]
                date_str = re.findall(r'"created_at": "(.*?)"', each)[0]
                date = datetime.datetime.strptime(date_str, "%a %b %d %H:%M:%S %z %Y")  # 将日期字符串转换为datetime对象
                date = date.strftime("%Y-%m-%d %H:%M:%S")  # 将日期格式化为字符串
            except IndexError:  # 如果发生IndexError异常
                continue  # 跳过当前循环
            print(user, content, like_counts, date)  # 打印用户名、评论内容、点赞量和日期
            csv_writer.writerow([user, content, like_counts, date])  # 将数据写入CSV文件

        temp = random.randint(2, 4)  # 生成2到4之间的随机数
        time.sleep(temp)  # 暂停指定的随机秒数


if __name__ == '__main__':
    # 设置HTTP请求头
    headers = {
        "Cookie": "SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFy4HL3Fc6IhymiBCQbnGGQ5JpX5KMhUgL.Fo-41K5N1hq7SKM2dJLoIpjLxKML1h.L1-zLxK.L1-eLBonLxK-L1KeLBKqt; SCF=Ahipg4Bv9GZA9W2E_HR4VBAQe5yF5fvnWKuqw9ybbXgL5r7ArPeB6Z8eNpjVCIjcz0ozCBWaTSy8zt_g_Q9AK-U.; SUB=_2A25LYtxbDeRhGeNH4lIW-CjMzjuIHXVoHlGTrDV6PUJbktCOLVLVkW1NSn7E_kdw6jOHdkgctRUqr5ojIIMF19XN; ALF=1720596747; _T_WM=54727833491; XSRF-TOKEN=438159; WEIBOCN_FROM=1110006030; MLOGIN=1; mweibo_short_token=821169ce51; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    output_path = r'D:\MINE\大数据分析综合实验\大数据2102班_彭弋桐_基于小米su7评论的情感分析和数据分析\数据\xiaomi.csv'
    # 打开CSV文件用于写入数据
    with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)  # 创建CSV写入器
        csv_writer.writerow(['用户名', '内容', '点赞量', '日期'])  # 写入CSV文件头
        get_content(csv_writer)  # 调用get_content函数
