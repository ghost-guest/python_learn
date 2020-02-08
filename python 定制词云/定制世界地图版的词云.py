import wordcloud
import jieba
import imageio
import os
import matplotlib.pyplot as plt
# 读取图片
mk = imageio.imread("chinamap.png")
# 字体，是词云支持中文
font=os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")

# 获取当前文件的绝对路径,读取文件
path = os.path.dirname(__file__)
txt = open(os.path.join(path, "新时代中国特色社会主义.txt"), encoding='utf-8').read()
# 对文件内容进行分词处理
tt = jieba.lcut(txt)
txt = ' '.join(tt)
# 创建词云对象
wc = wordcloud.WordCloud(width=1000,
                         height=700,
                         background_color='white',
                         font_path=font,
                         mask=mk,
                         scale=15).generate(txt)
# 创建词云
#wc.generate(txt)

# 展示图片
plt.imshow(wc)
plt.axis("off")
plt.show()
# 输出图片
wc.to_file("中国地图版词云.png")

