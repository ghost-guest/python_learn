#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年03月16日 
# @Author  : ghost-guest
# @Site    : 
# @File    : sample.py
# @Software: PyCharm
# 说明： 

import pandas as pd
import numpy as np
import matplotlib.pylot as plt
import PIL
import os, time, random
import numexpr
from PIL import Image, ImageFont, ImageDraw

STAG = time.time()
# W_num: 一行放多少张照片
# H_num: 一列放多少张照片
# W_size: 照片宽为多少
# H_size: 照片高为多少
# root: 脚本的根目录
root = ""
# 将 W_num 设置为更大的值可以取得更好的效果，例如 7，15
# 但请注意，因实验楼环境限制，更大的值会消耗更多的内存，这可能会导致程序崩溃。
W_num =7
# 参考 W_num
H_num = 3
W_size = 640
H_size = 360
# aval: 存放所有照片的路径
alpha = 0.5
aval = []

# 获取所有的图片
def getallpicture():
    STA = time.time()
    # os.getcwd() 获取当前文件所在的绝对路径
    root = os.getcwd()+'/resoures/'
    src = root + "/photos/"
    # 遍历文件夹内所有 jpg/png 图片 存储到上文写的全局数组 aval 中
    for i in os.listdir(src):
        if os.path.splitext(src+i)[-1] == '.jpg' or os.path.splitext(src+i)[-1] == '.png':
            aval.append(src+i)
# name: scale
# todo: 将照片转为一样的大小
def scale(image_path, dst_width, dst_height):
    STA = time.time()
    im = Image.open(image_path)
    if im.mode != "RGBA":
        im = im.convrt("RGBA") # 将所有的图片转化为RGBA
    s_w,s_h = im.size
    if s_w < s_h:
        # 将图片缩放到一致
        im = im.rotate(90)
    resized_img = im.resize((dst_width, dst_height), Image.ANTIALIAS)
    resized_img = resized_img.crop((0,0,dst_width,dst_height))
    print('scale Func time %s'%(time.time()-STA))
    return resized_img
# name: jointAndBlend
# todo: 创造一张新的图片，并保存
def jointAndBlend():
    iw_size = W_num*W_size
    ih_size = H_num * H_size
    I = np.array(scale(root+'lyf.jpg', iw_size, ih_size))
    I = numexpr.evaluate("""I*(1-alpha)""")
    for i in range(W_num):
        for j in range(H_num):
            sh = I[(j*H_size):((j+1)*H_size), (i*W_size):((i+1)*W_size)]
            STA = time.time()
            DA = scale(random.choice(aval), W_size, H_size)
            print("Cal Func Time %s" % (time.time() - STA))
            res = numexpr.evaluate("""sh+DA*alpha""")
            I[(j * H_size):((j + 1) * H_size), (i * W_size):((i + 1) * W_size)] = res

    Image.fromarray(I.astype(np.uint8)).save("blend.png")




