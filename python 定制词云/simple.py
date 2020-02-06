
#-*- coding: utf-8 -*-
from os import path
from wordcloud import WordCloud, STOPWORDS
import os
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

font=os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")


def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" %random.randint(60, 100)
d = path.dirname(__file__)

mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))
# read the whole txt
text = open(path.join(d, "santi.txt"), encoding="gbk").read()
text = text.replace("程心说", "程心")
text = text.replace("程心和", "程心")
text = text.replace("程心问", "程心")

stopword = set(STOPWORDS)
stopword.add('int')
stopword.add('ext')

# print(text)
# generate a word cloud image
#wordcloud = WordCloud().generate(text)
# display the generated image
# the matplotlib way:
wc = WordCloud(font_path=font, max_words=2000, mask=mask, stopwords=stopword, margin=10, random_state=1).generate(text)
#plt.imshow(wordcloud)
#plt.axis("off")
default_color = wc.to_array()

plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))
wc.to_file("a_new_hope.png")
plt.axis("off")
plt.savefig("aa.png")
# plt.figure()
plt.title("santi")
plt.imshow(default_color)
plt.axis("off")
# plt.figure()
plt.savefig('santi.png')

