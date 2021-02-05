# -*- coding = utf-8 -*-
# @Time : 2021/1/21 20:40
# @Author : 摇脑壳的ocean
# @File : spider.py
# @Software : PyCharm
from bs4 import BeautifulSoup

import re
import urllib.request
import urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页
    # savePath = ".\\豆瓣电影top250.xls"  # .表示当前文件夹，.\\表示生成文件系统
    dataList = getData(baseurl)

    # 解析数据
    # 保存数据
    # saveData(dataList, savePath)
    dbPath = "movie.db"
    saveData2DB(dataList, dbPath)
    # askURL("https://movie.douban.com/top250?start=")


# 定义正则提取的规则findLink
# 影片的详情链接
findLink = re.compile(r'<a href="(.*?)">')  # .表示一个字符，*：这一个字符出现0次或多次，？：构成的字符串出现0次或1次
# 影片的图片
findImageSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 忽略里面的换行符号
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>');
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
finBd = re.compile(r'<p class="">(.*?) </p>', re.S)


#

# 爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0, 10):
        url = baseUrl + str(i * 25)  # i = 0时，从第一个电影开始；i = 1时，从第25个开始，正好是第二页
        html = askURL(url)  # 保存网页的源码
        # 逐一解析
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            item = str(item)
            data = []
            # 获取影片详情链接
            link = re.findall(findLink, item)[0]  # findLink提取规则，item被提取的对象，[0]返回第一个提取到的
            data.append(link)  # 添加链接

            ImgSrc = re.findall(findImageSrc, item)[0]
            data.append(ImgSrc)  # 添加图片链接

            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append("无外国名")  # 添加名字，外国名字留空

            RatingNum = re.findall(findRating, item)
            data.append(RatingNum)  # 添加评分

            JudgeNum = re.findall(findJudge, item)
            data.append(JudgeNum)  # 添加评分人数

            inq = re.findall(findInq, item)
            # 针对无概况电影
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)
            else:
                data.append("无概况")

            bd = re.findall(finBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
            bd = re.sub('/', "", bd)
            data.append(bd.strip())  # 去掉前后空格

            dataList.append(data)  # 将处理好的一部电影放入dataList
    return dataList


# 保存数据
# def saveData(dataList, savePath):
#     print("save,,")
#     book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
#     sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)  # 创建工作表
#     col = ("电影详情链接", "图片连接", "影片名", "影片别名", "评分", "评价人数", "电影概况", "相关信息")
#     for i in range(0, 8):
#         sheet.write(0, i, col[i])
#     for i in range(0, 250):
#         print("第%d条" % (i + 1))
#         data = dataList[i]
#         for j in range(0, 8):
#             sheet.write(i + 1, j, data[j])
#     book.save(savePath)


def saveData2DB(dataList, dbPath):
    init_db(dbPath)
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()

    for data in dataList:
        for index in range(len(data)):
            data[index] = '"' + str(data[index]) + '"'
        sql = '''
        insert into movie250(
        info_link, pic_link, cname, ename, score, rated, introduction, info
        ) 
        values (%s)''' % ",".join(data)  # (",".join(data))将data中的值以","连接起来
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbPath):
    # 创建数据表
    sql = '''
    create table movie250
    (
    id integer primary key autoincrement,
    info_link text,
    pic_link text,
    cname varchar ,
    ename varchar ,
    score numeric ,
    rated numeric ,
    introduction text,
    info text  
    )
    '''
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()  # Cursor 是每行的集合
    cursor.execute(sql)
    conn.commit()
    conn.close()


def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / "
                      "87.04280.66Safari / 537.36 "
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):  # 判断e对象中是否有code属性
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == '__main__':  # 当程序执行时，调用函数,协调函数执行组织的流程(相当于主函数)
    # init_db("movieTest.db")
    main()
