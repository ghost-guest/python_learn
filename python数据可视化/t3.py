#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-02-29 15:48:38
@LastEditors: ghost-guest
@LastEditTime: 2020-02-29 16:05:52
@FilePath: /pyenv/python数据可视化/t3.py
@Description: 
'''


import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(2000)
y = np.random.standard_normal((20,2)).cumsum(axis=0)
print(y)
fig, ax1 = plt.subplots()
plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.grid(True)
plt.axis('tight')
plt.legend(loc=8)
plt.xlabel('index')
plt.ylabel('value 1st')
plt.title('a simple plot')
ax2 = ax1.twinx()
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.ylabel('value 2nd')
plt.show()


