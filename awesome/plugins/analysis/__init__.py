# coding:utf-8

'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: __init__.py.py
@time: 2020-04-16 20:43
@desc:
'''
import pytz

from config import user
from aiocqhttp.exceptions import Error as CQHttpError

from awesome.utils.oss import upload
import os
from nonebot import on_natural_language, NLPSession, IntentCommand, on_command, CommandSession
import datetime
import time
from awesome.plugins.short_url.short_url_api import shorten_lyx


# todo 昨日回顾

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    if session.ctx['group_id'] == "827699992" or "252414185":
        print(session.ctx['group_id'])
        print(session.ctx['sender']['nickname'])
        print(session.msg_text)
        with open(str(session.ctx['group_id']) + "log" + str(datetime.date.today()) + ".txt", 'a')as f:
            f.write(str(session.ctx['sender']['nickname']) + "*" + str(int(time.time())) + "*" + str(
                session.msg_text) + "\n")


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import jieba.analyse


def analy(file):
    with open(file, 'r')as f:
        lines = f.readlines()
        dict = {}
        for line in lines:
            line = line.split("*")

            dict[line[0].strip()] = dict.get(line[0].strip(), "") + "  " + str(line[2]).strip()
        str_text = ''
        for k, v in dict.items():
            str_text += v
        print(str_text)
        # str_text=r"新冠肺炎疫情发生以来，人民军队坚决贯彻习近平主席重要指示，自1月24日开始，从陆军、海军、空军、火箭军、战略支援部队、联勤保障部队、武警部队多个医疗单位，分3批次抽组4000余名医务人员，支援武汉抗击新冠肺炎疫情。从支援武汉金银潭医院、武昌医院和汉口医院病区，到进驻武汉火神山医院、武汉市泰康同济医院、湖北省妇幼保健院光谷院区，军队医务人员牢记人民军队宗旨，闻令而动，勇挑重担，敢打硬仗，同时间赛跑，与病魔较量，在疫情防控战场上发起一次次冲锋，全力保护人民生命安全和身体健康。各级党组织和广大党员冲锋在前、顽强拼搏，充分发挥战斗堡垒作用和先锋模范作用，在大战中践行初心使命、交出合格答卷。"
        tags = jieba.analyse.extract_tags(str_text, topK=20, withWeight=False)
        text = " ".join(tags)
        print(os.path.join(os.getcwd(), r"awesome/plugins/analysis/mqrtt.ttf"))
        wc = WordCloud(background_color='white',  # 背景颜色
                       max_words=2000,  # 词云显示的最大词数
                       max_font_size=200,  # 字体最大值
                       min_font_size=10,
                       mode='RGBA',
                       font_path=os.path.join(os.getcwd(), r"awesome/plugins/analysis/mqrtt.ttf"),
                       # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
                       random_state=40  # 颜色种类
                       )
        wc.generate(text)
        wc.to_file('123.png')
        img_url = upload('123.png')
        return img_url, text


@on_command('analysis', aliases={"分析"})
async def run(session: CommandSession):
    print(os.getcwd())
    img, text = analy(os.path.join(os.getcwd(), str(827699992) + "log" + str(datetime.date.today()) + ".txt"))
    img = shorten_lyx(img)
    await session.send(text + "\n" + img)


import nonebot


@nonebot.scheduler.scheduled_job("cron", day_of_week='*', hour='23', minute='0', second='00',
                                 timezone=pytz.timezone('Asia/Shanghai'))
async def _():
    global switch
    switch = 1

    img, text = analy(os.path.join(os.getcwd(), str(827699992) + "log" + str(datetime.date.today()) + ".txt"))
    img = shorten_lyx(img)
    try:
        bot = nonebot.get_bot()
        await bot.send_private_msg(user_id=user, message=text + "\n" + img)

        bot.logger.info('发送词云')
    except CQHttpError:
        pass


if __name__ == '__main__':
    analy(r"C:\Users\stare-star\Desktop\code\qqbot\252414185log.txt")
