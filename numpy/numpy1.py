'''
@Author: ghost_guest
@Date: 2020-02-23 10:47:18
@LastEditTime: 2020-02-23 11:11:14
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
