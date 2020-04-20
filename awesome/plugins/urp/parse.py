from bs4 import BeautifulSoup

from awesome.plugins.urp.course import add_info


def parse(html):
    soup = BeautifulSoup(open(html), 'lxml')
    re = soup.find_all('table', class_='titleTop2')
    lines = re[0].find_all('tr')  # 表
    # print(lines[1])
    # print(len(lines))
    titles = lines[1].find_all('th')
    for title in titles:
        print(title.text)

    lines = re[0].find_all(class_='odd')  # 成绩表
    print(len(lines))
    cells = lines[0].find_all('td')

    # for cell in cells:
    #     print(cell.text)
    course=[]
    for line in lines:
        cells = line.find_all('td')
        course_list=[]
        for cell in cells:
            # print(cell.text)
            course_list.append(cell.text.strip())
        print(course_list)
        course.append(course_list)
        # add_info(course_list[0],176241000,course_list[1],course_list[2],course_list[3],course_list[4],course_list[5],course_list[6])
    return course


def parse_bk(html):
    soup = BeautifulSoup(html, 'lxml')
    re = soup.find_all('table', class_='titleTop2')
    lines = re[0].find_all('tr')  # 表
    # print(lines[1])
    # print(len(lines))
    titles = lines[1].find_all('th')
    for title in titles:
        print(title.text)
    print(1111111111111111111111111111111111)
    lines = re[0].find_all(class_='odd')  # 成绩表
    print(len(lines))
    cells = lines[0].find_all('td')

    # for cell in cells:
    #     print(cell.text)
    res=[]
    for line in lines:
        cells = line.find_all('td')
        course_list=[]
        for cell in cells:
            print(cell.text)
            course_list.append(cell.text.strip())
        res.append(course_list)
    return res

if __name__ == '__main__':
    c=parse('bxqcjcx.html')
    print(502)
    print(c[9][2])
    print(c[9][9])
