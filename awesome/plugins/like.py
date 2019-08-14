'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: like.py
@time: 2019-08-07 19:32
@desc:
'''

__plugin_name__ = '点赞'
__plugin_usage__ = r'''
发送“赞我”、“点赞”
即可得到10个赞

'''


# 点赞 需要pro

from collections import deque

from nonebot import on_command, CommandSession

IS_LIKE = deque()


@on_command('send_like', aliases=['点赞', '赞我'],only_to_me=False)
async def _(session: CommandSession):
    session.ctx['times'] = 10
    await session.bot.send_like(**session.ctx)
    msg = f'[CQ:at,qq={session.ctx["user_id"]}]已经给你赞了10次了,记得回赞哦。'
    if session.ctx["user_id"] in IS_LIKE:
        msg = f'[CQ:at,qq={session.ctx["user_id"]}]今天已经赞过你啦！'
    IS_LIKE.append(session.ctx["user_id"])
    await session.finish(msg)