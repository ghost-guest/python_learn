#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月30日 
# @Author  : ghost-guest
# @Site    : 
# @File    : t1.py
# @Software: PyCharm
# 说明： 
import jieba
import jieba.posseg as psg

sent = '自然语言处理是计算机科学领域与人工智能领域中的一个重要方向'
result = jieba.cut(sent, cut_all=False, HMM=False)
c = '｜'.join(result)
print(c)
result = jieba.cut(sent, cut_all=False, HMM=True)
c = '｜'.join(result)
print(c)

str = '自然语言处理是人工智能领域的一个重要分支'
for x in psg.cut(str):
    print(x.word, x.flag)
