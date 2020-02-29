#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

a = np.random.seed(1000)
print(a)
y = np.random.standard_normal(20)
print(y)
x = range(len(y))
print(x)
# 定义图片的大小，宽和高
plt.figure(figsize=(7, 4))
# 修改连续线条和离散点
plt.plot(y.cumsum(), 'b', lw=1.5)
plt.plot(y.cumsum(), 'ro')
plt.grid(True) # 添加网格线
plt.axis('tight') #紧凑坐标轴
# 可以使用 plt.xlim 和 plt.ylim 设置每个坐标轴的最小值和最大值。
plt.xlim(-1, 20)
plt.ylim(np.min(y.cumsum())-1,np.max(y.cumsum())+1)
# 添加标题和坐标标签
plt.title('a simple plot')
plt.xlabel('index')
plt.ylabel('value')
plt.show()

