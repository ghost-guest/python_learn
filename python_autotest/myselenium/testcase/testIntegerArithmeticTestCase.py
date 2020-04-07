#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年04月07日 
# @Author  : ghost-guest
# @Site    : 
# @File    : testIntegerArithmeticTestCase.py
# @Software: PyCharm
# 说明： 
#! /usr/bin/python3

import unittest

class testIntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
        print("testAdd passed")
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
        print("testMultiply passed")

if __name__ == '__main__':
    unittest.main()