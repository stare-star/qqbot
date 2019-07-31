'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: short_url_api.py
@time: 2019-07-29 20:12
@desc:
'''

import requests
import json
import re

from config import token

host = 'https://dwz.cn'
path = '/admin/v2/create'
url = host + path
method = 'POST'
content_type = 'application/json'

# TODO: 设置Token
token = token


def shorten(long_url):
    # TODO：设置待创建的长网址
    bodys = {'Url': long_url, 'TermOfValidity': 'long-term'}

    # 配置headers
    headers = {'Content-Type': content_type, 'Token': token}

    # 发起请求
    response = requests.post(url=url, data=json.dumps(bodys), headers=headers)

    # 读取响应
    print(response.text)
    return response.json()["ShortUrl"]


def participle(msg):
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式

    url = re.findall(pattern, msg)
    print(url)


if __name__ == '__main__':
    string = 'Its after 12 noon, do you know where your rooftops are? http://tinyurl.com/NYCRooftops '
    print(shorten("https://blog.csdn.net/qq_35246620/article/details/77647234"))
    print(participle(string))