'''
@Author: ghost-guest
@Date: 2020-02-24 19:21:20
@LastEditTime: 2020-02-24 19:30:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyenv/numpy/np4.py
'''
import numpy as np


# 创建一个5*5的二维数组，边界值为1其余为0
a = np.ones((5,5))
print(a[1:-1])
print("-"*90)
print(a[:,1:-1])
print("="*90)

a[1:-1, 1:-1] = 0
print(a)
print("+_+"*90)
#52. 使用数字 0 将一个全为 1 的 5x5 二维数组包围
b = np.ones((5,5))
Z = np.pad(b, pad_width=1, mode='constant', constant_values=0)
print(Z)
# 53. 创建一个 5x5 的二维数组，并设置值 1, 2, 3, 4 落在其对角线下方
Z = np.diag(1+np.arange(4), k=-1)
print(Z)

# 54. 创建一个 10x10 的二维数组，并使得 1 和 0 沿对角线间隔放置
Z = np.zeros((10, 10), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)
# 55. 创建一个 0-10 的一维数组，并将 (1, 9] 之间的数全部反转成负数
Z = np.arange(11)
Z[(1 < Z) & (Z <= 9)] *= -1
print(Z)