import pytz
import requests
import time
import json


import nonebot
from config import user

from awesome.plugins.Quant.fundapi import getFundRt
from awesome.plugins.oneyan import getone
from config import group_id

""" 每日基金插件
"""


@nonebot.scheduler.scheduled_job("cron", day_of_week='*', hour='14', minute='20', second='00',timezone=pytz.timezone('Asia/Shanghai'))
async def fund():
    """ 基金
    """
    try:
        fund_str = get_message()
        bot = nonebot.get_bot()
        await bot.send_private_msg(user_id=user, message=fund_str)
        bot.logger.info('发送基金信息')

    except nonebot.CQHttpError:
        pass




def get_message():
    """ 获得消息
    不同的问候语
    """
    try:
        fscode='005918'

        res = getFundRt(fscode)
        res['code'] =0
    except:
        res = {'code': -1}

    str_data=''
    if res['code'] == 0:

        str_data =res['name']+':\n'+res['gszzl']+'\n                     '+res['gztime']
    else:
        str_data += '好像没法获得基金信息了，嘤嘤嘤'

    return str_data