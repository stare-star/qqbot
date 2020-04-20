'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2020-03-18 10:08
@desc:
'''
import nonebot
from nonebot import on_natural_language, NLPSession, IntentCommand, on_command, CommandSession
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
my_bot = ChatBot("Training demo")
trainer = ListTrainer(my_bot)

# @on_command('chat', aliases=('chatterbot'), only_to_me=False)
# async def film(session: CommandSession):
#     stripped_msg = session.msg_text.strip()
#     print(stripped_msg)
#     res = my_bot.get_response(stripped_msg)
#     await session.send(res)


@on_natural_language( only_to_me=False)
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    print(stripped_msg)
    res=my_bot.get_response(stripped_msg)
    return IntentCommand(0, 'justsend',  args={'message': res})


@nonebot.scheduler.scheduled_job("cron", day_of_week='*', hour='18', minute='0', second='00',timezone=pytz.timezone('Asia/Shanghai'))
async def _():
    trainer = ListTrainer(my_bot)