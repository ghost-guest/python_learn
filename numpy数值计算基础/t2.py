#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-02 20:28:58
@LastEditors: ghost-guest
@LastEditTime: 2020-03-02 20:30:55
@FilePath: /pyenv/numpy数值计算基础/t2.py
@Description: 
'''
import numpy as np

one = np.array([7, 2, 9, 10])
two = np.array([[5.2, 3.0, 4.5],
                [9.1, 0.1, 0.3]])
three = np.array([[[1, 1], [1, 1], [1, 1]],
                  [[1, 1], [1, 1], [1, 1]],
                  [[1, 1], [1, 1], [1, 1]],
                  [[1, 1], [1, 1], [1, 1]]])

print(one)
print(one.shape)
print(two)
print(two.shape)
print(three)
print(three.shape)
