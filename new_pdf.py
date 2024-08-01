from reportlab.pdfgen import canvas
# create a new pdf file
c=canvas.Canvas('my.pdf')

#add text and shapes to the pdf
c.drawString(100,750,"Hello world")
c.line(100,740,300,740)

#save pdf
c.save()