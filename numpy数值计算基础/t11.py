#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-04 18:58:56
@LastEditors: ghost-guest
@LastEditTime: 2020-03-04 19:01:58
@FilePath: /pyenv/numpy数值计算基础/t11.py
@Description: 
'''
import numpy as np

"""
算术运算
当然，NumPy 也提供了一些用于算术运算的方法，使用起来会比 Python 提供的运算符灵活一些，主要是可以直接针对数组。

numpy.add(x1, x2)：对应元素相加。
numpy.reciprocal(x)：求倒数 1/x。
numpy.negative(x)：求对应负数。
numpy.multiply(x1, x2)：求解乘法。
numpy.divide(x1, x2)：相除 x1/x2。
numpy.power(x1, x2)：类似于 x1^x2。
numpy.subtract(x1, x2)：减法。
numpy.fmod(x1, x2)：返回除法的元素余项。
numpy.mod(x1, x2)：返回余项。
numpy.modf(x1)：返回数组的小数和整数部分。
numpy.remainder(x1, x2)：返回除法余数。

"""

a = np.random.randint(0,10,5)
b = np.random.randint(0,10,5)
print(a, b)
c = np.add(a, b)
print(c)

print(np.negative(a))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.power(a,b))
