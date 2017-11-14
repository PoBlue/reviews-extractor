# reviews-extractor
Extractor for review crawler

## 环境
- python 3

## 如何运行
1. 打开 `data.py` 文件，设置好参数，参考下面的【配置参数】章节
2. 运行下面代码
```
python data-to-csv.py
```
3. 在 `review-csv` 就能见到新生成的 csv 了，have fun ; )

### 其它
- 支持 Excel 的中文，阅读这里：[Excel 乱码解决方法](https://github.com/PoBlue/reviews-extractor/issues/1)

### 配置参数

打开 `data.py` 文件

复制下面的代码并放进去
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# set path to get json
REVIEW_ROOT_JSON_PATH = "example-data/"
DESC_JSON_PATH = REVIEW_ROOT_JSON_PATH + "description/"
CONTENT_JSON_PATH =  REVIEW_ROOT_JSON_PATH + "contents/"
COMMENT_JSON_PATH = REVIEW_ROOT_JSON_PATH + "comments/"


# set path to export csv
REVIEW_ROOT_CSV_PATH = "review-csv/" 
DESC_CSV_PATH = REVIEW_ROOT_CSV_PATH + "description.csv"
CONTENT_CSV_PATH = REVIEW_ROOT_CSV_PATH + "content.csv"
COMMENT_CSV_PATH = REVIEW_ROOT_CSV_PATH + "comment.csv"
```

主要可以修改的设置有以下：
1. `REVIEW_ROOT_JSON_PATH`, 这个是指向存储已爬取的 review 数据的相对路径
2. `REVIEW_ROOT_CSV_PATH `，这个是指向导出 csv 的相对路径

可以 clone 项目后直接不用改，直接运行，尝试一下，里面已经有 `example-data/` 的了

