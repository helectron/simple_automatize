#!/usr/bin/python3
from PyPDF2 import PdfFileMerger

pdfs = ["PdfFileWriter.pdf", "RectangleObject.pdf"]
nombre_archivo_salida = "secop_pantallazos.pdf"
fusionador = PdfFileMerger()

for pdf in pdfs:
    fusionador.append(open(pdf, 'rb'))

with open(nombre_archivo_salida, 'wb') as salida:
    fusionador.write(salida)
