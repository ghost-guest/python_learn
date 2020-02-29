'''
@Author: your name
@Date: 2020-02-29 11:18:08
@LastEditTime: 2020-02-29 11:33:58
@LastEditors: ghost-guest
@Description: In User Settings Edit
@FilePath: /pyenv/numpy/np8.py
'''
import numpy as np

# 81. 统计随机数组中的各元素的数量：
Z = np.random.randint(0, 100, 25).reshape(5, 5)
print(Z)
a = np.unique(Z, return_counts=True) 
print(a)
# 82. 将数组中各元素按指定分类转换为文本值：
# 指定类别如下
# 1 → 汽车
# 2 → 公交车
# 3 → 火车

Z = np.random.randint(1, 4, 10)
print(Z)

label_map = {1: "汽车", 2: "公交车", 3: "火车"}

a = [label_map[x] for x in Z]
print(a)

# 83. 将多个 1 维数组拼合为单个 Ndarray：
Z1 = np.arange(3)
Z2 = np.arange(3, 7)
Z3 = np.arange(7, 10)

Z = np.array([Z1, Z2, Z3])
print(Z)

a = np.concatenate(Z)
print(a)
# 84. 打印各元素在数组中升序排列的索引：
a = np.random.randint(100, size=10)
print('Array: ', a)

a = a.argsort()
print(a)
# 85. 得到二维随机数组各行的最大值：
Z = np.random.randint(1, 100, [5, 5])
print(Z)

c = np.amax(Z, axis=1)
print(c)
# 86. 得到二维随机数组各行的最小值（区别上面的方法）：
Z = np.random.randint(1, 100, [5, 5])
print(Z)

a = np.apply_along_axis(np.min, arr=Z, axis=1)
print(a)
# 87. 计算两个数组之间的欧氏距离：
a = np.array([1, 2])
b = np.array([7, 8])

# 数学计算方法
print(np.sqrt(np.power((8-2), 2) + np.power((7-1), 2)))
# NumPy 计算
c = np.linalg.norm(b-a)
print(c)

# 88. 打印复数的实部和虚部：
a = np.array([1 + 2j, 3 + 4j, 5 + 6j])

print("实部：", a.real)
print("虚部：", a.imag)


# 89. 求解给出矩阵的逆矩阵并验证：
matrix = np.array([[1., 2.], [3., 4.]])
inverse_matrix = np.linalg.inv(matrix)

# 验证原矩阵和逆矩阵的点积是否为单位矩阵
assert np.allclose(np.dot(matrix, inverse_matrix), np.eye(2))
print(inverse_matrix)

# 90. 使用 Z-Score 标准化算法对数据进行标准化处理：
# 根据公式定义函数
def zscore(x, axis=None):
    xmean = x.mean(axis=axis, keepdims=True)
    xstd = np.std(x, axis=axis, keepdims=True)
    zscore = (x-xmean)/xstd
    return zscore


# 生成随机数据
Z = np.random.randint(10, size=(5, 5))
print(Z)

a = zscore(Z)
print(a)