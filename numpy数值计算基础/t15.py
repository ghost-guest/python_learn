#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-04 19:20:49
@LastEditors: ghost-guest
@LastEditTime: 2020-03-04 19:22:33
@FilePath: /pyenv/numpy数值计算基础/t15.py
@Description: 
'''
import numpy as np
"""
搜索和计数
除了排序，我们可以通过下面这些方法对数组中元素进行搜索和计数。列举如下：

argmax(a ,axis,out)：返回数组中指定轴的最大值的索引。
nanargmax(a ,axis)：返回数组中指定轴的最大值的索引,忽略 NaN。
argmin(a ,axis,out)：返回数组中指定轴的最小值的索引。
nanargmin(a ,axis)：返回数组中指定轴的最小值的索引,忽略 NaN。
argwhere(a)：返回数组中非 0 元素的索引,按元素分组。
nonzero(a)：返回数组中非 0 元素的索引。
flatnonzero(a)：返回数组中非 0 元素的索引,并铺平。
where(条件,x,y)：根据指定条件,从指定行、列返回元素。
searchsorted(a,v ,side,sorter)：查找要插入元素以维持顺序的索引。
extract(condition,arr)：返回满足某些条件的数组的元素。
count_nonzero(a)：计算数组中非 0 元素的数量。
"""

a = np.random.randint(0, 10, 20)
print(a)
print(np.argmax(a))
print(np.argmin(a))
print(np.nonzero(a))
print(np.count_nonzero(a))
