from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

from config import user
from awesome.plugins.daily_weather.weather_API import get_weather, tran


# 时差-8
@nonebot.scheduler.scheduled_job("cron", day_of_week='*', hour='22', minute='30', second='00',
                                 timezone=pytz.timezone('Asia/Shanghai'))
async def _():
    bot = nonebot.get_bot()
    try:
        weather = get_weather()
        str_weather = "河海大学常州校区\n " + str(weather[0]['date']) + '   ' + tran[str(weather[3][0]['value'])] + '   ' + \
                      tran[
                          str(weather[4][0]['value'])] + '   ' + str(weather[0]['min']) + "-" + str(
            weather[0]['max']) + '   ' + '平均气温' + str(weather[0]['avg']) + '\n ' + str(weather[1]['date']) + '   ' + \
                      tran[str(weather[3][1]['value'])] + '   ' + tran[str(weather[4][1]['value'])] + '   ' + str(
            weather[1]['min']) + "-" + str(weather[1]['max']) + '   ' + '平均气温' + str(weather[1]['avg'])

        await bot.send_private_msg(user_id=user, message=str_weather)

    except CQHttpError:
        pass
