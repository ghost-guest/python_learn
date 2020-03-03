#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-03 18:47:30
@LastEditors: ghost-guest
@LastEditTime: 2020-03-03 18:54:23
@FilePath: /pyenv/numpy数值计算基础/t7.py
@Description: 
'''
import numpy as np

# NumPy 的随机数功能非常强大，主要由 numpy.random 模块完成。
# numpy.random.rand(d0, d1, ..., dn) 方法的作用为：指定一个数组，
# 并使用 [0, 1) 区间随机数据填充，这些数据均匀分布

a = np.random.rand(2,5)
print(a)

# numpy.random.randn(d0, d1, ..., dn) 与 numpy.random.rand(d0, d1, ..., dn) 
# 的区别在于，前者是从标准正态分布中返回一个或多个样本值。
b = np.random.randn(1,10)
print(b)
"""
randint(low, high, size, dtype) 
方法将会生成 [low, high) 的随机整数。注意这是一个半开半闭区间。
"""
c = np.random.randint(1,10,5)
print(c)
# random_sample(size) 方法将会在 [0, 1) 区间内生成指定 size 的随机浮点数。
d = np.random.random_sample([10])
print(d)
# choice(a, size, replace, p) 方法将会给定的数组里随机抽取几个值，该方法类似于随机抽样。
f = np.random.choice(10,5)
print(f)

"""
概率密度分布
除了上面介绍的 6 种随机数生成方法，NumPy 还提供了大量的满足特定概率密度分布的样本生成方法。它们的使用方法和上面非常相似，这里就不再一一介绍了。列举如下：

numpy.random.beta(a，b，size)：从 Beta 分布中生成随机数。
numpy.random.binomial(n, p, size)：从二项分布中生成随机数。
numpy.random.chisquare(df，size)：从卡方分布中生成随机数。
numpy.random.dirichlet(alpha，size)：从 Dirichlet 分布中生成随机数。
numpy.random.exponential(scale，size)：从指数分布中生成随机数。
numpy.random.f(dfnum，dfden，size)：从 F 分布中生成随机数。
numpy.random.gamma(shape，scale，size)：从 Gamma 分布中生成随机数。
numpy.random.geometric(p，size)：从几何分布中生成随机数。
numpy.random.gumbel(loc，scale，size)：从 Gumbel 分布中生成随机数。
numpy.random.hypergeometric(ngood, nbad, nsample, size)：从超几何分布中生成随机数。
numpy.random.laplace(loc，scale，size)：从拉普拉斯双指数分布中生成随机数。
numpy.random.logistic(loc，scale，size)：从逻辑分布中生成随机数。
numpy.random.lognormal(mean，sigma，size)：从对数正态分布中生成随机数。
numpy.random.logseries(p，size)：从对数系列分布中生成随机数。
numpy.random.multinomial(n，pvals，size)：从多项分布中生成随机数。
numpy.random.multivariate_normal(mean, cov, size)：从多变量正态分布绘制随机样本。
numpy.random.negative_binomial(n, p, size)：从负二项分布中生成随机数。
numpy.random.noncentral_chisquare(df，nonc，size)：从非中心卡方分布中生成随机数。
numpy.random.noncentral_f(dfnum, dfden, nonc, size)：从非中心 F 分布中抽取样本。
numpy.random.normal(loc，scale，size)：从正态分布绘制随机样本。
numpy.random.pareto(a，size)：从具有指定形状的 Pareto II 或 Lomax 分布中生成随机数。
numpy.random.poisson(lam，size)：从泊松分布中生成随机数。
numpy.random.power(a，size)：从具有正指数 a-1 的功率分布中在 0，1 中生成随机数。
numpy.random.rayleigh(scale，size)：从瑞利分布中生成随机数。
numpy.random.standard_cauchy(size)：从标准 Cauchy 分布中生成随机数。
numpy.random.standard_exponential(size)：从标准指数分布中生成随机数。
numpy.random.standard_gamma(shape，size)：从标准 Gamma 分布中生成随机数。
numpy.random.standard_normal(size)：从标准正态分布中生成随机数。
numpy.random.standard_t(df，size)：从具有 df 自由度的标准学生 t 分布中生成随机数。
numpy.random.triangular(left，mode，right，size)：从三角分布中生成随机数。
numpy.random.uniform(low，high，size)：从均匀分布中生成随机数。
numpy.random.vonmises(mu，kappa，size)：从 von Mises 分布中生成随机数。
numpy.random.wald(mean，scale，size)：从 Wald 或反高斯分布中生成随机数。
numpy.random.weibull(a，size)：从威布尔分布中生成随机数。
numpy.random.zipf(a，size)：从 Zipf 分布中生成随机数。

"""
