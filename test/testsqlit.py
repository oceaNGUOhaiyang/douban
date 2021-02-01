# -*- coding = utf-8 -*-
# @Time : 2021/1/31 17:23
# @Author : ocean G
# @File : testsqlit.py
# @Software : PyCharm
import sqlite3

# 创建数据库
# conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
# print("Opened database successfully")
# conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
#
# print("Opened database successfully")
#
# c = conn.cursor()  # 获取游标
# 创建表
# sql = '''
#     create table company
#     (id int primary key not null,
#     name text not null,
#     age int not null,
#     address char (50),
#     salary real
#     );
# '''
# c.execute(sql)
# conn.commit()
#
# 添加数据
# conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
# c = conn.cursor()  # 获取游标
# sql1 = '''
#     insert into company(id, name, age, address, salary)
#     values(1,'张三','22','武汉','10000')
# '''
# sql2 = '''
#     insert into company(id, name, age, address, salary)
#     values(2,'李四','25','荆州','15000')
# '''
# c.execute(sql1)
# c.execute(sql2)
# conn.commit()
#
# print("insert table successfully")
# 查询数据库
conn = sqlite3.connect("test.db")  # 打开或创建数据库文件
c = conn.cursor()  # 获取游标
sql = "select id,name,address,salary from company"
cursor = c.execute(sql)

for row in cursor:
    print("id = ", row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3], "\n")
conn.close()
print("query successfully")
