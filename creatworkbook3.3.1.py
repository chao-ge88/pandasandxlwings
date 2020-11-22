
import xlwings as xw #导入xlwings模块并命名为xw
app = xw.App(visible= True,add_book= False)#打开excel程序不新建工作薄
workbook = app.books.add()#新建工作薄
workbook.save('d:\\example.xlsx')#保存前面创建的空白文件簿
workbook.close()#关闭创建的文件簿
app.quit()#退出excel程序