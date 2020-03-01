#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-01 14:48:58
@LastEditors: ghost-guest
@LastEditTime: 2020-03-01 15:09:00
@FilePath: /pyenv/python数据可视化/t9.py
@Description: 3D 绘图
'''
import numpy as np
import matplotlib.pyplot as plt
# import mpl_toolkits
# import importlib
# importlib.import_module('mpl_toolkits').__path__
from mpl_toolkits.mplot3d import Axes3D

# 这为我们提供了一个2维坐标系。
# 我们可以使用 NumPy 的 meshgrid函数，根据两个 1 维 ndarray 对象生成这样的坐标系
strike = np.linspace(50, 150, 24)
ttm = np.linspace(0.5, 2.5, 24)
strike, ttm = np.meshgrid(strike, ttm)
# 现在，根据新的 ndarray 对象，我们通过简单的比例调整二次函数生成模拟的隐含波动率：
iv = (strike - 100) ** 2 / (100 * strike) / ttm


fig = plt.figure(figsize=(9,6))
ax = fig.gca(projection='3d')

surf = ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2, cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True)

ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')

fig.colorbar(surf, shrink=0.5, aspect=5)

# 和2维图表一样，线样式可以由单个点或者下例中的单个三角形表示。
# 下图用相同的数据绘制3D散点图，但是现在用 view_init 函数设置不同的视角
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(30, 60)

ax.scatter(strike, ttm, iv, zdir='z', s=25, c='b', marker='^')

ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
plt.show()