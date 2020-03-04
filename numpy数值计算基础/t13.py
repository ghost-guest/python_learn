#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-04 19:05:45
@LastEditors: ghost-guest
@LastEditTime: 2020-03-04 19:10:50
@FilePath: /pyenv/numpy数值计算基础/t13.py
@Description: 
'''
import numpy as np

#数组的索引
a = np.random.randint(1,10,6)
print(a)
print(a[1])
print(a[[1,4]])
b = np.arange(20).reshape(4,5)
print(b)
print(b[[1,2],[2,3]])

a = np.arange(30).reshape(2, 5, 3)
print(a)
print(a[[0, 1], [1, 2], [1, 2]])

