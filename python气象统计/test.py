#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-04 19:31:45
@LastEditors: ghost-guest
@LastEditTime: 2020-03-09 19:39:22
@FilePath: /pyenv/python气象统计/test.py
@Description: 
'''
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from sklearn.svm import SVR

df_ferrara = pd.read_csv('WeatherData/ferrara_270615.csv')
df_milano = pd.read_csv('WeatherData/milano_270615.csv')
df_mantova = pd.read_csv('WeatherData/mantova_270615.csv')
df_ravenna = pd.read_csv('WeatherData/ravenna_270615.csv')
df_torino = pd.read_csv('WeatherData/torino_270615.csv')
df_asti = pd.read_csv('WeatherData/asti_270615.csv')
df_bologna = pd.read_csv('WeatherData/bologna_270615.csv')
df_piacenza = pd.read_csv('WeatherData/piacenza_270615.csv')
df_cesena = pd.read_csv('WeatherData/cesena_270615.csv')
df_faenza = pd.read_csv('WeatherData/faenza_270615.csv')

# 取出要分析的温度和日期
y1 = df_milano['temp']
x1 = df_milano['day']
y2 = df_faenza['temp']
x2 = df_faenza['day']
y3 = df_cesena['temp']
x3 = df_cesena['day']
y4 = df_milano['temp']
x4 = df_milano['day']
y5 = df_asti['temp']
x5 = df_asti['day']
y6 = df_torino['temp']
x6 = df_torino['day']
# 把日期数据转化为datetime格式

day_ravenna = [parser.parse(x) for x in x1]
day_faenza = [parser.parse(x) for x in x2]
day_cesena = [parser.parse(x) for x in x3]
day_milano = [parser.parse(x) for x in x4]
day_asti = [parser.parse(x) for x in x5]
day_torino = [parser.parse(x) for x in x6]

fig, ax = plt.subplots()
# 调整x轴坐标刻度，使其旋转70度，方便查看
plt.xticks(rotation=70)
# 设定时间格式
hours = mdates.DateFormatter("%H:%M")
# 设定x轴的显示格式
ax.xaxis.set_major_formatter(hours)
# 画出图像，day_milano是X轴数据，y1是Y轴数据，‘r’代表的是'red' 红色
# ax.plot(day_milano ,y1, 'r')
ax.plot(day_ravenna,y1,'r',day_faenza,y2,'r',day_cesena,y3,'r')
ax.plot(day_milano,y4,'g',day_asti,y5,'g',day_torino,y6,'g')
plt.show()

# dist 是一个装城市距离海边距离的列表
dist = [df_ravenna['dist'][0],
    df_cesena['dist'][0],
    df_faenza['dist'][0],
    df_ferrara['dist'][0],
    df_bologna['dist'][0],
    df_mantova['dist'][0],
    df_piacenza['dist'][0],
    df_milano['dist'][0],
    df_asti['dist'][0],
    df_torino['dist'][0]
]

# temp_max 是一个存放每个城市最高温度的列表
temp_max = [df_ravenna['temp'].max(),
    df_cesena['temp'].max(),
    df_faenza['temp'].max(),
    df_ferrara['temp'].max(),
    df_bologna['temp'].max(),
    df_mantova['temp'].max(),
    df_piacenza['temp'].max(),
    df_milano['temp'].max(),
    df_asti['temp'].max(),
    df_torino['temp'].max()
]
# temp_min 是一个存放每个城市最低温度的列表
temp_min = [df_ravenna['temp'].min(),
    df_cesena['temp'].min(),
    df_faenza['temp'].min(),
    df_ferrara['temp'].min(),
    df_bologna['temp'].min(),
    df_mantova['temp'].min(),
    df_piacenza['temp'].min(),
    df_milano['temp'].min(),
    df_asti['temp'].min(),
    df_torino['temp'].min()
]

fig, ax = plt.subplots()
ax.plot(dist, temp_max, 'ro')
# plt.show()

# dist1是靠近海的城市集合，dist2是远离海洋的城市集合
dist1 = dist[0:5]
dist2 = dist[5:10]
# 改变列表的结构，dist1现在是5个列表的集合
# 之后我们会看到 nbumpy 中 reshape() 函数也有同样的作用
dist1 = [[x] for x in dist1]
dist2 = [[x] for x in dist2]
# temp_max1 是 dist1 中城市的对应最高温度
temp_max1 = temp_max[0:5]
# temp_max2 是 dist2 中城市的对应最高温度
temp_max2 = temp_max[5:10]
# 我们调用SVR函数，在参数中规定了使用线性的拟合函数
# 并且把 C 设为1000来尽量拟合数据（因为不需要精确预测不用担心过拟合）
svr_lin1 = SVR(kernel='linear', C=1e3)
svr_lin2 = SVR(kernel='linear', C=1e3)
# 加入数据，进行拟合（这一步可能会跑很久，大概10多分钟，休息一下:) ）
svr_lin1.fit(dist1, temp_max1)
svr_lin2.fit(dist2, temp_max2)
# 关于 reshape 函数请看代码后面的详细讨论
xp1 = np.arange(10,100,10).reshape((9,1))
xp2 = np.arange(50,400,50).reshape((7,1))
yp1 = svr_lin1.predict(xp1)
yp2 = svr_lin2.predict(xp2)
# 限制了 x 轴的取值范围
fig, ax = plt.subplots()
ax.set_xlim(0,400)
# 画出图像
ax.plot(xp1, yp1, c='b', label='Strong sea effect')
ax.plot(xp2, yp2, c='g', label='Light sea effect')
ax.plot(dist,temp_max,'ro')
plt.show()