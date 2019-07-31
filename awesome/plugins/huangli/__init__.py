'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2019-07-29 21:02
@desc:
'''
#查黄历
import socket, requests
from nonebot import on_command, CommandSession

@on_command("huangli", aliases = ("黄历", "查黄历"), only_to_me=False)
async def huangli(session: CommandSession):
    huangli = chahuangli()
    await session.send(huangli)
def chahuangli():
    hlurl = "http://m.laohuangli.net/"
    hl = requests.get(hlurl)
    hl.encoding = "gb2312"
    hlraw = hl.text
    return timecut(hlraw) + yijicut(hlraw)

def timecut(html):
    key1 = '<span class="txt1">'
    key2 = '</span>'
    content = html.partition(key1)[2]
    content = content.partition(key2)[0]
    return  "农历  " + content # 得到网页的内容

def yijicut(html):
    key1 = '<div class="neirong_Yi_Ji">'
    key2 = '</div>'
    content1 = html.partition(key1)[2]
    content2 = content1.partition(key2)[0]
    jry  = "\n今日宜：" + content2.replace('<br/>','　')
    content1 = content1.partition(key1)[2]
    content2 = content1.partition(key2)[0]
    jrj  = "今日忌：" + content2.replace('<br/>','　')
    return jry + "\n" + jrj