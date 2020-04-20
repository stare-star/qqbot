'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: short_url.py
@time: 2019-07-29 20:11
@desc:
'''
from nonebot import CommandSession, on_command, NLPSession, on_natural_language, IntentCommand

from awesome.plugins.short_url.short_url_api import shorten_lyx, participle

__plugin_name__ = '短网址'
__plugin_usage__ = r'''
short url
'''


@on_command('short_url', aliases={'short', '短网址'})
async def short_url(session: CommandSession):
    url = session.get('url', prompt='请输入长网址')
    short_url_ = shorten_lyx(url)
    await session.send(short_url_)


@short_url.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    url = participle(stripped_arg)
    if stripped_arg:
        session.state['url'] = url
        return
    else:
        session.pause('请重新输入')


@on_natural_language(keywords={'短网址'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    url = participle(stripped_msg)
    return IntentCommand(90.0, 'short_url', current_arg=url)
