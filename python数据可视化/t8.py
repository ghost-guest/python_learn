#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-01 14:44:14
@LastEditors: ghost-guest
@LastEditTime: 2020-03-01 14:48:31
@FilePath: /pyenv/python数据可视化/t8.py
@Description: 数学示例
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 一步是定义需要求取积分的函数
def func(x):
    return 0.5 * np.exp(x) + 1

# 第二步是定义积分区间，生成必需的数值
a, b = 0.5, 1.5
x = np.linspace(0, 2)
y = func(x)
# 第三步，绘制函数图形
fig, ax = plt.subplots(figsize=(7, 5))
plt.plot(x, y, 'b', linewidth=2)
plt.ylim(ymin=0)

# 第四步是核心，我们使用 Polygon 函数生成阴影部分（“补丁”），表示积分面积
Ix = np.linspace(a, b)
Iy = func(Ix)
verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]
poly = Polygon(verts, facecolor='0.7', edgecolor='0.5')
ax.add_patch(poly)

# 第五步是用 plt.text 和 plt.figtext 在图表上添加数学公式和一些坐标轴标签。LaTeX 代码在两个美元符号之间传递（……）。两个函数的前两个参数都是放置对应文本的坐标值：
plt.text(0.5 * (a + b), 1, r"$\int_a^b fx\mathrm{d}x$", horizontalalignment='center', fontsize=20)
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')

'''
最后，我们分别设置x和y刻度标签的位置。注意，尽管我们以 LaTeX 渲染变量名称，
但是用于定位的是正确的数字值。我们还添加了网格，在这个特殊例子中，只是为了强调选中的刻度：
'''
ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([func(a), func(b)])
ax.set_yticklabels(('$f(a)$', '$f(b)$'))
plt.grid(True)
plt.show()