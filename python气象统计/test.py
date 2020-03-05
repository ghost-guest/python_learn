#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@Author: ghost-guest
@Date: 2020-03-04 19:31:45
@LastEditors: ghost-guest
@LastEditTime: 2020-03-05 19:29:08
@FilePath: /pyenv/python气象统计/test.py
@Description: 
'''
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser

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

