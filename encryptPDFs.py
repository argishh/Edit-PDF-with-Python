import PyPDF2 as pdf

file = pdf.PdfFileReader('assets/files/pdf1.pdf')
writer = pdf.PdfFileWriter()

for i in range(file.getNumPages()):
    writer.addPage(file.getPage(i))

writer.encrypt(user_pwd = "python", owner_pwd = None, use_128bit = True)

newFileName = input("Enter new file name: ")
with open(f'assets/{newFileName}.pdf', 'wb') as f:
    writer.write(f)