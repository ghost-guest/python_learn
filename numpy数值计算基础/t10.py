#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-03 18:59:15
@LastEditors: ghost-guest
@LastEditTime: 2020-03-03 19:20:17
@FilePath: /pyenv/numpy数值计算基础/t10.py
@Description: 
'''
import numpy as np

'''
求和、求积、差分
下面这些方法用于数组内元素或数组间进行求和、求积以及进行差分。

numpy.prod(a, axis, dtype, keepdims)：返回指定轴上的数组元素的乘积。
numpy.sum(a, axis, dtype, keepdims)：返回指定轴上的数组元素的总和。
numpy.nanprod(a, axis, dtype, keepdims)：返回指定轴上的数组元素的乘积, 将 NaN 视作 1。
numpy.nansum(a, axis, dtype, keepdims)：返回指定轴上的数组元素的总和, 将 NaN 视作 0。
numpy.cumprod(a, axis, dtype)：返回沿给定轴的元素的累积乘积。
numpy.cumsum(a, axis, dtype)：返回沿给定轴的元素的累积总和。
numpy.nancumprod(a, axis, dtype)：返回沿给定轴的元素的累积乘积, 将 NaN 视作 1。
numpy.nancumsum(a, axis, dtype)：返回沿给定轴的元素的累积总和, 将 NaN 视作 0。
numpy.diff(a, n, axis)：计算沿指定轴的第 n 个离散差分。
numpy.ediff1d(ary, to_end, to_begin)：数组的连续元素之间的差异。
numpy.gradient(f)：返回 N 维数组的梯度。
numpy.cross(a, b, axisa, axisb, axisc, axis)：返回两个(数组）向量的叉积。
numpy.trapz(y, x, dx, axis)：使用复合梯形规则沿给定轴积分。
'''
a = np.arange(10)  # 生成 0-9
print(a)  # 输出 a 的值

b = np.sum(a)
print(b)
# a = '1,2,3,4,5'
# print(','.join(a.split(',')[:-1]))
c = np.diff(a)
print(c)
