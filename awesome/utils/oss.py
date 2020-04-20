# coding:utf-8

'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: oss.py
@time: 2020-04-16 21:16
@desc:
'''
from shutil import move
import sys
from shutil import copyfile
import oss2
from random import choice
from config import oss_ACCESS_KEY_ID, oss_ACCESS_KEY_SECRET

map = ["a", "b", "c", "d", "e", "f", "g", "h",
       "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
       "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5",
       "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H",
       "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
       "U", "V", "W", "X", "Y", "Z"]


def url_s(m):
    url = ""
    for i in range(m):
        url = url + str(choice(map))
    return url


# 随机生成短链
def get_shourt_file_name(local_name, m):
    name = url_s(m)
    local_name = str(local_name).rsplit(".")
    return "pics/%s.%s" % (name, local_name[-1])


BUCKET_NAME = "lyx-tc"
PRE = "http://**.**.**.**:88/img/"
PRE_A = "https://pics.starfishs.cn/"
PRE_B = "https://lyx-tc.oss-cn-shanghai.aliyuncs.com/"
length = 5
PIC_STYLE = ""
ENDPOINT = "oss-cn-shanghai.aliyuncs.com"
ACCESS_KEY_ID = oss_ACCESS_KEY_ID
ACCESS_KEY_SECRET = oss_ACCESS_KEY_SECRET


def upload( src_file):
    # 获取文件路径
    auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
    bucket = oss2.Bucket(auth, ENDPOINT, BUCKET_NAME)

    remote_file_name = get_shourt_file_name(src_file, int(length))

    bucket.put_object_from_file(remote_file_name, src_file)  # 上传文件
    result_str = "%s%s%s" % (PRE_B, remote_file_name, PIC_STYLE)
    print(result_str)
    print('上传完成')
    return result_str



