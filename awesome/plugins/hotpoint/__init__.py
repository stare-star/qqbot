'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2019-07-29 21:00
@desc:
'''
#百度热点
import datetime

import pytz
import requests
from bs4 import BeautifulSoup
from config import group_id
import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
@nonebot.scheduler.scheduled_job("cron", day_of_week='*', hour='8', minute='0', second='00',timezone=pytz.timezone('Asia/Shanghai'))
async def _():
    nowhotp = "        当前热点          热度"
    for num in range(0, 20):
        nowhotp = nowhotp + "\n" + getnowhotp()[num]
    global switch
    switch = 1
    try:
        bot = nonebot.get_bot()
        await bot.send_group_msg(group_id=group_id,
                                 message=nowhotp)
        bot.logger.info('发送热点')
    except CQHttpError:
        pass


from nonebot import on_command, CommandSession
switch = 0
@on_command("newhotpoint", aliases=("热点", "当前热点"), only_to_me=False)
async def nowhot(session: CommandSession):
    nowhotp = "        当前热点          热度"
    for num in range(0,20):
        nowhotp = nowhotp + "\n" + getnowhotp()[num]
    global switch
    switch = 1
    await session.send(nowhotp)

@on_command("tdhotpoint", aliases=("今日热点", "今天热点"), only_to_me=False)
async def tdhot(session: CommandSession):
    tdhotp = "        今日热点          热度"
    for num in range(0,20):
        tdhotp = tdhotp + "\n" + gettdhotp()[num]
    global switch
    switch = 2
    await session.send(tdhotp)

@on_command("givemeurl", aliases=("链接", "告诉我链接"), only_to_me=False)
async def gmurl(session:  CommandSession):
    if switch != 0:
        session.get("number", prmopt="你想知道那一条的链接？")
        url = await geturl(session.args["number"])
        await session.send(url)
    else:
        await session.finish("还没有加载任何新闻!")

@gmurl.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.args["number"] = stripped_arg

def getnowhotp():
    global nowurl
    nowurl = []
    url = "http://top.baidu.com/buzz?b=1"
    nowhotall = requests.get(url)
    nowhotall.encoding = "gb2312"
    nowhotraw = BeautifulSoup(nowhotall.text, "html.parser")
    nowtitlehraw = nowhotraw.find("table")
    nowtitle = nowtitlehraw.find_all(class_="list-title")
    nowscore = nowtitlehraw.find_all("td", class_="last")
#统一格式化
    for title in range(0,50):
        nowurl.append (nowtitle[title]["href"])
        nowtitle[title] = nowtitle[title].string
        nowscore[title] = nowscore[title].find("span")
        nowscore[title] = nowscore[title].string
        nowtitle[title] = str(title + 1) + ". " + nowtitle[title] + "    " + nowscore[title]
    return nowtitle

def gettdhotp():
    global tdurl
    tdurl = []
    url = "http://top.baidu.com/buzz?b=341"
    tdhotall = requests.get(url)
    tdhotall.encoding = "gb2312"
    tdhotraw = BeautifulSoup(tdhotall.text, "html.parser")
    tdtitlehraw = tdhotraw.find("table")
    tdtitle = tdtitlehraw.find_all(class_="list-title")
    tdscore = tdtitlehraw.find_all("td", class_="last")
#统一格式化
    for title in range(0,50):
        tdurl.append (tdtitle[title]["href"])
        tdtitle[title] = tdtitle[title].string
        tdscore[title] = tdscore[title].find("span")
        tdscore[title] = tdscore[title].string
        tdtitle[title] = str(title + 1) + ". " + tdtitle[title] + "    " + tdscore[title]
    return tdtitle

async def geturl(number: str) -> str:
    global nowurl, tdurl, switch
    if switch == 1:
        return nowurl[int(number)-1]
    elif switch == 2:
        return tdurl[int(number)-1]#百度热点
import requests
from bs4 import BeautifulSoup

from nonebot import on_command, CommandSession
switch = 0


@on_command("newhotpoint", aliases=("热点", "当前热点"), only_to_me=False)
async def nowhot(session: CommandSession):
    nowhotp = "        当前热点          热度"
    for num in range(0,20):
        nowhotp = nowhotp + "\n" + getnowhotp()[num]
    global switch
    switch = 1
    await session.send(nowhotp)

@on_command("tdhotpoint", aliases=("今日热点", "今天热点"), only_to_me=False)
async def tdhot(session: CommandSession):
    tdhotp = "        今日热点          热度"
    for num in range(0,20):
        tdhotp = tdhotp + "\n" + gettdhotp()[num]
    global switch
    switch = 2
    await session.send(tdhotp)

@on_command("givemeurl", aliases=("链接", "告诉我链接"), only_to_me=False)
async def gmurl(session:  CommandSession):
    if switch != 0:
        session.get("number", prmopt="你想知道那一条的链接？")
        url = await geturl(session.args["number"])
        await session.send(url)
    else:
        await session.finish("还没有加载任何新闻!")

@gmurl.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.args["number"] = stripped_arg

def getnowhotp():
    global nowurl
    nowurl = []
    url = "http://top.baidu.com/buzz?b=1"
    nowhotall = requests.get(url)
    nowhotall.encoding = "gb2312"
    nowhotraw = BeautifulSoup(nowhotall.text, "html.parser")
    nowtitlehraw = nowhotraw.find("table")
    nowtitle = nowtitlehraw.find_all(class_="list-title")
    nowscore = nowtitlehraw.find_all("td", class_="last")
#统一格式化
    for title in range(0,50):
        nowurl.append (nowtitle[title]["href"])
        nowtitle[title] = nowtitle[title].string
        nowscore[title] = nowscore[title].find("span")
        nowscore[title] = nowscore[title].string
        nowtitle[title] = str(title + 1) + ". " + nowtitle[title] + "    " + nowscore[title]
    return nowtitle

def gettdhotp():
    global tdurl
    tdurl = []
    url = "http://top.baidu.com/buzz?b=341"
    tdhotall = requests.get(url)
    tdhotall.encoding = "gb2312"
    tdhotraw = BeautifulSoup(tdhotall.text, "html.parser")
    tdtitlehraw = tdhotraw.find("table")
    tdtitle = tdtitlehraw.find_all(class_="list-title")
    tdscore = tdtitlehraw.find_all("td", class_="last")
#统一格式化
    for title in range(0,50):
        tdurl.append (tdtitle[title]["href"])
        tdtitle[title] = tdtitle[title].string
        tdscore[title] = tdscore[title].find("span")
        tdscore[title] = tdscore[title].string
        tdtitle[title] = str(title + 1) + ". " + tdtitle[title] + "    " + tdscore[title]
    return tdtitle

async def geturl(number: str) -> str:
    global nowurl, tdurl, switch
    if switch == 1:
        return nowurl[int(number)-1]
    elif switch == 2:
        return tdurl[int(number)-1]