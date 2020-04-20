# coding:utf-8

'''
@author: lyx
@contact: woshiluyangxing@qq.com
@file: python_run.py
@time: 2020-04-15 15:46
@desc:
'''
import random
import numpy as np



# script = 'random.sample(range(15,20),2)'
# print(runpy(script))
#
# print(random.sample(range(15, 20), 2))


def get501(k=1):
    l = ["鲁", "郑", "唐", "王", "马", "何"]
    return np.random.choice(l, k,replace=False)


print(eval('get501(1)'))


print(eval('get501(5)'))
print(eval('get501(1)'))
print(eval('get501(1)'))
print(eval('get501(1)'))
print(eval('get501(1)'))