'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: morning.py
@time: 2019-07-29 21:10
@desc:
'''
import nonebot

from awesome.plugins.oneyan import getone
from config import group_id

""" 每日早安插件
"""
import re
from random import randint

import requests
from nonebot import CommandSession, on_command





@nonebot.scheduler.scheduled_job("cron", day_of_week='*', hour='0', minute='0', second='00')
async def morning():
    """ 早安
    """
    hello_str = get_message()
    yan=getone()
    out=hello_str+'\n\n'+yan
    bot = nonebot.get_bot()
    await bot.send_group_msg(group_id=group_id,
                                 message=out)
    bot.logger.info('发送早安信息')


TEXTS = ['早上好呀~>_<~', '大家早上好呀！', '朋友们早上好！']


def get_message():
    """ 获得消息
    不同的问候语
    """
    try:
        # 获得不同的问候语
        res = requests.get('http://timor.tech/api/holiday/tts').json()
    except:
        res = {'code': -1}

    text_index = randint(0, len(TEXTS) - 1)
    str_data = f'{TEXTS[text_index]}\n'

    if res['code'] == 0:
        str_data += res['tts']
    else:
        str_data += '好像没法获得节假日信息了，嘤嘤嘤'

    return str_data