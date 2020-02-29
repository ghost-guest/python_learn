'''
@Author: ghost-guest
@Date: 2020-02-29 11:35:06
@LastEditors: ghost-guest
@LastEditTime: 2020-02-29 11:54:28
@FilePath: /pyenv/numpy/np9.py
'''
import numpy as np

# 91. 使用 Min-Max 标准化算法对数据进行标准化处理：
# 根据公式定义函数
def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)
    return result


# 生成随机数据
Z = np.random.randint(10, size=(5, 5))
print(Z)

a = min_max(Z)
print(a)


# 92. 使用 L2 范数对数据进行标准化处理：
# 根据公式定义函数
def l2_normalize(v, axis=-1, order=2):
    l2 = np.linalg.norm(v, ord=order, axis=axis, keepdims=True)
    l2[l2 == 0] = 1
    return v/l2

# 生成随机数据
Z = np.random.randint(10, size=(5, 5))
print(Z)

a = l2_normalize(Z)
print(a)


# 93. 使用 NumPy 计算变量直接的相关性系数：
Z = np.array([
    [1, 2, 1, 9, 10, 3, 2, 6, 7],  # 特征 A
    [2, 1, 8, 3, 7, 5, 10, 7, 2],  # 特征 B
    [2, 1, 1, 8, 9, 4, 3, 5, 7]])  # 特征 C

c = np.corrcoef(Z)
print("+"*69)
print(c)

# 94. 使用 NumPy 计算矩阵的特征值和特征向量：
M = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
w, v = np.linalg.eig(M)
# w 对应特征值，v 对应特征向量
print(w, v)
# 95. 使用 NumPy 计算 Ndarray 两相邻元素差值：
Z = np.random.randint(1, 10, 10)
print(Z)

# 计算 Z 两相邻元素差值
print(np.diff(Z, n=1))
# 重复计算 2 次
print(np.diff(Z, n=2))
# 重复计算 3 次
print(np.diff(Z, n=3))


# 96. 使用 NumPy 将 Ndarray 相邻元素依次累加：
Z = np.random.randint(1, 10, 10)
print(Z)

"""
[第一个元素, 第一个元素 + 第二个元素, 第一个元素 + 第二个元素 + 第三个元素, ...]
"""
a = np.cumsum(Z)
print(a)
# 97. 使用 NumPy 按列连接两个数组：
M1 = np.array([1, 2, 3])
M2 = np.array([4, 5, 6])

a = np.c_[M1, M2]
print(a)
# 98. 使用 NumPy 按行连接两个数组：
M1 = np.array([1, 2, 3])
M2 = np.array([4, 5, 6])

a = np.r_[M1, M2]
print(a)
# 99. 使用 NumPy 打印九九乘法表：
a = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (9, 9))
print(a)
# 100. 使用 NumPy 将实验楼 LOGO 转换为 Ndarray 数组：
from io import BytesIO
from PIL import Image
import PIL
import requests

# 通过链接下载图像
URL = 'https://static.shiyanlou.com/img/logo-black.png'
response = requests.get(URL)

# 将内容读取为图像
I = Image.open(BytesIO(response.content))
# 将图像转换为 Ndarray
shiyanlou = np.asarray(I)
print(shiyanlou)
# 将转换后的 Ndarray 重新绘制成图像
from matplotlib import pyplot as plt
# %matplotlib inline
# get_ipython().run_line_magic('matplotlib', 'inline')
print("a"*70)
plt.imshow(shiyanlou)
plt.show()