'''
@Author: your name
@Date: 2020-02-29 09:53:57
@LastEditTime: 2020-02-29 11:17:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyenv/numpy/np7.py
'''
import numpy as np

# 71. 对于给定的 5x5 二维数组，在其内部随机放置 p 个值为 1 的数：
p = 3

Z = np.zeros((5, 5))
np.put(Z, np.random.choice(range(5*5), p, replace=False), 1)

print(Z)


# 72. 对于随机的 3x3 二维数组，减去数组每一行的平均值：
X = np.random.rand(3, 3)
print(X)

Y = X - X.mean(axis=1, keepdims=True)
print(Y)

# 73. 获得二维数组点积结果的对角线数组：
A = np.random.uniform(0, 1, (3, 3))
B = np.random.uniform(0, 1, (3, 3))

print(np.dot(A, B))

# 较慢的方法
np.diag(np.dot(A, B))
np.sum(A * B.T, axis=1)  # 较快的方法
np.einsum("ij, ji->i", A, B)  # 更快的方法
# 74. 找到随机一维数组中前 p 个最大值：
Z = np.random.randint(1, 100, 100)
print(Z)

p = 5

a = Z[np.argsort(Z)[-p:]]
print(a)
# 75. 计算随机一维数组中每个元素的 4 次方数值：
x = np.random.randint(2, 5, 5)
print(x)

a = np.power(x, 4)
print(a)
# 76. 对于二维随机数组中各元素，保留其 2 位小数：
Z = np.random.random((5, 5))
print(Z)

np.set_printoptions(precision=2)
print(Z)
# 77. 使用科学记数法输出 NumPy 数组：
Z = np.random.random([5, 5])
print(Z)

print(Z/1e3)

# 78. 使用 NumPy 找出百分位数（25%，50%，75%）：
a = np.arange(15)
print(a)

c = np.percentile(a, q=[25, 50, 75])
print(c)
# 79. 找出数组中缺失值的总数及所在位置：
# 生成含缺失值的 2 维数组
Z = np.random.rand(10, 10)
Z[np.random.randint(10, size=5), np.random.randint(10, size=5)] = np.nan
print(Z)
print("缺失值总数: \n", np.isnan(Z).sum())
print("缺失值索引: \n", np.where(np.isnan(Z)))
# 80. 从随机数组中删除包含缺失值的行：
b = Z[np.sum(np.isnan(Z), axis=1) == 0]
print(b)