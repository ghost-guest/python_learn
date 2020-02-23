'''
@Author: ghost-guest
@Date: 2020-02-23 16:45:49
@LastEditTime: 2020-02-23 16:52:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyenv/numpy/numpy3.py
'''
import numpy as np

a = np.array([[1,3,2],[6,3,8],[4,7,2]])
# 返回每列的最大值
print(np.max(a, axis=0))
# 返回每行最小值
print(np.min(a, axis=1))
# 返回每列最大值索引
print(np.argmax(a, axis=0))
# 返回每行最小值索引
print(np.argmin(a, axis=1))
# 统计数组各列的中位数
print(np.median(a, axis=0))
# 统计数组各行的算术平均值
print(np.mean(a, axis=1))
