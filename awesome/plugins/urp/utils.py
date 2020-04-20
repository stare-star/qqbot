# from PIL import Image
# from http.cookiejar import CookieJar
# from urllib.request import build_opener, HTTPCookieProcessor, Request
# from urllib.parse import urlencode
import time

import pytesseract
import requests
from PIL import Image

rep = {'|': '1',  # 替换列表
       '¥': 'Y',
       '&': '8',
       '\\': '1',
       '/': '1',
       '#': 'g',
       '‘': '',
       'i': 'j',
       ' .': '',
       '"': '',
       'c': 'g',
       '£': 'f',
       'é': '8'

       };


def initTable(threshold=140):  # 二值化函数
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table


# --------------------------------------------------------------------------------------


def code():
    image = Image.open("yzm.jpg")
    im = image.convert('L')  # 2.将彩色图像转化为灰度图
    binaryImage = im.point(initTable(), '1')  # 3.降噪，图片二值化
    text = pytesseract.image_to_string(binaryImage, lang='eng', config='-psm 7', nice=8)  # 使用简体中文解析图片
    text = text.replace(' ', '')
    for r in rep:
        text = text.replace(r, rep[r])
    # print(text+'---'+str(n))
    # with open('zym.txt','a') as f:
    #   f.write(text+'\n')
    # os.rename((str(n)+".jpg",text+'.jpg')
    return text


def code_self():
    h = Image.open('yzm.jpg')
    h.show()
    text = input('请输入验证码：')
    return text


yzm_url = codeurl = 'http://urp.luyangxing.com/validateCodeAction.do?random=0.0480646841204162'
post_url = Url = 'http://urp.luyangxing.com/loginAction.do'
Header = {'Host': 'jwurp.hhuc.edu.cn',
          'Origin': 'http://jwurp.hhuc.edu.cn',
          'Referer': 'http://jwurp.hhuc.edu.cn/',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
Header2 = {'Host': 'jwurp.hhuc.edu.cn',
           'Origin': 'http://jwurp.hhuc.edu.cn',
           'Referer': 'http://jwurp.hhuc.edu.cn/menu/mainFrame.jsp',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}


def download_img(name, session, cookies):
    img_url = r'http://urp.luyangxing.com/xjInfoAction.do?oper=img'
    headers = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': cookies,
        'Host': 'jwurp.hhuc.edu.cn',
        'Referer': 'http://jwurp.hhuc.edu.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    }
    # 保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片
    imgdata = session.get(img_url, headers=headers)  # 获取头像
    with open(name, 'wb') as f:
        # 将response的二进制内容写入到文件中
        f.write(imgdata.content)
    return 1


# async
async def login(id, passwd):
    count = 1
    while True:
        session = requests.session()  # 建立会话，保持会话信息，cookies
        r = session.get(post_url)
        cookies = r.headers['Set-Cookie']  # 获取cookies
        cookies = cookies.strip('; path=/')  # 删除指定字符，这里是由于 我学

        yam_headers = {
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': cookies,
            'Host': 'jwurp.hhuc.edu.cn',
            'Referer': 'http://jwurp.hhuc.edu.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
        }

        # 这是获取验证码的表头，这里的链接通google浏览器的开发者工具，按照前面说的去找。
        yamdata = session.get(yzm_url, headers=yam_headers)  # 获取验证码
        with open('yzm.jpg', 'wb') as f:

            # 将response的二进制内容写入到文件中
            f.write(yamdata.content)

        # h=Image.open('yzm.jpg')
        # h.show()
        # code = input('请输入验证码：')
        logindata = {'zjh': id,
                     'mm': passwd}

        logindata['v_yzm'] = code()
        print(logindata['v_yzm'])
        login_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '37',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '',
            'Host': 'jwurp.hhuc.edu.cn',
            # 'Origin': '*********'
            'Referer': 'http://jwurp.hhuc.edu.cn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
        }
        login_headers['Cookie'] = cookies
        d = session.post(post_url, data=logindata, headers=login_headers)  # 将账号，密码，验
        print(d.text.find('#990000'))

        if d.text.find('#990000') == -1:
            break
        else:
            count += 1
            print(count)
        if count == 10:
            print('失败')
            return 0

    return session, cookies


