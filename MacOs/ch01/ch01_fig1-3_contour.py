# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# 添加中文字体支持
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='../../fonts/SimHei.ttf', size=14)
im = np.array(Image.open('../../data/empire.jpg').convert('L'))  # 打开图像，并转成灰度图像

plt.figure()
plt.subplot(121)
plt.gray()
# 在原点的左上角显示轮廓图像
plt.contour(im, origin='image')
plt.axis('equal')
plt.axis('off')
plt.title(u'图像轮廓', fontproperties=font)

plt.subplot(122)
plt.hist(im.flatten(), 255)
plt.title(u'图像直方图', fontproperties=font)
plt.xlim([0, 260])
plt.ylim([0, 11000])

plt.show()
