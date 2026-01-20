# 小米SU7评论数据分析项目

基于小米SU7微博评论的情感分析和数据挖掘项目。

## 项目简介

本项目通过爬取小米SU7汽车在微博上的用户评论，进行文本挖掘、情感分析、聚类分析和分类预测，深入了解用户对小米SU7的态度和关注点。

## 项目结构

```
XiaomiSu7_git/
├── README.md                    # 项目说明文档
├── requirements.txt             # Python依赖包列表
├── .gitignore                   # Git忽略配置
├── data/                        # 数据目录
│   ├── raw/                     # 原始数据
│   │   └── xiaomi.csv           # 爬取的原始评论数据
│   ├── processed/               # 处理后的数据
│   │   └── sentiment_scoring.csv # 情感分析后的数据
│   └── lexicon/                 # 词典资源
│       ├── stopwords_cn.txt     # 中文停用词表
│       ├── positive_emotional_words.txt    # 正面情感词
│       ├── negative_emotional_words.txt    # 负面情感词
│       ├── positive_evaluative_words.txt   # 正面评价词
│       ├── negative_evaluative_words.txt   # 负面评价词
│       └── not.csv              # 否定词表
├── notebooks/                   # Jupyter notebooks
│   ├── 01_data_preprocessing.ipynb          # 数据预处理
│   ├── 02_wordfrequency_wordcloud.ipynb     # 词频分析和词云
│   ├── 03_sentiment_analysis.ipynb          # 情感分析
│   ├── 04_clustering_analysis.ipynb         # 聚类分析
│   ├── 05_classification_models.ipynb       # 分类模型
│   └── 06_comment_quality.ipynb             # 评论质量分析
├── src/                         # 源代码
│   ├── __init__.py
│   └── crawler.py               # 爬虫代码
├── outputs/                     # 输出结果
│   ├── figures/                 # 图表
│   │   ├── wordcloud/           # 词云相关图表
│   │   ├── sentiment/           # 情感分析图表
│   │   ├── clustering/          # 聚类分析图表
│   │   └── quality/             # 质量分析图表
│   └── models/                  # 训练的模型
└── logs/                        # 日志文件
```

## 环境配置

### 依赖安装

```bash
pip install -r requirements.txt
```

### 系统要求

- Python 3.8+
- Jupyter Notebook

## 使用说明

### 1. 数据爬取（可选）

如果需要重新爬取数据：

```bash
python src/crawler.py
```

**注意**：需要配置有效的微博Cookie才能运行爬虫。

### 2. 数据分析流程

按照以下顺序运行notebooks：

1. **数据预处理** (`01_data_preprocessing.ipynb`)
   - 数据清洗
   - 去重去空值
   - 中文分词

2. **词频分析** (`02_wordfrequency_wordcloud.ipynb`)
   - 高频词统计
   - 词云可视化
   - 评论长度分布

3. **情感分析** (`03_sentiment_analysis.ipynb`)
   - 基于词典的情感打分
   - 否定词修正
   - 神经网络和贝叶斯分类模型

4. **聚类分析** (`04_clustering_analysis.ipynb`)
   - TF-IDF向量化
   - KMeans聚类
   - DBSCAN聚类
   - 余弦相似度分析

5. **分类模型** (`05_classification_models.ipynb`)
   - 逻辑回归
   - 随机森林
   - 特征重要性分析

6. **评论质量分析** (`06_comment_quality.ipynb`)
   - 评论趋势分析
   - 时间序列分析

## 主要功能

### 数据爬取
- 微博评论自动爬取
- 支持翻页和去重

### 文本分析
- 中文分词（jieba）
- 停用词过滤
- TF-IDF特征提取

### 情感分析
- 正负面情感词典匹配
- 否定词修正算法
- 情感得分计算
- 神经网络分类（准确率81%+）

### 聚类分析
- KMeans聚类
- DBSCAN密度聚类
- 余弦相似度计算
- 聚类效果可视化

### 可视化
- 词云图
- 词频分布图
- 情感占比饼图
- 聚类热力图
- 时间趋势图

## 数据说明

### 原始数据字段

- `username`: 用户名
- `content`: 评论内容
- `likecount`: 点赞数
- `date`: 评论时间

### 处理后数据字段

- 原始字段 +
- `amend_weight_sum`: 修正后的情感得分
- `length`: 评论长度
- `tokenized_text`: 分词后文本

## 分析结果

主要发现：
- 正面评论占比约79%，负面评论占比约21%
- 高频词：小米、雷总、汽车、SU7等
- 主要关注点：外观设计、性能、价格、产能等

## 技术栈

- **数据爬取**: requests, BeautifulSoup
- **数据处理**: pandas, numpy
- **文本处理**: jieba, re
- **机器学习**: scikit-learn, imblearn
- **深度学习**: sklearn.neural_network
- **可视化**: matplotlib, seaborn, wordcloud

## 注意事项

1. 爬虫代码中的Cookie需要自行配置，已移除敏感信息
2. 路径配置已改为相对路径，适配不同操作系统
3. 建议在虚拟环境中运行项目

## 作者

大数据2102班 - 彭弋桐

## 许可证

本项目仅用于学习和研究目的。
