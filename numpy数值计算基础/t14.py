#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-04 19:12:26
@LastEditors: ghost-guest
@LastEditTime: 2020-03-04 19:20:24
@FilePath: /pyenv/numpy数值计算基础/t14.py
@Description: 
'''
import numpy as np
# 数组切片
# Ndarray[start:stop:step]
# [start:stop:step] 分别代表 [起始索引:截至索引:步长]。对于一维数组：
# 一维的等同于list
a = np.arange(10)
print(a)
print(a[:3])
a = np.arange(20).reshape(4,5)
print(a)
print(a[0:3,2:4])
# 我们可以使用 numpy.sort方法对多维数组元素进行排序。其方法为
# numpy.sort(a, axis=-1, kind='quicksort', order=None)
"""
a：数组。
axis：要排序的轴。如果为None，则在排序之前将数组铺平。默认值为 -1，沿最后一个轴排序。
kind：{'quicksort'，'mergesort'，'heapsort'}，排序算法。默认值为 quicksort。
"""
a = np.arange(10).reshape(2,5)
print(a)
c = np.sort(a)
print(c)
"""

除了 numpy.sort，还有这样一些对数组进行排序的方法：

numpy.lexsort(keys ,axis)：使用多个键进行间接排序。
numpy.argsort(a ,axis,kind,order)：沿给定轴执行间接排序。
numpy.msort(a)：沿第 1 个轴排序。
numpy.sort_complex(a)：针对复数排序。
"""
