'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: zhuhu.py
@time: 2019-07-31 13:26
@desc:
'''
from nonebot import on_command, CommandSession
import aiohttp

__plugin_name__ = '知乎日报'
__plugin_usage__ = r"""
命令名称:知乎日报
使用方法:知乎日报
"""


@on_command('知乎日报')
async def news(session: CommandSession):
    STORY_URL_FORMAT = 'https://daily.zhihu.com/story/{}'
    async with aiohttp.request('GET', 'https://news-at.zhihu.com/api/4/news/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}) as resp:
        data = await resp.json()
        stories = data.get('stories')
        if not stories:
            await session.send('暂时没有数据, 或者服务无法访问')
            return
        reply = ''
        for story in stories:
            url = STORY_URL_FORMAT.format(story['id'])
            title = story.get('title', '未知内容')
            images = story.get('images')
            print(images)
            reply += f'\n{title}\n{url}\n [CQ:image,file={images[0]}] \n'
        await session.send(reply)