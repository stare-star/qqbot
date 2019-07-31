'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: oneyan.py
@time: 2019-07-30 22:32
@desc:
'''


import json
import re

import requests
from nonebot import CommandSession, on_command
api="https://v1.hitokoto.cn/"

@on_command('one', only_to_me=False)
async def one(session: CommandSession):
    try:
        output=getone()
        # 去掉最后一个\n
        await session.send(output)
    except:
        await session.send('获取信息失败了~>_<~')


def getone():
    response = requests.get(api)
    data = response.content.decode('utf-8')
    rjson = json.loads(data)
    rjson['hitokoto']
    rjson['from']
    output = f"{rjson['hitokoto']}   ---     {rjson['from']}"
    return output
