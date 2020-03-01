#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-01 14:37:56
@LastEditors: ghost-guest
@LastEditTime: 2020-03-01 14:41:52
@FilePath: /pyenv/python数据可视化/t7.py
@Description: 箱型图
'''
import numpy as np
import matplotlib.pyplot as plt

y = np.random.standard_normal((1000, 2))
fix, ax = plt.subplots(figsize=(7, 4))
plt.boxplot(y)
plt.grid(True)
plt.setp(ax, xticklabels=['1st', '2nd'])
plt.xlabel('data set')
plt.ylabel("value")
plt.title('boxplot')
plt.show()