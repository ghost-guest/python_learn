#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-02-29 16:39:10
@LastEditors: ghost-guest
@LastEditTime: 2020-02-29 16:48:52
@FilePath: /pyenv/python数据可视化/t4.py
@Description: 
'''
import numpy as np
import matplotlib.pyplot as plt


# 生成二维的数组
y = np.random.standard_normal((20,2)).cumsum(axis=0)

print(y)
plt.figure(figsize=(7, 5))
# 两个单独子图的情况
plt.subplot(211)

plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.grid(True)
plt.title('a simple plot')

plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')

plt.subplot(212)
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.grid(True)

plt.xlabel("index")
plt.legend(loc=0)
plt.axis('tight')
plt.ylabel('value')
# plt.show()
plt.figure(figsize=(9, 4))

plt.subplot(121)
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('1st Data Set')

plt.subplot(122)
plt.bar(np.arange(len(y)), y[:, 1], width=0.5, color='g', label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.title('2nd Data Set')
plt.show()