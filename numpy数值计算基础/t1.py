#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-02 20:00:12
@LastEditors: ghost-guest
@LastEditTime: 2020-03-02 20:27:39
@FilePath: /pyenv/numpy数值计算基础/t1.py
@Description: 
'''
import numpy as np


# 指定一维数组，类型是float
a = np.array([1,2,3,4,5], dtype=np.float64)
print(a)
print(a.dtype)
# 将a的数组类型转化为int
a = a.astype(int)
print(a.dtype)

# 二维数组的创建

a = np.array([(1,2,3),(2,3,4)])
print(a)


# 通过arange创建一个有规律的数组
a = np.arange(1, 5, step=0.5)
print(a)
# 通过linspace创建一个有规律的数组
# a = np.linspace(1, 10, 10, endpoint=True)
a = np.linspace(1, 10, 10, endpoint=False)

print(a)

# 创建全为1的数组
a = np.ones((2,3))
print(a)
# 创建全为0的数组
a = np.zeros((1,3))
print(a)

# 创建一个二维数组，其特点是k 对角线上的值为 1，其余值全部为0
# numpy.eye(N, M=None, k=0, dtype=<type 'float'>)
# N：输出数组的行数。
# M：输出数组的列数。
# k：对角线索引：0（默认）是指主对角线，正值是指上对角线，负值是指下对角线。
a = np.eye(5,5,1)
print(a)
a = np.eye(5,5,0)
print(a)
a = np.eye(5,5,-1)
print(a)

"""
我们还可以从已知数据文件、函数中创建 ndarray。NumPy 提供了下面 5 个方法：

frombuffer（buffer）：将缓冲区转换为 1 维数组。
fromfile（file，dtype，count，sep）：从文本或二进制文件中构建多维数组。
fromfunction（function，shape）：通过函数返回值来创建多维数组。
fromiter（iterable，dtype，count）：从可迭代对象创建 1 维数组。
fromstring（string，dtype，count，sep）：从字符串中创建 1 维数组。
"""
a = np.fromfunction(lambda a, b: a * b, (5, 4))

print(a)


# 创建一个二维数组，使用numpy的T属性
a = np.array([[1,2,3],[1,2,3]])
print(a)
print(a.T) # 数组的行列翻转
print(a.dtype) # 数组的类型
print(a.real) # 数组的实部
print(a.imag) # 数组的虚部
print(a.size) # 数组包含的总元素数
print(a.itemsize) # 数组元素的字节
print(a.nbytes) # 数组元素的总字节
print(a.ndim) # 数组的维度
print(a.shape) # 数组的形状
print(a.strides) # 用来遍历数组时，输出每个维度中步进的字节数组







