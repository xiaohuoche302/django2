
import jieba
from PIL import Image  # 图片处理
import numpy as np  # 科学运算
from wordcloud import WordCloud, STOPWORDS  # 词云
import matplotlib
from matplotlib import pyplot as plt  # 绘图

# 显示中文
matplotlib.rcParams["font.sans-serif"] = ["simhei"]  # 配置字体
matplotlib.rcParams["font.family"] = "sans-serif"

pythonInfo = open('./lanlan.txt', 'r', encoding='utf-8', errors='ignore')
# 切割
myPythonCut = jieba.cut(pythonInfo.read(), cut_all=True)
pythonInfo.close()

myPythonCut = ' '.join(myPythonCut)

# RGB格式矩阵
bg = np.array(Image.open('./lanlan.png'))
print(bg)

myWordCloud = WordCloud(font_path='./simkai.ttf',  # 字体
                        width=200, height=200,
                        mask=bg,  # 字体颜色
                        scale=1,  # 缩放
                        max_words=200,  # 词云最大数量
                        min_font_size=4,  # 最小字体
                        stopwords=STOPWORDS,  # 停止词
                        random_state=90,  # 随机状态
                        background_color='black',  # 背景颜色
                        ).generate(myPythonCut)  # 生成词云

plt.figimage(myWordCloud)
plt.show()
# 保存
# plt.savefig('lanlan.jpg')