Python 3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:19:19) 
[Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import openpyxl
>>> import os
>>> os.chdir('/weijunxia/documents/python')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.chdir('/weijunxia/documents/python')
FileNotFoundError: [Errno 2] No such file or directory: '/weijunxia/documents/python'
>>> os.chdir('/users/weijunxia/documents/python')
>>> os.getcwd()
'/Users/weijunxia/Documents/python'
>>> workbook = openpyxl.load_workbook('exmaple.xlsx')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    workbook = openpyxl.load_workbook('exmaple.xlsx')
  File "/Users/weijunxia/Library/Python/3.9/lib/python/site-packages/openpyxl/reader/excel.py", line 315, in load_workbook
    reader = ExcelReader(filename, read_only, keep_vba,
  File "/Users/weijunxia/Library/Python/3.9/lib/python/site-packages/openpyxl/reader/excel.py", line 124, in __init__
    self.archive = _validate_archive(fn)
  File "/Users/weijunxia/Library/Python/3.9/lib/python/site-packages/openpyxl/reader/excel.py", line 96, in _validate_archive
    archive = ZipFile(filename, 'r')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/zipfile.py", line 1239, in __init__
    self.fp = io.open(file, filemode)
FileNotFoundError: [Errno 2] No such file or directory: 'exmaple.xlsx'
>>> workbook = openpyxl.load_workbook('example.xlsx')
>>> type(workbook)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> sheet = workbook.get_sheet_by_name('Sheet1')

Warning (from warnings module):
  File "<pyshell#9>", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
>>> sheet = workbook.get_sheet_by_name('Sheet1')
>>> type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> workbook.get_sheet_names()

Warning (from warnings module):
  File "<pyshell#12>", line 1
DeprecationWarning: Call to deprecated function get_sheet_names (Use wb.sheetnames).
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet['A1']
<Cell 'Sheet1'.A1>
>>> cell = sheet['A1']
>>> cell.value
datetime.datetime(2015, 4, 5, 13, 34, 2)
>>> str(sheet['A1'].value)
'2015-04-05 13:34:02'
>>> int(sheet['C1'].value)
73
>>> sheet.cell(row=1, column=2)
<Cell 'Sheet1'.B1>
>>> sheet['B1']
<Cell 'Sheet1'.B1>
>>> for i in range(1, 8
	       )
SyntaxError: invalid syntax
>>> for i in range(1,8):
	print(i, sheet.cell(row=i, column=2). value)

	
1 Apples
2 Cherries
3 Pears
4 Oranges
5 Apples
6 Bananas
7 Strawberries
>>>

# The OpenPyXL third-part module handles Excel spreadsheets
# openpyxl.load_workbook(filename) returns a Workbook object.
# get_sheet_names() and get_sheet_by_names() help get Worksheet objects
# The square brackets in sheet['A1'] get Cell objects
# Cell objects have a value member variable with the content of that cell
# The cell() method also returns a Cell object from a sheet                         
                         
