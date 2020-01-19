from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from nonebot.command.argfilter.controllers import handle_cancellation

from awesome.plugins.ocr.ocr_API import get_ocr_result, get_ocr_result_by_url, getImag


# on_command 装饰器将函数声明为一个命令处理器
# 这里为命令的名字，同时允许使用别名

@on_command('ocr', aliases=('识别', '转文字'))
async def ocr(session: CommandSession):
    # 从会话状态（session.state）中获取图片url（url），如果当前不存在，则询问用户
    url = session.get('img', prompt='你想识别哪张图片呢？')
    # ocr识别
    res_ocr = get_ocr_result_by_url(url)
    # 向用户发送识别结果
    await session.send(res_ocr)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@ocr.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    img = session.current_arg_images
    print("\n", img, "\n")

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['img'] = session.current_arg_images
        return

    if not session.is_first_run:
        if not session.current_arg_images:
            # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
            # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
            session.pause()

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = session.current_arg_images



@on_natural_language(keywords=None)
async def _(session: NLPSession):
    try:
        img = session.current_arg_images
        print(img)
        if img:
            return IntentCommand(90.0, 'ocr', current_arg=img)
    except:
        pass



