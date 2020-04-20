'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2020-04-15 15:24
@desc:
'''

import os
import random
from nonebot import CommandSession, on_command, NLPSession, on_natural_language, IntentCommand
from awesome.plugins.short_url.short_url_api import shorten_lyx, participle
from awesome.plugins.run.runpy import get501

__plugin_name__ = 'python'
__plugin_usage__ = r'''
python
'''


def runpy(script='print("Hello, world")'):
    return eval(script)


@on_command('py')
async def run(session: CommandSession):
    script = session.current_arg_text.strip()
    print(script)
    ret = runpy(script)
    ret=str(ret)
    print(ret)
    await session.send(ret)
