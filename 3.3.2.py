import xlwings as xw
app = xw.App(visible=True, add_book=False)
workbook = app.books.add()
workbook.save('d:\\example.xlsx')
workbook.close()
app.quit()