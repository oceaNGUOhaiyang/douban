# -*- codeing = utf-8 -*-
# @Time : 2021/1/23 21:23
# @Author : 摇脑壳的ocean
# @Flie : testBeautifulString.py
# @Software : PyCharm
from bs4 import BeautifulSoup
import re

file = open("baidu.html", "rb")  # 将文件以二进制形式读取到内存，rb = readbyte
html = file.read()
bs = BeautifulSoup(html, "html.parser")


# print(bs.title)  # 打印title标签
# print(bs.a)
# print(bs.head)
# print(bs.title.string)  # 打印标签里的字符串
# print(bs.a.attrs)  # 以字典的形式显示标签中所有的属性
# print(bs.name)
# print(bs)#打印整个文档
# print(bs.head.string)
# t_list = bs.find_all("a")  # 找到第一个标签（a）
# print(t_list)
# t_list = bs.find_all(re.compile("a"))  # 搜索所有包含a的
# print(t_list)
# def name_is_exist(tag):
#     return tag.has_attr("name")
#
#
# # 以自己定义的函数来搜索内容
# t_list = bs.find_all(name_is_exist)
# for item in t_list:
#     print(t_list)
# 按照参数来搜索
    # 按照id搜索
# t_list = bs.find_all(id="head")
# for item in t_list:
#     print(t_list)
    # 按照类名搜索
# t_list = bs.find_all(class_=True)
# print(t_list)
    #也可以直接搜索内容
#text参数
# t_list = bs.find_all(text=["hao123","地图"])
# for item in t_list:
#     print(item)
# t_list = bs.find_all(text=re.compile("\d"))#正则表达式来擦找特定文本
# for item in t_list:
#     print(item)
#限制搜索个数（limit）
# t_list = bs.find_all("a",limit=3)
# print(t_list)
#css选择器
'''
1、可以按标签来查找"title"
2、按类名来查找".mnav"（.类名）
3、按照id查找"#u1"（#id名）
4、按照属性来查找"a[class='bri']"、"a[name='tj_trnews']"
5、按照父节点来查找"head>title"
6、通过兄弟节点来访问".mnav~.bri"
'''
t_list = bs.select(".mnav~.bri")
print(t_list[0].get_text())
