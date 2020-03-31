#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月31日 
# @Author  : ghost-guest
# @Site    : 
# @File    : demo3.py
# @Software: PyCharm
# 说明： 
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
# 进入51testing网站
driver.get('http://bbs.51testing.com/forum.php')
# 用id定位账号输入框并输入账号
driver.find_element_by_id("ls_username").send_keys("1qaz2wsx123")

# 用id定位密码输入框并输入密码
driver.find_element_by_id("ls_password").send_keys("1qaz2wsx")

# 定位“登录”按钮并获取登录按钮的文本
txt = driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').text
# 打印获取的文本
print(txt)
# 定位“登录”按钮并获取登录按钮的type属性值
type = driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').get_attribute("type")

# 打印type属性值
print(type)
# 定位“登录”按钮并进行点击操作
driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').click()
#alert = driver.switch_to.alert

# 查看alert中的文字

#print(alert.text)

# 点击确定

#alert.accept()

# 点击取消（如果有）

#alert.dismiss()
sleep(2)
# 页面下拉指定高度
js = 'document.documentElement.scrollTop=800;'
driver.execute_script(js)
sleep(3)
# 获取窗口所有句柄
all_handles = driver.window_handles
# 获取当前窗口句柄
curr_window = driver.current_window_handle
# 遍历所有句柄
for k in all_handles:
    # 如果不是当前窗口句柄
    if k != curr_window:
        # 窗口句柄切换
        driver.switch_to.window(k)
#iframe = driver.find_element_by_xpath()

# 切换到iframe

#driver.switch_to.frame(iframe)

#...页面操作代码...

# 跳出iframe

#driver.switch_to.default_content()
driver.quit()
