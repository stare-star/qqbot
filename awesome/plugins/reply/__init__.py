'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2020-01-18 12:58
@desc:
'''

'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2020-01-18 12:53
@desc:
'''
import random
import re
import nonebot
from nonebot import on_natural_language, NLPSession, IntentCommand, on_command, CommandSession
import time


@on_command('justsend')
async def justsend(session: CommandSession):
    words = session.get('message')
    await session.send(words)


@on_natural_language(keywords={'敬业福'}, only_to_me=False)
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    print(stripped_msg)
    words = '不会还有人没有敬业福吧'

    return IntentCommand(90.0, 'justsend', args={'message': words})


@on_natural_language(keywords={'不会还有人'}, only_to_me=False)
async def _(session: NLPSession):
    words = '你刚刚说了“不会还有人”是吧？\n你就是大营养师吗？'
    return IntentCommand(90.0, 'justsend', args={'message': words})


@on_natural_language(keywords={'jojo'}, only_to_me=False)
async def _(session: NLPSession):
    if random.random() < 0.3:
        words = '你刚刚说了jojo是吧？'
        return IntentCommand(90.0, 'justsend', args={'message': words})


@on_natural_language(keywords={'陈鹏', 'cp'}, only_to_me=False)
async def _(session: NLPSession):
    if random.random() < 0.1:
        words = '啊~~~ 尊敬的陈鹏老师'
        return IntentCommand(90.0, 'justsend', args={'message': words})


@on_natural_language(keywords={'曹元', 'cy'}, only_to_me=False)
async def _(session: NLPSession):
    if random.random() < 0.1:
        words = f"[CQ:face,id =76]"

        return IntentCommand(90.0, 'justsend', args={'message': words})

