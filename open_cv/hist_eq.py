from PIL import Image
from pylab import *
from imtools import *

im = array(Image.open("Baki.jpeg").convert('L'))

imshow(im)

im2,cdf = histeq(im)

imshow(im2)

show()