from PIL import Image
from pylab import *
from numpy import *
from scipy.ndimage import filters

im = array(Image.open("Baki.jpeg").convert("L"))
gray()
imshow(im)
im2 = filters.gaussian_filter(im,sigma=1)
im3 = filters.gaussian_filter(im,sigma=3)
im4 = filters.gaussian_filter(im,sigma=5)
figure()
imshow(im2)
title("Sigma 1")
figure()
imshow(im3)
title("Sigma 2")
figure()
imshow(im4)
title("Sigma 3")

show()