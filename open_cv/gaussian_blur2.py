from PIL import Image
from pylab import *
from numpy import *
from scipy.ndimage import filters

im = array(Image.open("Baki.jpeg"))
imshow(im)
title("Original image")
print(f"im.shape(): {im.shape}\n")
im2 = im.copy()
im3 = im.copy()
im4 = im.copy()

for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],1)

for i in range(3):
    im3[:,:,i] = filters.gaussian_filter(im[:,:,i],3)

for i in range(3):
    im4[:,:,i] = filters.gaussian_filter(im[:,:,i],10)

figure()
imshow(im2)
title("Sigma 1")

figure()
imshow(im3)
title("Sigma 3")

figure()
imshow(im4)
title("Sigma 10")

show()
