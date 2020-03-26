#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月26日 
# @Author  : ghost-guest
# @Site    : 
# @File    : t1.py
# @Software: PyCharm
# 说明：
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
y_bar = [3, 4, 6, 8, 9, 10, 9, 11, 7, 8]
y_line = [2, 3, 5, 7, 8, 9, 8, 10, 6, 7]

plt.bar(x, y_bar)
plt.plot(x, y_line, '-o', color='y')
plt.show()


sns.set()  # 声明使用 Seaborn 样式

plt.bar(x, y_bar)
plt.plot(x, y_line, '-o', color='y')
plt.show()
iris = sns.load_dataset("iris")
iris.head()
sns.relplot(x="sepal_length", y="sepal_width", data=iris)
sns.relplot(x="sepal_length", y="sepal_width", hue="species", data=iris)
sns.relplot(x="sepal_length", y="sepal_width",
            hue="species", style="species", data=iris)
sns.relplot(x="sepal_length", y="petal_length",
            hue="species", style="species", kind="line", data=iris)
sns.lineplot(x="sepal_length", y="petal_length",
             hue="species", style="species", data=iris)
sns.catplot(x="sepal_length", y="species", data=iris)
sns.catplot(x="sepal_length", y="species", kind="swarm", data=iris)
sns.catplot(x="sepal_length", y="species", kind="box", data=iris)
sns.catplot(x="sepal_length", y="species", kind="violin", data=iris)
sns.catplot(x="species", y="sepal_length", kind="boxen", data=iris)
sns.catplot(x="sepal_length", y="species", kind="point", data=iris)
sns.catplot(x="sepal_length", y="species", kind="bar", data=iris)
sns.catplot(x="species", kind="count", data=iris)
sns.distplot(iris["sepal_length"])
sns.kdeplot(iris["sepal_length"])
sns.jointplot(x="sepal_length", y="sepal_width", data=iris)
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="kde")
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="hex")
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="reg")
sns.pairplot(iris)
sns.pairplot(iris, hue="species")
sns.regplot(x="sepal_length", y="sepal_width", data=iris)
sns.lmplot(x="sepal_length", y="sepal_width", hue="species", data=iris)

plt.show()
sns.heatmap(np.random.rand(10, 10))
iris.pop("species")
sns.clustermap(iris)
plt.show()
