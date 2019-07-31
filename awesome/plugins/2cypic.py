'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: 2cypic.py
@time: 2019-07-30 22:46
@desc:
'''

import json
import re

import requests
from nonebot import CommandSession, on_command
api="http://www.dmoe.cc/random.php?return=json"

@on_command('pic', only_to_me=False)
async def pic(session: CommandSession):
    try:
        output = ''
        response = requests.get(api)
        data = (response.json())
        url=data['imgurl']


        img=f"[CQ:image,file={url}]"
        print(img)
        # 去掉最后一个\n
        await session.send(img)
    except:
        await session.send('获取图片失败了~>_<~')


if __name__ == '__main__':
    response = requests.get(api)
    data=(response.json())

    print(data['imgurl'])