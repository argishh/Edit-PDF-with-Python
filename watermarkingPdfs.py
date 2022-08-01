from PyPDF2 import PdfFileReader, PdfFileWriter

pdf = PdfFileReader("assets/files/pdf1.pdf")
writer = PdfFileWriter()

image = PdfFileReader("assets/watermark.pdf")
watermark = image.getPage(0)

for i in range(pdf.getNumPages()):
    page = pdf.getPage(i)
    page.mergePage(watermark)
    writer.addPage(page)

with open('assets/watermarked_pdf.pdf', 'wb') as out:
    writer.write(out)
    print("Watermarked PDF created")
