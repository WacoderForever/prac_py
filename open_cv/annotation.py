from PIL import Image
from pylab import *

im = array(Image.open("Baki.jpeg"))
imshow(im)
print("Please click 4 points")
x = ginput(4)
print(f"You clicked: {x}")
show()