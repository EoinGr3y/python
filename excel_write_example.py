import openpyxl
import os

newWorkbook = openpyxl.Workbook()
sheet = newWorkbook.get_sheet_by_name('Sheet')

sheet['A1'] = 42
sheet['A2'] = 'Hello'

sheet1 = newWorkbook.create_sheet(index=0, title='New Sheet')

newWorkbook.save('write_example.xlsx')
