'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: fundapi.py
@time: 2020-01-14 14:29
@desc:
'''
import requests
import time
import json

def getUrlRealTime(fscode):
  head = 'http://fundgz.1234567.com.cn/js/'
  tail = '.js?rt='+ time.strftime("%Y%m%d%H%M%S",time.localtime())
  return head+fscode+tail



def getFundRt(fscode):
    content = requests.get(getUrlRealTime(fscode))
    t=content.text
    fjson=json.loads(t[int(t.find("("))+1:int(t.find(")"))])
    return fjson

if __name__ == '__main__':
    print(getFundRt('005918')['name'])
    print(getFundRt('005918')['gszzl'])