import re
import urllib.request
import urllib.parse
import xlwings
from bs4 import BeautifulSoup
import sys


# 简单get请求
response = urllib.request.urlopen("http://www.baidu.com")   # urlopen跟一个url参数可以返回一个网页对象
# print(response.read().decode('utf-8'))                      # 网页对象的read方法可以获得网页的完整内容（返回的html文件）
print(response.status)                      # 打印状态码
print(response.getheaders())                # 得到所有响应头，结果是一个由元组组成的列表
print(response.getheader("Cache-Control"))  # 得到特定响应头






