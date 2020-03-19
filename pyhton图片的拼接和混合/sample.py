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
import matplotlib.pyplot as plt
import PIL
import os, time, random
import numexpr
from PIL import Image, ImageFont, ImageDraw

"""
RGBA： 颜色的三元素和透明度
os.getcwd() 获取当前文件所在的绝对路径
os.listdir 返回当前文件下的所有的文件和文件夹的名称
os.path.splitext() 函数将文件名和扩展名分开
os.path.split() 函数将文件路径和文件名分开
Image.open() open method used to open different extension image file
image.mode 对于彩色图像，不管其图像格式是PNG，还是BMP，或者JPG，在PIL中，
使用Image模块的open()函数打开后，返回的图像对象的模式都是“RGB”。而对于灰度图像，
不管其图像格式是PNG，还是BMP，或者JPG，打开后，其模式为“L”。
image.convert() Convert image to the given mode. The mode must be given as a string constant.
image.size in pixels. The size is given as a 2-tuple (width, height).
image.rotate() 旋转图片
# 图像旋转，两种方法：
new_img1 = im.transpose(Image.ROTATE_270) # 逆时针旋转270(有些人抄都不会抄，还顺时针呢)
new_img2 = im.rotate(90) # 逆时针旋转90
这里说一下这两种方法，new_img1就是单纯的旋转了图片的方向。new_img2在旋转以后，可能会发生裁剪（一般不推荐2）。
image.resize()  img.resize((width, height),Image.ANTIALIAS) PIL带ANTIALIAS滤镜缩放结果
image.crop()使用PIL裁切图片使用PIL需要引用Image，使用Image的open(file)方法可以返回打开的图片，使用crop((x0,y0,x1,y1))方法可以对图片做裁切。

区域由一个4元组定义，表示为坐标是 (left, upper, right, lower)，Python Imaging Library 使用左上角为 (0, 0)的坐标系统
scale() 
image.paste 方法将 im 放到第二个图片对象 im2 中，第二个参数是放置的中心点。
font = ImageFont.truetype: 导入字体 ，第一个参数是字体文件，第二个参数是字体的大小
draw = ImageDraw(img): 生成画笔，参数为要在图片中写字的图片对象。
draw.ink = R + G*256 + B*256*256: 来设置画笔的颜色
draw.text: 向图片对象中写字，第一个参数为字体的位置，用元组表示，第二个参数是内容，第三个参数是字体。
"""
STAG = time.time()
# W_num: 一行放多少张照片
# H_num: 一列放多少张照片
# W_size: 照片宽为多少
# H_size: 照片高为多少
# root: 脚本的根目录
root = ""
# 将 W_num 设置为更大的值可以取得更好的效果，例如 7，15
# 但请注意，因实验楼环境限制，更大的值会消耗更多的内存，这可能会导致程序崩溃。
W_num = 3
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
    root = os.getcwd() + '/resoures/'
    src = root + "/photos/"
    # 遍历文件夹内所有 jpg/png 图片 存储到上文写的全局数组 aval 中
    for i in os.listdir(src):
        if os.path.splitext(src + i)[-1] == '.jpg' or os.path.splitext(src + i)[-1] == '.png':
            aval.append(src + i)


# name: scale
# todo: 将照片转为一样的大小
def scale(image_path, dst_width, dst_height):
    STA = time.time()
    im = Image.open(image_path)
    if im.mode != "RGBA":
        im = im.convert("RGBA")  # 将所有的图片转化为RGBA
    s_w, s_h = im.size
    if s_w < s_h:
        # 将图片缩放到一致
        im = im.rotate(90)
    resized_img = im.resize((dst_width, dst_height), Image.ANTIALIAS)
    resized_img = resized_img.crop((0, 0, dst_width, dst_height))
    print('scale Func time %s' % (time.time() - STA))
    return resized_img


# name: jointAndBlend
# todo: 创造一张新的图片，并保存
def jointAndBlend():
    iw_size = W_num * W_size
    ih_size = H_num * H_size
    root = os.getcwd() + '/resoures/'
    print(111111111111111111111111111)

    I = np.array(scale(root + 'lyf.jpg', iw_size, ih_size))
    print(I)
    I = numexpr.evaluate("""I*(1-alpha)""")
    for i in range(W_num):
        for j in range(H_num):
            sh = I[(j * H_size):((j + 1) * H_size), (i * W_size):((i + 1) * W_size)]
            STA = time.time()
            DA = scale(random.choice(aval), W_size, H_size)
            print("循环的值%s" % (DA))
            print("Cal Func Time %s" % (time.time() - STA))
            res = numexpr.evaluate("""sh+DA*alpha""")
            I[(j * H_size):((j + 1) * H_size), (i * W_size):((i + 1) * W_size)] = res

    Image.fromarray(I.astype(np.uint8)).save("blend.png")


# name: rotate
# todo: 旋转照片 blend.py
def rotate():
    imName = "blend.png"
    print("正在讲图片翻转中.....")
    STA = time.time()
    im = Image.open(imName)
    im2 = Image.new("RGBA", (W_size * int(W_num + 1), H_size * (H_num + 4)))
    im2.paste(im, (int(0.5 * W_size), int(0.8 * H_size)))
    im2 = im2.rotate(359)
    im2.save("rotate.png")
    print("rotate Func Time %s" % (time.time() - STA))


# name: addText
# todo: 在图片中写祝福语
def addText():
    print("正在向图片中添加祝福语...")
    img = Image.open("blend.png")
    root = os.getcwd() + '/resoures/'
    fontWeight = W_num * W_size // 12
    font = ImageFont.truetype(root + 'xindexingcao57.ttf', fontWeight)
    draw = ImageDraw.Draw(img)
    draw.ink = 21 + 118 * 256 + 65 * 256 * 256

    #    draw.text((0,H_size * 6),unicode("happy every day",'utf-8'),(0,0,0),font=font)

    draw.text((W_size * 0.5, fontWeight), "happy life written by python", font=font)
    img.save("addText.png")


if __name__ == "__main__":
    getallpicture()
    jointAndBlend()
    rotate()
    addText()
    print("Total Time %s" % (time.time() - STAG))
