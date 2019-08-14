'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: bilibili.py
@time: 2019-07-29 21:06
@desc:
'''
import re

""" 获取B站番剧的今日更新
"""
import json

import requests
from nonebot import CommandSession, on_command


@on_command('bilibili', only_to_me=False)
async def bilibili_today(session: CommandSession):
    try:
        output = ''
        response = requests.get(
            'https://bangumi.bilibili.com/web_api/timeline_global')
        data = response.content.decode('utf-8')
        rjson = json.loads(data)
        for day in rjson['result']:
            if (day['is_today'] == 1):
                for item in day['seasons']:
                    output += f'{item["pub_time"]} : {item["title"]}  \n  [CQ:image,file={item["square_cover"]}]   \n'

        # 去掉最后一个\n
        await session.send(output[:-1])
    except:
        await session.send('获取番剧信息失败了~>_<~')


@on_command('get_cover', aliases=['封面'])
async def crawl(session: CommandSession):
    target_av = session.current_arg_text
    if target_av.startswith('av'):
        if target_av[2:].isdigit():
            ret = await get_pic(av=target_av)
            await session.finish(ret)
    await session.finish('格式:封面 av号\n例子:封面 av123456')


async def get_pic(av) -> str:
    TARGET_URL = 'http://www.bilibili.com/video/' + av
    html = requests.get(TARGET_URL, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    })

    # if html.find('视频去哪了呢') != -1:
    #     # print(html)
    #     return '视频已经被删除了哟~'
    img_url = re.findall(r'//i[0-9].hdslb.com/bfs/archive/[0-9a-zA-Z\.]+', html)
    if not img_url:
        return '没找到封面哦~'
    pic_url = 'http:' + img_url[0]
    return f'[CQ:image,file={pic_url}]'
