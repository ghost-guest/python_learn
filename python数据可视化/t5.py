#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-01 14:21:19
@LastEditors: ghost-guest
@LastEditTime: 2020-03-01 14:29:36
@FilePath: /pyenv/python数据可视化/t5.py
@Description: 散点图
'''
import numpy as np
import matplotlib.pyplot as plt


y = np.random.standard_normal((100, 2))
c = np.random.randint(0, 10, len(y))
print(c)
plt.figure(figsize=(7, 5))
# plt.plot(y[:, 0],y[:, 1], 'ro')
plt.scatter(y[:, 0], y[:,1], c=c,  marker='o')
plt.colorbar()
plt.grid(True)
plt.xlabel("1st")
plt.ylabel("2nd")
plt.title(" scatter plot")
plt.show()


