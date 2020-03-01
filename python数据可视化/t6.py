#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-01 14:30:27
@LastEditors: ghost-guest
@LastEditTime: 2020-03-01 14:36:50
@FilePath: /pyenv/python数据可视化/t6.py
@Description: 直方图
'''
import numpy as np
import matplotlib.pyplot as plt


y = np.random.standard_normal((1000, 2))
print(y)
plt.figure(figsize=(7, 5))
# plt.hist(y, label=['1st', '2nd'], bins=25)
# 两个数据集的数据在直方图中堆叠
plt.hist(y, label=['1st', '2nd'], color=['b', 'g'], stacked=True, bins=20)
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('histogram')
plt.show()
