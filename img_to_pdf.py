import img2pdf

img = "assets/watermark.png"

pdf = open("assets/Image_pdf.pdf", 'wb')
pdf.write(img2pdf.convert(img))
pdf.close()
