'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: baike.py
@time: 2019-07-29 21:26
@desc:
'''

import requests
urlo="https://blog.csdn.net/potato012345/article/details/78215754"
url = "https://baike.baidu.com/search/word?word=高淳区"
print(url)
Headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    'Content-Length': '37',
    "Host": "baike.baidu.com",
    "Referer": "https://baike.baidu.com/",
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}

r = requests.get(url=url)
print(r.text)
print(r.text)
