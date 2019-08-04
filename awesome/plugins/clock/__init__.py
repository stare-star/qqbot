'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2019-08-04 11:05
@desc:
'''

from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from nonebot.command.argfilter.controllers import handle_cancellation
from sqlalchemy import func

import awesome.plugins.clock.Clock
from awesome.plugins.clock.Clock import session as sql_session

__plugin_name__ = '打卡'
__plugin_usage__ = r'''
命令格式
打卡 XXX
打卡记录
'''


# on_command 装饰器将函数声明为一个命令处理器
# 这里为命令的名字，同时允许使用别名

@on_command('clock', aliases=('打卡', '签到'), only_to_me=False)
async def clock(session: CommandSession):
    # 从会话状态（session.state）中获取图片url（url），如果当前不存在，则询问用户
    name = session.get('name', prompt='你想打卡什么？')
    # 获取qq
    qq = session.ctx["user_id"]
    # 验证用户是否存在
    user = sql_session.query(Clock.User).filter_by(qq=qq).first()
    if user is None:
        user = Clock.add_user(qq)
    # 验证任务是否存在
    clock = sql_session.query(Clock.Clock).filter_by(user_id=user.id, name=name).first()
    if clock is None:
        clock = Clock.add_clock(name=name, user_id=user.id)

    Clock.add_clock_record(clock.id, user.id)
    num = sql_session.query(Clock.ClockRecord).filter_by(clock_id=clock.id).count()
    # 向用户发送打卡结果
    await session.send(f"打卡成功 \n {clock.name} 已打卡{num}次")

@on_command('my_clock', aliases=('打卡记录', "我的打卡"), only_to_me=False)
async def my_clock(session: CommandSession):
    # 从会话状态（session.state）中获取图片url（url），如果当前不存在，则询问用户
    # name = session.get('name', prompt='你想打卡什么？')
    # 获取qq
    qq = session.ctx["user_id"]
    # 验证用户是否存在
    user = sql_session.query(Clock.User).filter_by(qq=qq).first()
    if user:
        clocks = user.clocks
        num = []
        last_time = []
        for clock in clocks:
            print(clock.name)
            num.append(sql_session.query(Clock.ClockRecord).filter_by(clock_id=clock.id).count())
            last_time.append(sql_session.query(func.max(Clock.ClockRecord.time)).filter_by(clock_id=clock.id).scalar())
        res = ''
        for i in range(len(num)):
            res += f"{clocks[i].name} \t {num[i]} \t 上次打卡时间 {last_time[i]}\n"
        await session.send(res[:-1])

    else:
        await session.send("没有该用户的信息")

    # 向用户发送识别结果


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@clock.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            print(stripped_arg)
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['name'] = stripped_arg
        return

    if not session.is_first_run:
        if not stripped_arg:
            # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
            # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
            session.pause()

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


# @my_clock.args_parser
# async def _(session: CommandSession):
#     # 去掉消息首尾的空白符
#     stripped_arg = session.current_arg_text.strip()
#
#     if session.is_first_run:
#         # 该命令第一次运行（第一次进入命令会话）
#         if stripped_arg:
#             # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
#             # 例如用户可能发送了：天气 南京
#             session.state['name'] = stripped_arg
#         return
#
#     if not session.is_first_run:
#         if not session.current_arg_images:
#             # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
#             # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
#             session.pause()
#
#     # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
#     session.state[session.current_key] = session.current_arg_images


@on_natural_language(keywords={'打卡'})
async def _(session: NLPSession):
    # stripped_msg = session.msg_text.strip()
    # pass
    # return IntentCommand(90.0, 'clock', current_arg=url)
    pass


if __name__ == '__main__':
    import awesome.plugins.clock.Clock
    import awesome.plugins.clock.User
