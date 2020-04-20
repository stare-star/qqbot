'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2020-01-15 13:19
@desc:
'''

__plugin_name__ = '我帮你百度'
__plugin_usage__ = r"""
我帮你百度
用法：baidu  bd
"""

import requests
from nonebot import CommandSession, on_command
from awesome.plugins.short_url import shorten_lyx


@on_command('baidu', aliases={'bd', '百度'}, only_to_me=False)
async def baidu(session: CommandSession):
    try:
        q = session.get('q', prompt='请输入关键词')
        output = getUrl(q)
        short_url_ = shorten_lyx(output)
        await session.send(short_url_)
    except:
        await session.send('失败了~>_<~')


@baidu.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['q'] = stripped_arg
        return
    else:
        session.pause('请重新输入关键词')


def getUrl(q):
    url = 'http://iwo.im'
    payload = {}
    payload['q']=q
    ret = requests.get(url, params=payload)
    return ret.url

if __name__ == '__main__':
    getUrl('hehaihhuc')