# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im = np.array(Image.open('../../data/empire.jpg').convert('L'))
print(int(im.min()), int(im.max()))

im2 = 255 - im  # invert image
print(int(im2.min()), int(im2.max()))

im3 = (100.0 / 255) * im + 100  # clamp to interval 100...200
print(int(im3.min()), int(im3.max()))

im4 = 255.0 * (im / 255.0) ** 2  # squared
print(int(im4.min()), int(im4.max()))

plt.figure()
plt.gray()
plt.subplot(1, 3, 1)
plt.imshow(im2)
plt.axis('off')
plt.title(r'$f(x)=255-x$')

plt.subplot(1, 3, 2)
plt.imshow(im3)
plt.axis('off')
plt.title(r'$f(x)=\frac{100}{255}x+100$')

plt.subplot(1, 3, 3)
plt.imshow(im4)
plt.axis('off')
plt.title(r'$f(x)=255(\frac{x}{255})^2$')
plt.show()
