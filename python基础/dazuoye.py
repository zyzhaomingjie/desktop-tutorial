# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:42:15 2020

@author: ZMJ
"""

import csv
from itertools import islice

###一共有多少不同的用户
def get_users():
    user=set()
    with open('tags.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             user.add(row[0])
    with open('ratings.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             user.add(row[0])
    print(len(user))

get_users()

###一共有多少不同的电影
def get_movies():
    movie=set()
    with open('tags.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             movie.add(row[1])
    with open('ratings.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             movie.add(row[1])
    with open('movies.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             movie.add(row[0])
    with open('links.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             movie.add(row[0])
    with open('scores.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             movie.add(row[0])
    print(len(movie))
    return len(movie)
get_movies()

###一共有多少不同的电影种类
def get_movie_kinds():
    movie_kind=set()
    with open('movies.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             lists = row[2].split('|', )
             for list in lists:
                 if list != '(no genres listed)':
                     movie_kind.add(list)
    print(len(movie_kind))
    
get_movie_kinds()
    
###一共有多少电影没有外部链接
def get_movie_no_links():
    movie_no_link=set()
    with open('links.csv', 'r',encoding='utf-8') as f:
         reader = csv.reader(f)        
         for row in islice(reader, 1, None):
             movie_no_link.add(row[0])
    return len(movie_no_link)

a = get_movies()
b = get_movie_no_links()
result = a-b

###2018年一共有多少人进行过电影评分
import pandas as pd
import datetime

def get_2018_users():
    df = pd.read_csv('ratings.csv')
    df['timestamp_1'] = df['timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(x))
    df['year'] = pd.DatetimeIndex(df['timestamp_1']).year
    df_1 = df.query('(year == 2018)')
    print(len(df_1['userId'].drop_duplicates()))

get_2018_users()
    





























    
    
    
    

                            
                            
            
            
            
            
            
            
            
            
