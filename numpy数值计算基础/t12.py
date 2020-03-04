#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-04 19:03:07
@LastEditors: ghost-guest
@LastEditTime: 2020-03-04 19:05:19
@FilePath: /pyenv/numpy数值计算基础/t12.py
@Description: 
'''
import numpy as np

"""
矩阵和向量积
求解向量、矩阵、张量的点积等同样是 NumPy 非常强大的地方。

numpy.dot(a, b)：求解两个数组的点积。
numpy.vdot(a, b)：求解两个向量的点积。
numpy.inner(a, b)：求解两个数组的内积。
numpy.outer(a, b)：求解两个向量的外积。
numpy.matmul(a, b)：求解两个数组的矩阵乘积。
numpy.tensordot(a, b)：求解张量点积。
numpy.kron(a, b)：计算 Kronecker 乘积。
除了上面这些归好类别的方法，NumPy 中还有一些用于数学运算的方法，归纳如下：

numpy.angle(z, deg)：返回复参数的角度。
numpy.real(val)：返回数组元素的实部。
numpy.imag(val)：返回数组元素的虚部。
numpy.conj(x)：按元素方式返回共轭复数。
numpy.convolve(a, v, mode)：返回线性卷积。
numpy.sqrt(x)：平方根。
numpy.cbrt(x)：立方根。
numpy.square(x)：平方。
numpy.absolute(x)：绝对值, 可求解复数。
numpy.fabs(x)：绝对值。
numpy.sign(x)：符号函数。
numpy.maximum(x1, x2)：最大值。
numpy.minimum(x1, x2)：最小值。
numpy.nan_to_num(x)：用 0 替换 NaN。
numpy.interp(x, xp, fp, left, right, period)：线性插值。
"""
a = np.matrix([[1, 2, 3], [4, 5, 6]])
b = np.matrix([[2, 2], [3, 3], [4, 4]])
print(a,b)
c = np.matmul(a, b)
print(c)
"""
代数运算
上面，我们分为 8 个类别，介绍了 NumPy 中常用到的数学函数。这些方法让复杂的计算过程表达更为简单。除此之外，NumPy 中还包含一些代数运算的方法，尤其是涉及到矩阵的计算方法，求解特征值、特征向量、逆矩阵等，非常方便。

numpy.linalg.cholesky(a)：Cholesky 分解。
numpy.linalg.qr(a ,mode)：计算矩阵的 QR 因式分解。
numpy.linalg.svd(a ,full_matrices,compute_uv)：奇异值分解。
numpy.linalg.eig(a)：计算正方形数组的特征值和右特征向量。
numpy.linalg.eigh(a, UPLO)：返回 Hermitian 或对称矩阵的特征值和特征向量。
numpy.linalg.eigvals(a)：计算矩阵的特征值。
numpy.linalg.eigvalsh(a, UPLO)：计算 Hermitian 或真实对称矩阵的特征值。
numpy.linalg.norm(x ,ord,axis,keepdims)：计算矩阵或向量范数。
numpy.linalg.cond(x ,p)：计算矩阵的条件数。
numpy.linalg.det(a)：计算数组的行列式。
numpy.linalg.matrix_rank(M ,tol)：使用奇异值分解方法返回秩。
numpy.linalg.slogdet(a)：计算数组的行列式的符号和自然对数。
numpy.trace(a ,offset,axis1,axis2,dtype,out)：沿数组的对角线返回总和。
numpy.linalg.solve(a, b)：求解线性矩阵方程或线性标量方程组。
numpy.linalg.tensorsolve(a, b ,axes)：为 x 解出张量方程 a x = b
numpy.linalg.lstsq(a, b ,rcond)：将最小二乘解返回到线性矩阵方程。
numpy.linalg.inv(a)：计算逆矩阵。
numpy.linalg.pinv(a ,rcond)：计算矩阵的（Moore-Penrose）伪逆。
numpy.linalg.tensorinv(a ,ind)：计算 N 维数组的逆。
"""