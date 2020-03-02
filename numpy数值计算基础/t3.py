#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-02 20:32:46
@LastEditors: ghost-guest
@LastEditTime: 2020-03-02 20:36:21
@FilePath: /pyenv/numpy数值计算基础/t3.py
@Description: 
'''
import numpy as np

# 重设形状
# numpy.reshape(a, newshape)
# 其中，a 表示原数组，newshape 用于指定新的形状(整数或者元组)。
a = np.arange(10)
print(a)
print(a.shape)
a = a.reshape(5,2)
print(a)
print(a.shape)
print(np.reshape([1,2,3,4,5,6], (2,3)))
