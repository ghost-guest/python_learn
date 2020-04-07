#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年04月07日 
# @Author  : ghost-guest
# @Site    : 
# @File    : dir_path.py
# @Software: PyCharm
# 说明： 
#! /usr/bin/python3

from os import path

def dir_path():
    file_path = path.dirname(__file__)
    # 返回父级目录
    return path.dirname(file_path)