import openpyxl
import os

workbook = openpyxl.load_workbook('sample.xlsx')
print(workbook.get_sheet_names())
sheet = workbook.get_sheet_by_name('Sheet1')
print(sheet['A2'].value)

for i in range(1,8):
	print(i, sheet.cell(row=i, column=2).value)