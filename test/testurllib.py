#-*- codeing = utf-8 -*-
#@Time : 2021/1/23 19:17
#@Author : 摇脑壳的ocean
#@Flie : testurllib.py
#@Software : PyCharm

import urllib.request
# reponse = urllib.request.urlopen("http://www.baidu.com")
# print(reponse.read().decode('utf-8'))
import urllib.parse
# data = bytes(urllib.parse.urlencode({"ocean":"22"}),encoding="utf-8")
# # response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# # print(response.read().decode('utf-8'))
#超时处理
# try:
#     repsonse = urllib.request.urlopen("http://www.baidu.com",timeout=0.01)
#     print(repsonse.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.getheader("Server"))

url = "http://www.douban.com"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"

}
data = bytes(urllib.parse.urlencode({"ocean":"22"}),encoding="utf-8")
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))


