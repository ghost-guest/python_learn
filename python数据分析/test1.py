#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月23日 
# @Author  : ghost-guest
# @Site    : 
# @File    : test1.py
# @Software: PyCharm
# 说明： 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)
# 曲线图
plt.plot(x, y)
plt.show()
# 柱状图
plt.bar([1, 2, 3], [1, 2, 3])
plt.show()
# 散点图
x = np.random.ranf(1000)
y = np.random.ranf(1000)
plt.scatter(x, y)
plt.show()
plt.pie([1, 2, 3, 4, 5])
plt.show()
# 量场图
x, y = np.mgrid[0:10, 0:10]
plt.quiver(x, y)
plt.show()
# 等高线图
# 生成网格矩阵
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
x, y = np.meshgrid(x, y)
# 等高线计算公式
Z = (1 - x / 2 + x ** 3 + y ** 4) * np.exp(-x ** 2 - y ** 2)
plt.contourf(x, y, Z)
plt.show()




