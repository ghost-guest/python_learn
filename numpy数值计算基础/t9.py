#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-03 18:56:56
@LastEditors: ghost-guest
@LastEditTime: 2020-03-03 18:58:30
@FilePath: /pyenv/numpy数值计算基础/t9.py
@Description: 
'''
import numpy as np

'''
数值修约
数值修约, 又称数字修约, 是指在进行具体的数字运算前, 按照一定的规则确定一致的位数, 然后舍去某些数字后面多余的尾数的过程。比如, 我们常听到的「4 舍 5 入」就属于数值修约中的一种。

numpy.around(a)：平均到给定的小数位数。
numpy.round_(a)：将数组舍入到给定的小数位数。
numpy.rint(x)：修约到最接近的整数。
numpy.fix(x, y)：向 0 舍入到最接近的整数。
numpy.floor(x)：返回输入的底部(标量 x 的底部是最大的整数 i)。
numpy.ceil(x)：返回输入的上限(标量 x 的底部是最小的整数 i).
numpy.trunc(x)：返回输入的截断值。
'''
a = np.random.randn(5)  # 生成 5 个随机数
print(a)  # 输出 a 的值

print(np.around(a))
print(np.rint(a))
print(np.fix(a))
