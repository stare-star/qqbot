import re

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '15836561'
API_KEY = 'fxS5FV833jSpSt9GxaCXrRtL'
SECRET_KEY = 'eUbWz6WMQmZuewbkQP1PxImOYOqFNHfG'


client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# image = get_file_content('example.jpg')


def ocr(image):
    res = client.basicGeneral(image)

    res_str=''
    for i  in (res['words_result']):
            print(i['words'])
            res_str+=i['words']+"\n"
    print(res_str)
    return res_str
def ocr_url(url):
    res =  client.basicGeneralUrl(url)


    res_str=f''
    for i  in (res['words_result']):
            print(i['words'])
            res_str+=i['words']+"\n"
    print(res_str)
    return str(res_str)

def get_ocr_result(fileName):
    image = get_file_content(fileName)
    res = ocr(image)
    return res

def get_ocr_result_by_url(url):
    res = ocr_url(url)

    return res

def getImag(html):                        #传人捕获网页全部数据
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    url = re.findall(imgre, html)
    return url

if __name__ == '__main__':

    url=r"https://c2cpicdw.qpic.cn/offpic_new/1023256421//b414e9b1-813f-4d50-940a-4ee4372d0002/0?vuin=1513464657&amp;amp;term=2"
    # get_ocr_result(fileName)
    get_ocr_result_by_url(url)