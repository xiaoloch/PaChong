import re
import urllib.request
import urllib.parse
import xlwings
from bs4 import BeautifulSoup
import sys

# 定义url，headers
url = 'http://httpbin.org/post'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}
# 创建data
dict = {"name":"Jay"}
data = bytes(urllib.parse.urlencode(dict),encoding="utf-8")
# 组织request对象
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")

# 使用request对象作为urlopen参数
response = urllib.request.urlopen(req)
# 打印返回结果
print(response.read().decode())


