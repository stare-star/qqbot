from nonebot import on_command, CommandSession
from math import *

__plugin_name__ = '计算'
__plugin_usage__ = r"""
命令名称:计算
使用方法:计算 [表达式]
"""


@on_command('compute', aliases=['计算', 'js'])
async def weather(session: CommandSession):
    try:
        await session.send(str(eval(session.current_arg_text.strip())))
    except:
        await session.send('计算出错')
