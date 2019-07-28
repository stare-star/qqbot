# @Time  : 2019/3/23 0023 11:06
# @Author: LYX
# @File  : weather.py

import requests
# r = requests.get('http://www.weather.com.cn/data/sk/101191101.html')

# url_realtime='https://api.caiyunapp.com/v2/TAkhjf8d1nlSlspN/119.9805620000,31.8186570000/realtime.json'
# url_daily="https://api.caiyunapp.com/v2/TAkhjf8d1nlSlspN/119.9805620000,31.8186570000/daily.json?dailysteps=2"
# r=requests.get(url=url_daily)
# r.encoding = 'utf-8'
# print(r.text)

# # print( r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp'])

# 当日的气温
# print(r.json()["result"]["daily"]["temperature"][0])
# print(r.json()["result"]["daily"]["temperature"][1])

# 状态 多云   下雨等
# print(r.json()["result"]["daily"]["skycon"])
# print(r.json()["result"]["daily"]["skycon_08h_20h"])
# print(r.json()["result"]["daily"]["skycon_20h_32h"])

import requests

tran = {"CLEAR_DAY": "晴（白天）",
        "CLEAR_NIGHT": "晴（夜间）",
        "PARTLY_CLOUDY_DAY": "多云（白天）",
        "PARTLY_CLOUDY_NIGHT": "多云（夜间）",
        "CLOUDY": "阴",
        "WIND": "大风",
        "HAZE": "雾霾",
        "RAIN": "雨",
        "SNOW": "雪",

        }


def get_weather():
    url_daily = "https://api.caiyunapp.com/v2/TAkhjf8d1nlSlspN/119.9805620000,31.8186570000/daily.json?dailysteps=2"
    r = requests.get(url=url_daily)
    r.encoding = 'utf-8'
    weather = []
    try:
        weather.append(r.json()["result"]["daily"]["temperature"][0])
        weather.append(r.json()["result"]["daily"]["temperature"][1])
        weather.append(r.json()["result"]["daily"]["skycon"])
        weather.append(r.json()["result"]["daily"]["skycon_08h_20h"])
        weather.append(r.json()["result"]["daily"]["skycon_20h_32h"])
    except:
        weather = "failed"
    return weather


if __name__ == '__main__':

    weather=get_weather()
    print(weather)
# str ="河海大学常州校区\n " +str(weather[0]['date'])+'   '+tran[str(weather[3][0]['value'])]+'   '+tran[str(weather[4][0]['value'])]+'   '+  str(weather[0]['min'])+"-"+str(weather[0]['max']) +'   '+'平均气温'+ str(weather[0]['avg'])+'\n '+str(weather[1]['date'])+'   '+tran[str(weather[3][1]['value'])]+'   '+tran[str(weather[4][1]['value'])]+'   '+  str(weather[1]['min'])+"-"+str(weather[1]['max']) +'   '+'平均气温'+ str(weather[1]['avg'])

# print(str)
#
# 晴（白天）	CLEAR_DAY
# 晴（夜间）	CLEAR_NIGHT
# 多云（白天）	PARTLY_CLOUDY_DAY
# 多云（夜间）	PARTLY_CLOUDY_NIGHT
# 阴	CLOUDY
# 大风	WIND
# 雾霾	HAZE
# 雨	RAIN
# 雪	SNOW

# print(tran["CLEAR_DAY"])
