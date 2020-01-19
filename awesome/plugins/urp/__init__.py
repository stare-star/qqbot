import nonebot
import pytz
import pickle
from awesome.plugins.urp.utils import login, getHtml, parse

from nonebot import on_command, CommandSession
from config import user

__plugin_name__ = '查成绩'
__plugin_usage__ = r'''
urp 账号 密码
'''


# on_command 装饰器将函数声明为一个命令处理器
# 这里为命令的名字，同时允许使用别名
@on_command('urp', aliases=('成绩', '教务'))
async def urp(session: CommandSession):
    # 从会话状态（session.state）中获取name，如果当前不存在，则询问用户
    id = session.get('id', prompt='学号')
    passwd = session.get('passwd', prompt='密码')
    course = session.state.get('course')
    await session.send("正在查询中，请稍候~")
    # 查询
    s, cookies = await login(id, passwd)

    code, html = await getHtml(s, cookies)
    if code == 200:

        res = parse(html)
        res_format = ''
        for i in res:
            res_format += i[0] + '\t' + str(i[3]) + '\n'
        r = ''
        if course:
            for i in res:
                if i[0] == course:
                    r = course + "\t" + str(i[3])
                    break
        # 向用户发送结果
        await session.send(res_format)

        if course:
            for i in res:
                if i[0] == course:
                    r = course + "\t" + str(i[1])
                    await session.send(str(r))
                    break
    if code == 404:
        await session.send(html)


# weather.args_parser 装饰器将函数声明为 urp 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@urp.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符

    stripped_arg = session.current_arg_text.strip()
    print(stripped_arg)
    print(type(stripped_arg))

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        print(1111111111111111111111111111)
        print(1111111111111111111111111111)
        print(stripped_arg, "000000000000000000")

        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            arg = stripped_arg.split()
            print(arg)

            if len(arg) == 1:
                session.state['id'] = arg[0]
                session.state['passwd'] = arg[0]
            if len(arg) == 2:
                session.state['id'] = arg[0]
                session.state['passwd'] = arg[1]
            if len(arg) == 3:
                session.state['id'] = arg[0]
                session.state['passwd'] = arg[1]
                session.state['course'] = arg[2]
        return

    if not session.is_first_run:
        print(2222222222222222222222222222)
        print(stripped_arg)

        if not stripped_arg:
            # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
            # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
            session.pause('要查询的姓名不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg
    print(stripped_arg)


# 每天自动检查是否有出成绩，有则发送 ，无
#
@nonebot.scheduler.scheduled_job("cron", day_of_week='*', hour='12', minute='00', second='00',
                                 timezone=pytz.timezone('Asia/Shanghai'))
async def monitor():
    """ 早安
    """
    id = '1762410319'
    pd = '142857'
    s, c = login(id, pd)
    c, html = getHtml(s, c)
    res = parse(html)
    res_format = ''
    for i in res:
        res_format += i[0] + '\t' + str(i[3]) + '\n'

    filename = 'msg.data'

    msg = load(filename)

    if msg != res_format:
        bot = nonebot.get_bot()
        await bot.send_private_msg(user_id=user, message=res_format)
        save(filename, res_format)
    bot.logger.info('监控成绩更新信息')


def save(filename, var):
    f = open(filename, 'wb')
    # 将变量存储到目标文件中区
    pickle.dump(var, f)
    f.close()


def load(filename):
    f = open(filename, 'rb')
    # 将文件中的变量加载到当前工作区
    var = pickle.load(f)
    return var


if __name__ == '__main__':
    id = '1762410319'
    pd = '142857'
    s, c = login(id, pd)
    c, html = getHtml(s, c)
    res = parse(html)
    res_format = ''
    for i in res:
        res_format += i[0] + '\t' + str(i[3]) + '\n'

    filename = 'msg.data'
    msg = load(filename)
    if msg != res_format:
        print(1)
        save(filename, res_format)
    else:
        print(0)
