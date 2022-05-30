import re
import urllib.request
import urllib.parse
import xlwings
from bs4 import BeautifulSoup
import sys

# 使用 urlencode() 函数可以将一个 dict 转换成合法的查询参数
query_args = urllib.parse.urlencode({"name":"zhangsan","age":18})
print(query_args)

# 使用bytes函数将上文的查询字符串转换为二进制序列
data = bytes(query_args,encoding='utf-8')
print(data)

# 使用变量接收一个url路径
url = 'http://httpbin.org/post'

# 将二进制表单数据作为携带的参数发送post请求
try:
    response = urllib.request.urlopen(url,data=data, timeout=0.1)
    print(response.read().decode())
except Exception as e:
    print(url)





