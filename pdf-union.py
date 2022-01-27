#!/usr/bin/python3
from PyPDF2 import PdfFileMerger

pdfs = ["PdfFile1.pdf", "PdfFile2.pdf"]
nombre_archivo_salida = "FinalPdf.pdf"
fusionador = PdfFileMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)
