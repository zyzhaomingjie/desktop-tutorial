# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 23:16:48 2020

@author: ZMJ
"""

"""递归函数 """      
def recur(a):
   if a == 1 or a == 2:
       return 1
   else:
       return(recur(a-1) + recur(a-2))
       
"""输出数组"""    
def fib(n):
    fibs = []
    for i in range(1, n + 1):
        fibs.append(recur(i))
    return fibs
