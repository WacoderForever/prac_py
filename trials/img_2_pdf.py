import img2pdf
from PIL import Image
import os

#storing image path
img_path="/home/wacoder/Documents/prac_py/IMG-20240401-WA0000.jpg"

#storing pdf path
pdf_path="file_pdf.pdf"

image=Image.open(img_path)

#converting into chunks using img2pdf
pdf_bytes=img2pdf.convert(image.filename)

#opening or creating pdf file
file=open(pdf_path,"wb")

#writing pdf files with chunks
file.write(pdf_bytes)

#closing image file
image.close()

#closing pdf file
file.close()

print("Successfully made pdf file")
