#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月25日 
# @Author  : ghost-guest
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# 说明： 
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np

plt.plot([1, 2, 3, 4, 5, 6, 9, 7, 8, 1, 2, 3, 4, 5, 6, 7],
         [13, 14, 15, 16, 17, 18, 19, 10, 11, 12, 13, 14, 15, 16, 18, 13])
plt.show()

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# 在指定的间隔内返回均匀间隔的数字。
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.show()

plt.bar([1, 2, 3], [1, 2, 3])
plt.show()

x = np.random.ranf(1000)
# print(x)
y = np.random.ranf(1000)
plt.scatter(x, y)
plt.show()

plt.pie([1, 2, 3, 3])
plt.show()

# 在 -2PI 和 2PI 之间等间距生成 1000 个值，也就是 X 坐标
X = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
# 计算 sin() 对应的纵坐标
y1 = np.sin(X)
# 计算 cos() 对应的纵坐标
y2 = np.cos(X)

# 向方法中 `*args` 输入 X，y 坐标
plt.plot(X, y1, color='r', linestyle='--', linewidth=2, alpha=0.8)
plt.plot(X, y2, color='b', linestyle='-', linewidth=2)
plt.show()
label = 'Cat', 'Dog', 'Cattle', 'Sheep', 'Horse'  # 各类别标签
color = 'r', 'g', 'r', 'g', 'y'  # 各类别颜色
size = [1, 2, 3, 4, 5]  # 各类别占比
explode = (0, 0, 0, 0, 0.2)  # 各类别的偏移半径
# 绘制饼状图
plt.pie(size, colors=color, explode=explode,
        labels=label, shadow=True, autopct='%1.1f%%')
# 饼状图呈正圆
plt.axis('equal')
plt.show()
x = np.linspace(0, 10, 20)  # 生成数据
y = x * x + 2

fig = plt.figure()  # 新建图形对象
axes = fig.add_axes([0.5, 0.5, 0.8, 0.8])  # 控制画布的左, 下, 宽度, 高度
axes.plot(x, y, 'r')
plt.show()
fig = plt.figure()  # 新建画板
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # 大画布
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # 小画布

axes1.plot(x, y, 'r')  # 大画布
axes2.plot(y, x, 'g')  # 小画布
plt.show()


fig, axes = plt.subplots()
axes.plot(x, y, 'r')
plt.show()
fig, axes = plt.subplots(nrows=1, ncols=2)  # 子图为 1 行，2 列
for ax in axes:
    ax.plot(x, y, 'r')
plt.show()
fig, axes = plt.subplots(
    figsize=(16, 9), dpi=50)  # 通过 figsize 调节尺寸, dpi 调节显示精度
axes.plot(x, y, 'r')
plt.show()
fig, axes = plt.subplots()

axes.set_xlabel('x label')  # 横轴名称
axes.set_ylabel('y label')
axes.set_title('title')  # 图形名称

axes.plot(x, x**2)
axes.plot(x, x**3)
axes.legend(["y = x**2", "y = x**3"], loc=0)  # 图例
plt.show()
fig, axes = plt.subplots()

axes.plot(x, x+1, color="red", alpha=0.5)
axes.plot(x, x+2, color="#1155dd")
axes.plot(x, x+3, color="#15cc55")
plt.show()
fig, ax = plt.subplots(figsize=(12, 6))

# 线宽
ax.plot(x, x+1, color="blue", linewidth=0.25)
ax.plot(x, x+2, color="blue", linewidth=0.50)
ax.plot(x, x+3, color="blue", linewidth=1.00)
ax.plot(x, x+4, color="blue", linewidth=2.00)

# 虚线类型
ax.plot(x, x+5, color="red", lw=2, linestyle='-')
ax.plot(x, x+6, color="red", lw=2, ls='-.')
ax.plot(x, x+7, color="red", lw=2, ls=':')

# 虚线交错宽度
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10])

# 符号
ax.plot(x, x + 9, color="green", lw=2, ls='--', marker='+')
ax.plot(x, x+10, color="green", lw=2, ls='--', marker='o')
ax.plot(x, x+11, color="green", lw=2, ls='--', marker='s')
ax.plot(x, x+12, color="green", lw=2, ls='--', marker='1')

# 符号大小和颜色
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-',
        marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue")
plt.show()
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# 显示网格
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

# 设置坐标轴范围
axes[1].plot(x, x**2, x, x**3)
axes[1].set_ylim([0, 60])
axes[1].set_xlim([2, 5])
plt.show()
n = np.array([0, 1, 2, 3, 4, 5])

fig, axes = plt.subplots(1, 4, figsize=(16, 5))

axes[0].scatter(x, x + 0.25*np.random.randn(len(x)))
axes[0].set_title("scatter")

axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")

axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes[2].set_title("bar")

axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)
axes[3].set_title("fill_between")
plt.show()
fig, axes = plt.subplots()

x_bar = [10, 20, 30, 40, 50]  # 柱形图横坐标
y_bar = [0.5, 0.6, 0.3, 0.4, 0.8]  # 柱形图纵坐标
bars = axes.bar(x_bar, y_bar, color='blue', label=x_bar, width=2)  # 绘制柱形图
for i, rect in enumerate(bars):
    x_text = rect.get_x()  # 获取柱形图横坐标
    y_text = rect.get_height() + 0.01  # 获取柱子的高度并增加 0.01
    plt.text(x_text, y_text, '%.1f' % y_bar[i])  # 标注文字
plt.show()
fig, axes = plt.subplots()

bars = axes.bar(x_bar, y_bar, color='blue', label=x_bar, width=2)  # 绘制柱形图
for i, rect in enumerate(bars):
    x_text = rect.get_x()  # 获取柱形图横坐标
    y_text = rect.get_height() + 0.01  # 获取柱子的高度并增加 0.01
    plt.text(x_text, y_text, '%.1f' % y_bar[i])  # 标注文字

    # 增加箭头标注
    plt.annotate('Min', xy=(32, 0.3), xytext=(36, 0.3),
                 arrowprops=dict(facecolor='black', width=1, headwidth=7))
plt.show()


x = np.linspace(0, 10, 20)
y = x * x + 2
pylab.plot(x, y, 'r')  # 'r' 代表 red
pylab.show()
pylab.subplot(1, 2, 1)  # 括号中内容代表（行，列，索引）
pylab.plot(x, y, 'r--')  # ‘’ 中的内容确定了颜色和线型

pylab.subplot(1, 2, 2)
pylab.plot(y, x, 'g*-')
pylab.show()
