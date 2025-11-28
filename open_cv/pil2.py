from PIL import Image

pil_im = Image.open("Baki.jpeg")

pil_im.thumbnail((128,128))

pil_im.show()