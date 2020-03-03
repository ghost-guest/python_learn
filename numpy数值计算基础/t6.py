#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-03 18:35:15
@LastEditors: ghost-guest
@LastEditTime: 2020-03-03 18:44:55
@FilePath: /pyenv/numpy数值计算基础/t6.py
@Description: 
'''
import numpy as np

"""
删除
首先是 delete 删除：

delete(arr，obj，axis)：沿特定轴删除数组中的子数组。
"""
a = np.arange(10).reshape(5,2)
print(a)
c = np.delete(a, 2, 0)
print(c, c.shape)

"""
数组插入
再看一看 insert插入，用法和 delete 很相似，只是需要在第三个参数位置设置需要插入的数组对象：

insert(arr，obj，values，axis)：依据索引在特定轴之前插入值。
"""
a = np.arange(10).reshape(2,5)
b = np.arange(5)
print(a)
c = np.insert(a, 2, b, 0)
print(c)
"""
append 的用法也非常简单。只需要设置好需要附加的值和轴位置就好了。它其实相当于只能在末尾插入的 insert，所以少了一个指定索引的参数。

append(arr，values，axis)：将值附加到数组的末尾，并返回 1 维数组。
"""
a = np.arange(12).reshape(3,4)
print(a)
b = np.arange(4)
c = np.append(a, b)
print(c)

"""
resize 就很好理解了，直接举例子吧：

resize(a，new_shape)：对数组尺寸进行重新设定。
"""
a = np.arange(10)
print(a)
b = np.resize(a,(2,5))
print(b)


"""
翻转数组
在 NumPy 中，我们还可以对数组进行翻转操作：

fliplr(m)：左右翻转数组。
flipud(m)：上下翻转数组。
"""

a = np.arange(16).reshape(4, 4)
print(np.fliplr(a))
print(np.flipud(a))



