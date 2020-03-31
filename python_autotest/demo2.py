#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月31日 
# @Author  : ghost-guest
# @Site    : 
# @File    : demo2.py
# @Software: PyCharm
# 说明： 
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
# 浏览器进入百度
driver.get('https://www.baidu.com')
# 设置浏览器的宽度和高度
driver.set_window_size(800, 400)
# 等待3s
sleep(3)
# 进入另一个网站
driver.get('https://www.shiyanlou.com/')
sleep(3)

# 后退到上一个页面
driver.back()
sleep(3)
# 前进到下一个页面
driver.forward()
sleep(3)
# 刷新页面
driver.refresh()
# 等待3s
sleep(3)
# 最大窗口化
driver.maximize_window()
# 退出浏览器
driver.quit()
