'''
@Author: ghost-guest
@Date: 2020-02-24 19:30:22
@LastEditTime: 2020-02-24 19:36:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyenv/numpy/np5.py
'''
import numpy as np

# 找出两个一维数组中相同的元素
Z1 = np.random.randint(0, 10, 10)
Z2 = np.random.randint(0, 10, 10)
print("Z1:", Z1)
print("Z2:", Z2)
print(np.intersect1d(Z1, Z2))

print("__"*80)
# 57. 使用 NumPy 打印昨天、今天、明天的日期
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("yesterday: ", yesterday)
print("today: ", today)
print("tomorrow: ", tomorrow)
print("-"*90)
#  使用五种不同的方法去提取一个随机数组的整数部分：
Z = np.random.uniform(0, 10, 10)
print("原始值: ", Z)

print("方法 1: ", Z - Z % 1)
print("方法 2: ", np.floor(Z))
print("方法 3: ", np.ceil(Z)-1)
print("方法 4: ", Z.astype(int))
print("方法 5: ", np.trunc(Z))
print("="*90)
# 59. 创建一个 5x5 的矩阵，其中每行的数值范围从 1 到 5：
Z = np.zeros((5, 5))
Z += np.arange(1, 6)
print(Z)
print("+"*90)
# 60. 创建一个长度为 5 的等间隔一维数组，其值域范围从 0 到 1，但是不包括 0 和 1：
Z = np.linspace(0, 1, 6, endpoint=False)[1:]
print(Z)