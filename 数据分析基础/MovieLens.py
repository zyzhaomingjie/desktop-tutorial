# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:16:33 2020

@author: ZMJ
"""


import pandas as pd

grade = pd.read_csv('ratings.csv')

###求取每一档有多少部电影
bins = [0, 1, 2, 3, 4, 5]
grade['cuts'] = pd.cut(grade['rating'], bins)
counts = pd.value_counts(grade['cuts'])

###添加comment标签
def panduan(x):
    if x > 4 :
        return '推荐'
    else:
        return '不推荐'

grade['comment'] = grade['rating'].apply(lambda x : panduan(x))
