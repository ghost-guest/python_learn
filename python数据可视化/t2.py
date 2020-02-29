#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


# 生成一个二维数组
y = np.random.standard_normal((20,2)).cumsum(axis=0)
print(y)
# y[:, 0] = y[:, 0]*100
plt.figure(figsize=(7, 4))
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 1], lw=1.5, label='2nd')
plt.plot(y, 'ro')
plt.grid(True)
# plt.legend 接受不同的位置参数。0表示“最佳位置”，也就是图例尽可能少地遮盖数据。
plt.legend(loc=0)
plt.title('a simple plot')
plt.xlabel('index')
plt.ylabel("value")
plt.axis('tight')
plt.show()