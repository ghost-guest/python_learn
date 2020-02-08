import matplotlib.pyplot as plt
import os
import wordcloud
import jieba
import imageio

# 导入字体和图片
font = os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")
mk = imageio.imread("alice_color.png")

# 导入字体
txt = open('alice.txt', encoding='utf-8').read()
tt = jieba.lcut(txt)
txt = "".join(tt)
# 构建词云
wc = wordcloud.WordCloud(background_color='white', mask=mk).generate(txt)
# 调用wordcloud库中的ImageColorGenerator()函数，提取模板图片各部分的颜色
image_colors = wordcloud.ImageColorGenerator(mk)
# 显示原生词云图、按模板图片颜色的词云图和模板图片，按左、中、右显示
fig, axes = plt.subplots(1, 3)
# 最左边的图片显示原生词云图
axes[0].imshow(wc)
# 中间的图片显示按模板图片颜色生成的词云图，采用双线性插值的方法显示颜色
axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
# 右边的图片显示模板图片
axes[2].imshow(mk, cmap=plt.cm.gray)
for ax in axes:
    ax.set_axis_off()
plt.show()

# 给词云对象按模板图片的颜色重新上色
wc_color = wc.recolor(color_func=image_colors)
# 将词云图片导出到当前文件夹
wc_color.to_file('output10-alice.png')

