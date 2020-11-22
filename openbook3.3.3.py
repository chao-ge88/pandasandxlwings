import xlwings as xw
app = xw.App(visible=True,add_book=False)
workbook = app.books.open(r'd:\example.xlsx')#打开D盘下根文件夹下名为“example.xlsx”的工作薄
