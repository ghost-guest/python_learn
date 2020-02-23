'''
@Author: ghost_guest
@Date: 2020-02-23 10:47:18
@LastEditTime: 2020-02-23 16:21:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyenv/numpy/numpy1.py
'''
import numpy as np

# look numpy's version
print(np.__version__)

# create one  numpy with list
a = np.array([1,2,3])
print(a)

# create two-dimensional numpy 
b = np.array([[1,2,3], [4,5,6]])
print(b)

# create a zero of numpy
c = np.zeros([3,3])
print(c)
# create a one of numpy
d = np.ones([2,2])
print(d)

# create a Arithmetic sequence numpy 
e = np.arange(5)
print(e)
# create a two-dimensional arithmetic sequence numpy
f = np.arange(6).reshape(2,3)
print(f)

# 创建单位矩阵
g = np.eye(3)
print(g)
# 创建等间隔的一维数组
h = np.linspace(1,10,num=6)
print(h)

# 创建二维的随机整数数组
i = np.random.randint(5, size=(2,3))
print(i)


# 根据自定义的函数创建数组
k = np.fromfunction(lambda i, j:i+j, (3,3))
print(k)
# 一维数组的运算
l = np.array([10, 20, 30, 40 ,50])
j = np.arange(1, 6)
print("+"*50)
print(l)
print(j)

print(l+j)
print(l-j)
print(l*j)
print(l/j)
print("==="*50)
# 二维数组
m = np.array([[1,2], [3,4]])
n = np.array([[5,6], [7,8]])
print(m+n)
print(m-n)
print(m*n)
print(m/n)
print("-"*70)
print(np.dot(m,n))
#  数乘矩阵
print(2*m)
# 矩阵装置
print(m.T)
# 矩阵求逆转
print(np.linalg.inv(m))
# 三角函数
g = np.array([10,20,30,40,50,60])
print(np.sin(g))
# 以自然对数函数为底数的指数函数
print(np.exp(g))
# . 数组的方根的运算（开平方)
print(np.sqrt(g))
# 数组的方根的运算
print(np.power(g, 2))
