'''
@Author: your name
@Date: 2020-02-29 09:39:09
@LastEditTime: 2020-02-29 09:53:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyenv/numpy/np6.py
'''
import numpy as np

# 61. 创建一个长度为10的随机一维数组，并将其按升序排序：
a = np.random.random(10)
a.sort()
print(a)
#62. 创建一个 3x3 的二维数组，并将列按升序排序：
Z = np.array([[7, 4, 3], [3, 1, 2], [4, 2, 6]])
print("原始数组: \n", Z)

Z.sort(axis=0)
print(Z)
# 63. 创建一个长度为 5 的一维数组，并将其中最大值替换成 0：
Z = np.random.random(5)
print("原数组: ", Z)
Z[Z.argmax()] = 0
print(Z)
# 64. 打印每个 NumPy 标量类型的最小值和最大值：
for dtype in [np.int8, np.int32, np.int64]:
    print("The minimum value of {}: ".format(dtype), np.iinfo(dtype).min)
    print("The maximum value of {}: ".format(dtype), np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print("The minimum value of {}: ".format(dtype), np.finfo(dtype).min)
    print("The maximum value of {}: ".format(dtype), np.finfo(dtype).max)

# 65. 将 float32 转换为整型：
Z = np.arange(10, dtype=np.float32)
print(Z)

Z = Z.astype(np.int32, copy=False)
print(Z)

# 66. 将随机二维数组按照第 3 列从上到下进行升序排列：
Z = np.random.randint(0, 10, (5, 5))
print("排序前：\n", Z)

Z[Z[:, 2].argsort()]
print(Z)
# 67. 从随机一维数组中找出距离给定数值（0.5）最近的数：
Z = np.random.uniform(0, 1, 20)
print("随机数组: \n", Z)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]

print(m)

# 68. 将二维数组的前两行进行顺序交换：
A = np.arange(25).reshape(5, 5)
print(A)
A[[0, 1]] = A[[1, 0]]
print(A)
# 69. 找出随机一维数组中出现频率最高的值：
Z = np.random.randint(0, 10, 50)
print("随机一维数组:", Z)
a = np.bincount(Z).argmax()
print(a)
# 70. 找出给定一维数组中非 0 元素的位置索引：
Z = np.nonzero([1, 0, 2, 0, 1, 0, 4, 0])
print(Z)