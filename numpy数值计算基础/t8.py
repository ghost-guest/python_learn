#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-03 18:54:46
@LastEditors: ghost-guest
@LastEditTime: 2020-03-03 18:56:33
@FilePath: /pyenv/numpy数值计算基础/t8.py
@Description: 
'''
import numpy as np

'''
三角函数
首先, 看一看 NumPy 提供的三角函数功能。这些方法有：

numpy.sin(x)：三角正弦。
numpy.cos(x)：三角余弦。
numpy.tan(x)：三角正切。
numpy.arcsin(x)：三角反正弦。
numpy.arccos(x)：三角反余弦。
numpy.arctan(x)：三角反正切。
numpy.hypot(x1,x2)：直角三角形求斜边。
numpy.degrees(x)：弧度转换为度。
numpy.radians(x)：度转换为弧度。
numpy.deg2rad(x)：度转换为弧度。
numpy.rad2deg(x)：弧度转换为度。
'''
a = np.rad2deg(np.pi)  # PI 值弧度表示
print(a)

"""
双曲函数
在数学中，双曲函数是一类与常见的三角函数类似的函数。双曲函数经常出现于某些重要的线性微分方程的解中，使用 NumPy 计算它们的方法为：

numpy.sinh(x)：双曲正弦。
numpy.cosh(x)：双曲余弦。
numpy.tanh(x)：双曲正切。
numpy.arcsinh(x)：反双曲正弦。
numpy.arccosh(x)：反双曲余弦。
numpy.arctanh(x)：反双曲正切。
"""
