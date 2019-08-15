'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: film.py
@time: 2019-08-14 21:41
@desc:
'''

import requests
from bs4 import BeautifulSoup
from awesome.plugins.short_url.short_url_api import shorten


def search_url(name):
    n_url = name
    s_url = str('https://www.douban.com/search?q=') + str(n_url)
    s_data = requests.get(s_url).text
    s_soup = BeautifulSoup(s_data, 'html.parser')
    url_div = s_soup.find(class_="result")
    url_soup = url_div.find('a')
    url = url_soup.get('href')

    return url


def search_info(url):
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")

    film_soup = soup.find(property="v:itemreviewed")

    info_soup = soup.find(id="info")

    director_soup = info_soup.find(class_="attrs")
    director_a = director_soup.find_all('a')
    time_soup = info_soup.find(property="v:runtime")
    attr_div = soup.find(class_="actor")
    attr_a = attr_div.find_all('a')

    d_name = ''
    for dir_name in director_a:
        d_name = d_name + dir_name.string + ','

    a_name = ''
    for name in attr_a:
        a_name = a_name + name.string + ','

    sum_soup = soup.find(property="v:summary")
    sum = sum_soup.text.replace(" ", "")
    url = shorten(url)
    all = '网页链接：' + url + '\n' + '电影名称：' + film_soup.string + '\n' + '导演：' + d_name + '\n' + '主演：' + a_name + '\n' + '片长：' + time_soup.string + '\n' + '简介：' + sum + '\n'
    return all


def search_film(name):
    url = search_url(name)
    al = search_info(url)
    return al


if __name__ == '__main__':
    name = '战狼'
    al = search_film(name)
    print(al)
