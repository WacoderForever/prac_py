from PIL import Image
from pylab import *

# Load and convert image
img = array(Image.open("Baki.jpeg").convert('L'))

# Show original image
figure()
gray()
imshow(img)
axis("equal")
axis("off")
title('Original Image')

# Show inverted image
figure()
img1 = 255 - img  # invert image
imshow(img1)
axis("equal")
axis("off")
title('Inverted Image')

# Show power-law transformed image
figure()
img2 = 255 * (img/255.0)**2  # lower values of darker pixels
imshow(img2)
axis("equal")
axis("off")
title('Power-law Transformed')

show()  # This will display all figures at once