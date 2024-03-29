from PIL import Image
from pylab import *
from scipy.ndimage import filters

# from SciPy import misc

im = array(Image.open('../../data/empire.jpg').convert('L'))
# im = misc.lena()
gray()

subplot(1, 2, 1)
axis('off')
imshow(im)

sigma = 3

imx = im + 0.4 * (im - filters.gaussian_filter(im, sigma))
imx = np.clip(imx, 0, 255)

subplot(1, 2, 2)
axis('off')
imshow(imx)

show()
