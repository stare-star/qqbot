import requests
from bs4 import BeautifulSoup
# url='http://my.hhu.edu.cn/login/Search.jsp'
# data={}
# data['queryValue']='1762410319'
# print(data['queryValue'])
# r=requests.post(url=url,data=data)
#
#
# soup = BeautifulSoup(r.text,"lxml")
# number=len(soup.find_all("td", bgcolor="#FFFFFF"))/3
# str=''
# for i in range(int(number)):
#     print(soup.find_all("td", bgcolor="#FFFFFF")[3*i].text, soup.find_all("td", bgcolor="#FFFFFF")[3*i+1].text,soup.find_all("td", bgcolor="#FFFFFF")[3*i+2].text)
#     str+=soup.find_all("td", bgcolor="#FFFFFF")[3*i].text+soup.find_all("td", bgcolor="#FFFFFF")[3*i+1].text+soup.find_all("td", bgcolor="#FFFFFF")[3*i+2].text+'\n'
#
# print(str)

def search(name):
    url = 'http://my.hhu.edu.cn/login/Search.jsp'
    data = {}
    data['queryValue'] = name
    r = requests.post(url=url, data=data)
    soup = BeautifulSoup(r.text, "lxml")
    number = len(soup.find_all("td", bgcolor="#FFFFFF")) / 3
    res = ''
    for i in range(int(number)):
        print(soup.find_all("td", bgcolor="#FFFFFF")[3 * i].text,
              soup.find_all("td", bgcolor="#FFFFFF")[3 * i + 1].text,
              soup.find_all("td", bgcolor="#FFFFFF")[3 * i + 2].text)
        res += soup.find_all("td", bgcolor="#FFFFFF")[3 * i].text +'\t'+ soup.find_all("td", bgcolor="#FFFFFF")[
            3 * i + 1].text +'\t'+ soup.find_all("td", bgcolor="#FFFFFF")[3 * i + 2].text + '\n'

    return res


if __name__ == '__main__':
    print(search("张一诺"))


