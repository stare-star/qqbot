'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2019-08-14 21:46
@desc:
'''


from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from nonebot.command.argfilter.controllers import handle_cancellation
from sqlalchemy import func

import awesome.plugins.clock.Clock
from awesome.plugins.clock.Clock import session as sql_session

__plugin_name__ = '电影'
__plugin_usage__ = r'''
命令格式
电影 XXX
film XXX
'''


# on_command 装饰器将函数声明为一个命令处理器
# 这里为命令的名字，同时允许使用别名

@on_command('film', aliases=('豆瓣', '电影'), only_to_me=False)
async def film(session: CommandSession):
    # 从会话状态（session.state）中获取图片url（url），如果当前不存在，则询问用户
    name = session.get('name', prompt='你查找什么电影？')

    weather_report = await get_weather_of_city(name)
    await session.send(weather_report)


@film.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.split()

    if session.is_first_run:
        if stripped_arg:
            session.state['name'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的电影名不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg




