import os
import PyPDF2

def addPagesToWriter(writer, reader):
	for pageNum in range(reader.numPages):
		page = reader.getPage(pageNum)
		writer.addPage(page)


firstPdfFile = open('meetingminutes1.pdf', 'rb')
secondPdfFile = open('meetingminutes1.pdf', 'rb')
firstReader = PyPDF2.PdfFileReader(firstPdfFile)
secondReader = PyPDF2.PdfFileReader(secondPdfFile)
writer = PyPDF2.PdfFileWriter()

addPagesToWriter(writer, firstReader)
addPagesToWriter(writer, secondReader)
outputFile = open('combinedmeetingminutes.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
firstPdfFile.close()
secondPdfFile.close()