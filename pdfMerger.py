import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir('./assets/files'):
    if file.endswith(".pdf"):
        merger.append(f'./assets/files/{file}')

merger.write("assets/Merged_pdf.pdf")