from PIL import Image
from pylab import *

# read image and convert to grayscale
im = array(Image.open("Baki.jpeg").convert('L'))

# create new figure
figure()
# everything gray
gray()
# show contours with origin upper left corner
contour(im,origin='image')
axis("equal")
axis("off")
figure()
# im.flatten converts the 2D im into a 1D array
hist(im.flatten(),128)
show()