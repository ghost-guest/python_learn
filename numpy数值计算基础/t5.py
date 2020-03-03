#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-03 18:27:01
@LastEditors: ghost-guest
@LastEditTime: 2020-03-03 18:32:52
@FilePath: /pyenv/numpy数值计算基础/t5.py
@Description: 
'''
import numpy as np

# atleast_xd 支持将输入数据直接视为 x维。这里的 x 可以表示：1，2，3。

print(np.atleast_1d([1, 2, 3]))
print(np.atleast_2d([4, 5, 6]))
print(np.atleast_3d([7, 8, 9]))

"""
类型转换
在 NumPy 中，还有一系列以 as 开头的方法，它们可以将特定输入转换为数组，亦可将数组转换为矩阵、标量，ndarray 等。如下：

asarray(a，dtype，order)：将特定输入转换为数组。
asanyarray(a，dtype，order)：将特定输入转换为 ndarray。
asmatrix(data，dtype)：将特定输入转换为矩阵。
asfarray(a，dtype)：将特定输入转换为 float 类型的数组。
asarray_chkfinite(a，dtype，order)：将特定输入转换为数组，检查 NaN 或 infs。
asscalar(a)：将大小为 1 的数组转换为标量。
"""
# 这里以 asmatrix(data，dtype) 方法举例：
a = np.arange(4).reshape(2, 2)
print(a)
b = np.asmatrix(a)  # 将二维数组转化为矩阵类型
print(b)
"""
数组连接
concatenate 可以将多个数组沿指定轴连接在一起。其方法为
numpy.concatenate((a1, a2, ...), axis=0)
(a1, a2, ...)：需要连接的数组。
axis：指定连接轴。
"""
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10]])
c = np.array([[11, 12]])

d = np.concatenate((a, b, c), axis=0)
print(d)
"""
数组堆叠
在 NumPy 中，以下方法可用于数组的堆叠：

stack(arrays，axis)：沿着新轴连接数组的序列。
column_stack()：将 1 维数组作为列堆叠到 2 维数组中。
hstack()：按水平方向堆叠数组。
vstack()：按垂直方向堆叠数组。
dstack()：按深度方向堆叠数组。
"""
# 这里以 stack(arrays，axis) 方法举例：
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.stack((a, b))
print(c)
"""
拆分
split 及与之相似的一系列方法主要是用于数组的拆分，列举如下：

split(ary，indices_or_sections，axis)：将数组拆分为多个子数组。
dsplit(ary，indices_or_sections)：按深度方向将数组拆分成多个子数组。
hsplit(ary，indices_or_sections)：按水平方向将数组拆分成多个子数组。
vsplit(ary，indices_or_sections)：按垂直方向将数组拆分成多个子数组。
"""
a = np.arange(10)
c = np.split(a, 5)
print(c)
a = np.arange(10).reshape(2, 5)
b = np.split(a, 2)
print(b)

