import os
import PyPDF2

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages)

firstPage = reader.getPage(0)
text = firstPage.extractText()
print(text)