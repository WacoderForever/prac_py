from PIL import Image
from pylab import *

im = array(Image.open("Baki.jpeg"))
print(f"{im.shape} {im.dtype}")

