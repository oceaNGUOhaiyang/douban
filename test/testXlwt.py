# -*- coding = utf-8 -*-
# @Time : 2021/1/30 20:56
# @Author : ocean G
# @File : testXlwt.py
# @Software : PyCharm
import xlwt

'''
workbook = xlwt.Workbook(encoding="utf-8")#创建workbook对象
worksheet = workbook.add_sheet('sheet1')#创建工作表
worksheet.write(0,0,'hello')#写入数据，第一个参数行，第二个参数列
workbook.save('student.xls')
'''
workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
worksheet = workbook.add_sheet('sheet1')  # 创建工作表
for i in range(0, 9):
    for j in range(0, i+1):
        worksheet.write(i, j, "%d * %d = %d" % (i + 1, j + 1, (i + 1) * (j + 1)))
workbook.save('student.xls')
