'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: nickname.py
@time: 2019-08-01 16:54
@desc:
'''
from nonebot import CommandSession, on_command
import random
# [1703937r1703978]






@on_command('星星', only_to_me=False)
async def one(session: CommandSession):
    id1 = random.randint(1, 208)
    id2 = random.randint(128513, 128613)
    # reply=[f"[CQ: emoji.id =[1000048r10000057]]",
    reply = [
             f"[CQ:face,id ={id1}]",
             f"[CQ:emoji,id ={id2}] 不在!"]

    # f"[CQ:emoji,id =[9800r9811]不在!"]
    output=random.choice(reply)
    await session.send(output)


if __name__ == '__main__':
    pass