async def getHtml(session, cookies):
    # download_img('1.jpg',session,cookies)
    url_cj_this = 'http://urp.luyangxing.com/bxqcjcxAction.do'
    link_176241cj = 'http://jwurp.hhuc.edu.cn/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=1240'  # 成绩
    link_186231cj = "http://jwurp.hhuc.edu.cn/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=1494"  # 18级成绩
    # http://jwurp.hhuc.edu.cn/xjInfoAction.do?oper=xjxx  信息
    # http://jwurp.hhuc.edu.cn/gradeLnAllAction.do?type=ln&oper=qb
    Student_link = 'http://jwurp.hhuc.edu.cn/xjInfoAction.do?oper=xjxx'
    Photo_link = 'http: // jwurp.hhuc.edu.cn / xjInfoAction.do?oper = img '

    Headers = {
        'Cookie': cookies,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
    }

    # if str(id)[0:6] == '176241':
    #     link_cj = link_176241cj
    # elif str(id)[0:6] == '186231':
    #     link_cj = link_186231cj
    # else:
    #     return 404, "暂时无法查询该年级专业"
    # print(link_cj)
    cj = requests.get(url_cj_this, headers=Headers)
    cj.encoding = 'GBK'
    with open("bxqcjcx.html", "wb") as html:
        html.write(cj.content)

    # xx = requests.get(Student_link, headers=Headers)
    # xx.encoding = 'GBK'
    # with open("demo2.html", "wb") as html:
    #     html.write(xx.content)

    # photo = requests.get(Student_link, headers=Headers,)
    # with open(r'photo/'+str(id)+".jpg", "wb") as ph:
    #     ph.write(photo.iter_content(1000))
    # #http: // jwurp.hhuc.edu.cn / xjInfoAction.do?oper = img  照片
    session.close()
    return 200, cj.content


from bs4 import BeautifulSoup

from awesome.plugins.urp.course import add_info


# def record(html):
#     soup = BeautifulSoup(open(html), 'lxml')
#     re = soup.find_all('table', class_='titleTop2')
#     lines = re[0].find_all('tr')  # 表
#     # print(lines[1])
#     # print(len(lines))
#     titles = lines[1].find_all('th')
#     for title in titles:
#         print(title.text)
#
#     lines = re[0].find_all(class_='odd')  # 成绩表
#     print(len(lines))
#     cells = lines[0].find_all('td')
#
#     # for cell in cells:
#     #     print(cell.text)
#
#     for line in lines:
#         cells = line.find_all('td')
#         course_list = []
#         for cell in cells:
#             print(cell.text)
#             course_list.append(cell.text.strip())
#         add_info(course_list[0], 176241000, course_list[1], course_list[2], course_list[3], course_list[4],
#                  course_list[5], course_list[6])
#



def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    re = soup.find_all('table', class_='titleTop2')
    lines = re[0].find_all('tr')  # 表
    # print(lines[1])
    # print(len(lines))
    titles = lines[1].find_all('th')
    for title in titles:
        print(title.text)

    lines = re[0].find_all(class_='odd')  # 成绩表
    res=[]
    for line in lines:
        cells = line.find_all('td')
        course_list = []

        print(cells[2].text)
        course_list.append(cells[2].text.strip())
        course_list.append(cells[4].text.strip())
        course_list.append(cells[5].text.strip())
        course_list.append(cells[9].text.strip())

        res.append(course_list)

    return res



if __name__ == '__main__':
    # id = 1862310211
    # passwd = "zyn20001228"
    # search(id, passwd)
    # id = 1762410319
    # passwd = "1dasds57sxaxasc"
    # seesion, cookies =  login(id, passwd)
    # getHtml(seesion, cookies)



    c=parse('bxqcjcx.html')
    for i in c:
        print(i[2])
        print(i[9])

# for i in range(40):
#     work(id)
#     print(id)
#     time.sleep(10)
#     id += 1
