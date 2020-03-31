#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月27日 
# @Author  : ghost-guest
# @Site    : 
# @File    : t2.py
# @Software: PyCharm
# 说明： 
import scipy
from scipy import constants
import numpy as np
from scipy import linalg

print(constants.pi)
print(constants.golden)
print(constants.c)
print(constants.speed_of_light)
print(constants.h)
print(constants.Planck)

U, s, Vh = linalg.svd(np.random.randn(5, 4))
print(U)
print(s)
print(Vh)


