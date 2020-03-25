#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月25日 
# @Author  : ghost-guest
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# 说明： 
import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4, 5, 6, 9, 7, 8, 1, 2, 3, 4, 5, 6, 7],
         [13, 14, 15, 16, 17, 18, 19, 10, 11, 12, 13, 14, 15, 16, 18, 13])
plt.show()

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# 在指定的间隔内返回均匀间隔的数字。
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.show()

plt.bar([1, 2, 3], [1, 2, 3])
plt.show()

x = np.random.ranf(1000)
# print(x)
y = np.random.ranf(1000)
plt.scatter(x, y)
plt.show()
