'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: film.py
@time: 2019-08-14 21:41
@desc:
'''
import requests
from bs4 import BeautifulSoup



def search_film(n_url):
    s_url='https://www.douban.com/search?q='+n_url
    s_data=requests.get(s_url).text
    s_soup=BeautifulSoup(s_data,'html.parser')

    url_div=s_soup.find(class_="result")
    url_soup=url_div.find('a')
    url=url_soup.get('href')
    print('网页链接：',url)

    data=requests.get(url).text
    soup=BeautifulSoup(data,"html.parser")
    film_soup=soup.find(property="v:itemreviewed")

    info_soup=soup.find(id="info")
    director_soup=info_soup.find(class_="attrs")
    director_a=director_soup.find_all('a')
    time_soup=info_soup.find(property="v:runtime")
    attr_div=soup.find(class_="actor")
    attr_a=attr_div.find_all('a')
    print('电影名称：',film_soup.string)
    print('导演：')
    for dir_name in director_a:
        print(dir_name.string)
    print('主演：')
    for name in attr_a:
        print(name.string)
    print('片长：',time_soup.string)


