from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from .getwea import *
from jieba import posseg

__plugin_name__ = '天气'
__plugin_usage__ = r'''
天气 城市
'''


@on_command('weather', aliases=('天气', 'wea'))
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查询哪个城市？')
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.split()
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')


    session.state[session.current_key] = stripped_arg


async def get_weather_of_city(city: str):
    data = getweather(city[0])
    if(data != "请查询具体城市而非省分"):
        list = weaList(data)
        return f'{list}'
    return f'{data}'





@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    # 对消息进行分词和词性标注
    words = posseg.lcut(stripped_msg)

    city = "北京"
    # 遍历 posseg.lcut 返回的列表
    for word in words:
        # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
        if word.flag == 'ns':
            # ns 词性表示地名
            city = word.word

    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'weather', current_arg=city)