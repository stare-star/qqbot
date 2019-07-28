import requests

url = 'https://free-api.heweather.net/s6/weather/now?key=ed8124e2f448448297102f6ae9226667&location='


def getweather(city):
    dataJson = requests.get(url+city)
    data = dataJson.json()
    try:
        print(data["HeWeather6"][0]["basic"]['location'])
        return data["HeWeather6"][0]
    except:
        result = "请查询具体城市而非省分"
        return result


def weaList(str):
    list = ''
    list += str["basic"]['cnty'] + "/" + str["basic"]['admin_area'] + "/" + str["basic"]['parent_city'] + "/" + str["basic"]['location'] + '的天气：\n' + \
        '气温：' + str["now"]['tmp'] + '°C\n' + \
        '天气：' + str["now"]['cond_txt'] + '\n' +\
        '风向：' + str["now"]['wind_dir'] + '--' + str["now"]['wind_sc'] + '级(' + str["now"]['wind_spd'] + "Km/h " + ')' + '\n' +\
        '湿度：' + str["now"]['hum'] + '\n' + \
        '能见度：' + str["now"]['vis'] + '公里\n' +\
        '更新时间：' + str["update"]['loc']
    return list


if __name__ == '__main__':
    getweather('天河')