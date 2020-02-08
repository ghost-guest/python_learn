import jieba
import os
import wordcloud
import matplotlib.pyplot as plt
import imageio

# 获取图片
mk = imageio.imread("chinamap.png")
# 获取字体
font = 'DroidSansFallbackFull.ttf'
# 读取文件
txt = open("三国演义.txt", encoding='utf-8').read()
# 分词处理
tt = jieba.lcut(txt)
txt = ''.join(tt)
# 创建词云对象,注意增加参数contour_width和contour_color设置轮廓宽度和颜色
wc = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color="white",
    font_path=font,
    mask=mk,
    scale=15,
    contour_width=2,
    contour_color='blue'
)
# 构建词云
wc.generate(txt)
# 展示词云图片
plt.imshow(wc)
plt.axis("off")
plt.show()
# 生成词云图片
wc.to_file('勾勒轮廓.png')