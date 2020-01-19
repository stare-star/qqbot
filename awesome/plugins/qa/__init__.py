'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2020-01-16 19:53
@desc:
'''
# 这是对话内容
import time
from typing import Optional

from nonebot import *
from nonebot import logger
from aiocqhttp.message import escape
from nonebot.helpers import render_expression
from nonebot.permission import PRIVATE, GROUP
import random
from awesome.utils.SqlHelper import bot_speakExer
from awesome.plugins.chat_tencent import chat

# -------------这是私聊部分
EXPR_DONT_UNDERSTAND = (
    '??????',
    '……你想表达什么？',
    '你得明白你对面是机器人，请用机器人的语言来说！',
    '……人类的语言好深奥',
    'ERROR: 无法理解',
    '虽然不明白你说的意思，但这个时候卖萌就对了！(<ゝω·)☆~',
    '我！听！不！懂！',
    '……我需要一个人来教教我怎么回答这句'
)


@on_command('study', aliases=['学习', '我教你'], permission=GROUP | PRIVATE, only_to_me=False)
async def study(session: CommandSession):
    message_type = session.ctx['message_type']
    if message_type == 'group':
        group_id = session.ctx['group_id']
        logger.error('---------------------------group_id' + str(group_id))
        # # 加一个限定
        # if group_id != 572013667:
        #     await session.send('主人好像不允许我在这里学习呢...')
        #     return
    question = session.state.get('question')  # 从会话状态里尝试获取
    if question is None:
        question = session.get('question', prompt='你需要我学习应答什么句子？', at_sender=True)
        session.state['question'] = question  # 修改会话状态
    answer = session.get('answer', prompt='那么我该怎么回答这个句子？')
    user_id = session.ctx['sender']['user_id']
    sqlHelper = bot_speakExer()
    sqlHelper.insertQuestionAndAnswer(question, answer, user_id)
    reply = f'添加成功！\n询问:\n{question}\n回答:\n{answer}'
    session.finish(reply)


@on_command('forget', aliases=['忘记'], permission=GROUP | PRIVATE, only_to_me=False)
async def forget(session: CommandSession):
    message_type = session.ctx['message_type']
    if message_type == 'group':
        group_id = session.ctx['group_id']
        logger.error('---------------------------group_id' + str(group_id))
        # # 加一个限定
        # if group_id != 572013667:
        #     await session.send('主人好像不允许我在这里学习呢...')
        #     return
    question = session.state.get('question')  # 从会话状态里尝试获取

    if question is None:
        question = session.get('question', prompt='你需要我忘记应答什么句子？', at_sender=True)
        session.state['question'] = question  # 修改会话状态

    sqlHelper = bot_speakExer()
    q = sqlHelper.selectQuestion(question)
    all ='\n'+ question + '\n'
    for i in q:
        all += str(i.id) + ' ' + i.answer + '\n'

    id = session.get('id', prompt=f'选择要忘记的id{all}'  , at_sender=True)
    session.state['id'] = id  # 修改会话状态

    r = sqlHelper.deleteQuestionByid(id)
    if r:
        reply = f'删除成功！\nid:{id}\n'
    else:
        reply = f'删除失败'
    session.finish(reply)


@forget.args_parser
async def _(session: CommandSession):
    if session.is_first_run and session.current_arg_text.strip():
        # 第一次运行，如果有参数，则设置给 question
        session.state['question'] = session.current_arg_text.strip()


@study.args_parser
async def _(session: CommandSession):
    if session.is_first_run and session.current_arg_text.strip():
        # 第一次运行，如果有参数，则设置给 question
        session.state['question'] = session.current_arg_text.strip()

    # 如果不需要对参数进行特殊处理，则不用再手动加入 state，NoneBot 会自动放进去


@on_natural_language(permission=PRIVATE, only_to_me=True)
async def _(session: NLPSession):
    return IntentCommand(70, 'justspeak', args={'message': session.msg_text})


@on_command('justspeak', only_to_me=True)
async def justSpeak(session: CommandSession):
    # 获取可选参数，这里如果没有 message 参数，命令不会被中断，message 变量会是 None
    message = session.state.get('message')

    # 获取回复
    reply = await call_response(session, str(message), 0)
    if reply:
        await session.send(reply)
    else:

        # 获取可选参数，这里如果没有 message 参数，命令不会被中断，message 变量会是 None

        # 通过封装的函数获取图灵机器人的回复
        reply = await chat.call_txchat_api(session, message)
        if reply:
            # 如果调用图灵机器人成功，得到了回复，则转义之后发送给用户
            # 转义会把消息中的某些特殊字符做转换，以避免 酷Q 将它们理解为 CQ 码
            time.sleep(2)
            return escape(reply)
        else:
            # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取图灵回复时的「表达」
            # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
            return session.send(render_expression(EXPR_DONT_UNDERSTAND))

        # # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
        # await session.send(render_expression(EXPR_DONT_UNDERSTAND))
        # # return


# 回复的api方法，返回一个字符串
async def call_response(session: CommandSession, text: str, number: int) -> Optional[str]:
    if not text:
        return None

    # 从数据库查询
    sqlHelper = bot_speakExer()

    # if number == 0  and 1:   #取消判断  测试一下
    values = sqlHelper.selectQuestion(text.lstrip())
    # else: ???
    # values =bot_speakExer().selectQuestionForGroup(text)
    logger.debug('------------------values:' + str(values))
    randomresult = 0

    # 如果不存在
    if not values:
        print('数据库中无该问题' + text)
        # 获取可选参数，这里如果没有 message 参数，命令不会被中断，message 变量会是 None
        message = text
        get_bot().seesion
        # 通过封装的函数获取图灵机器人的回复
        reply = await chat.call_txchat_api(session, message)
        if reply:
            # 如果调用图灵机器人成功，得到了回复，则转义之后发送给用户
            # 转义会把消息中的某些特殊字符做转换，以避免 酷Q 将它们理解为 CQ 码
            time.sleep(2)
            return escape(reply)
        else:
            # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取图灵回复时的「表达」
            # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
            return session.send(render_expression(EXPR_DONT_UNDERSTAND))


    else:
        # 如果很不只有一个
        if len(values) != 1:
            randomresult = random.randint(0, len(values))
        return str(values[randomresult].answer)


# -------------这是群聊部分
@on_natural_language(permission=GROUP, only_to_me=True)
async def _(session: NLPSession):
    return IntentCommand(70, 'justspeakgroup', args={'message': session.msg_text})


@on_command('justspeakgroup')
async def justspeakgroup(session: CommandSession):
    message = session.state.get('message')

    reply = await call_response(session, str(message), 1)
    if reply:
        await session.send(reply)
    else:
        return
