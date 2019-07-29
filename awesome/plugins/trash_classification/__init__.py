from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .trash_api import get_the_sort_of_trash, participle

__plugin_name__ = '垃圾分类'
__plugin_usage__ = r'''
xx是什么垃圾
XX属于什么垃圾
'''

@on_command('refuse_classification', aliases={'是什么垃圾', '属于什么垃圾'})
async def refuse_classification(session: CommandSession):
    trash = session.get('trash', prompt='你想查询什么垃圾')
    await session.send("正在查询中，请稍候~")
    trash_result = await get_the_sort_of_trash(trash)
    await session.send(trash_result)


@refuse_classification.args_parser
async def _(session: CommandSession):
    stripped_arg = participle(session.current_arg_text.strip())
    if stripped_arg:
        session.state['trash'] = stripped_arg
        return
    else:
        session.pause('不存在这种垃圾呢，请重新输入')


@on_natural_language(keywords={'是什么垃圾', '属于什么垃圾'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    trash = participle(stripped_msg)
    return IntentCommand(90.0, 'refuse_classification', current_arg=trash)
