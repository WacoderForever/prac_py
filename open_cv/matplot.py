from PIL import Image
from pylab import *
# read image to array
im = array(Image.open("Baki.jpeg"))
# plot the image
imshow(im)
# some points
x = [100,100,500,520]
y = [200,500,200,520]
# plot points with red star markers
plot(x,y,'rx')
# line connecting the first points
plot(x[:2],y[:2])
title("Plotting: Baki")
show()