#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年04月07日 
# @Author  : ghost-guest
# @Site    : 
# @File    : runtest.py
# @Software: PyCharm
# 说明：

#! /usr/bin/python3

import unittest
from python_autotest.aa.HTMLTestRunner import HTMLTestRunner
from modules import sendEmail
from modules import getTestResult
from modules import dir_path
# discover = unittest.defaultTestLoader.discover("/Users/mac/Desktop/pyenv/python_autotest/myselenium/testcase/", pattern="test*.py")
# # # print(discover)
# # # runner = unittest.TextTestRunner()
# # # runner.run(discover)
# # filename = "/Users/mac/Desktop/pyenv/python_autotest/myselenium/report/report.html"
# # fp = open(filename, 'wb')
# # runner = HTMLTestRunner(stream=fp, title='AutoTest', description='My Selenium auto test')
# # runner.run(discover)
# # fp.close()





if __name__ == '__main__':

    # 测试用例路径
    test_dir = dir_path.dir_path() + '/testcase'
    # 测试报告存放路径
    report_dir = dir_path.dir_path() + '/report'

    filename = report_dir + '/report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='自动化测试', description='用例执行结果')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    runner.run(discover)
    fp.close()
    result = getTestResult.get_results(filename)
    print(result)
    mail = sendEmail.send_Mail(filename, result)
    if mail:
        print(u'邮件发送成功！')
    else:
        print(u'邮件发送失败！')