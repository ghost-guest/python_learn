#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-03 18:17:35
@LastEditors: ghost-guest
@LastEditTime: 2020-03-03 18:26:36
@FilePath: /pyenv/numpy数值计算基础/t4.py
@Description: 
'''
import numpy as np

# 数组展开
# numpy.ravel(a, order='C')
# a 表示需要处理的数组。order 表示变换时的读取顺序，
# 默认是按照行依次读取，当 order='F' 时，可以按列依次读取排序。
a = np.arange(10).reshape(2,5)
print(a)
b = np.ravel(a)
print(b)
c = np.ravel(a, order='F')
print(c)
#moveaxis 可以将数组的轴移动到新的位置
# numpy.moveaxis(a, source, destination)
# a：数组。
# source：要移动的轴的原始位置。
# destination：要移动的轴的目标位置。
a = np.ones((1,2,3))
print(a)
b = np.moveaxis(a, 0, -1)
print(b)
print(a.shape)
print(b.shape)
# 和 moveaxis 不同的是，swapaxes 可以用来交换数组的轴
# numpy.swapaxes(a, axis1, axis2)
"""
a：数组。
axis1：需要交换的轴 1 位置。
axis2：需要与轴 1 交换位置的轴 1 位置。
"""
a = np.ones((1, 4, 3))
print(a)

b = np.swapaxes(a, 0, 2)
print(b)
print(a.shape, b.shape)
# 数组转置
# numpy.transpose(a, axes=None)
"""
a：数组。
axis：该值默认为 none，表示转置。如果有值，那么则按照值替换轴。
"""
a = np.arange(4).reshape(2, 2)
print(a)

b = np.transpose(a)
print(b)

