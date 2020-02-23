'''
@Author: ghost-guest
@Date: 2020-02-23 16:22:07
@LastEditTime: 2020-02-23 16:43:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /pyenv/numpy/numpy2.py
'''
import numpy as np

# 数组的切片和索引
a = np.array([1,2,3,4,5])
print(a[0])
print(a[-1])
print(a[0:2])
print(a[:-1])
# 二维数组的切片和索引
b = np.array([(1,2,3),(4,5,6),(7,8,9)])
print(b)
print("="*80)
print(b[0])
print('-'*70)
print(b[-1])
# 取第二列
print("+"*80)
print(b[:,1])
print(b[1:3, :])
print("+++"*60)

c = np.random.random((3,2))
print(c)
print(c.shape)
print(c.reshape(2,3))
c.resize(2,3)
print(c)
# 展平数组
print(c.ravel())

# 垂直拼合数组
a = np.random.randint(10,size=(3,3))
b = np.random.randint(10,size=(3,3))
print(a)
print(b)

print(np.vstack((a, b)))
# 水平拼接
print(np.hstack((a, b)))

# 沿横轴分割数组
print(np.hsplit(a, 3))
#沿纵轴分割数组
print(np.vsplit(a, 3))


