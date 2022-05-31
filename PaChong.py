import re
import urllib.request
import urllib.parse
import xlwings
from bs4 import BeautifulSoup
import sys

url = "https://movie.douban.com/top250?start="


# 获取网页
def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode()
    return html


# 爬取数据
def getData(url):

    for i in range(0,1):
        # 构建url
        url = url + str(i * 25)
        # 获取页面数据
        html = askURL(url)
        # 生成bs对象
        bs = BeautifulSoup(html,"html.parser")
        # 定义data来接收一个电影的所有信息
        data = []
        # 定义datalist来接收所有电影的信息
        datalist = []
        # 遍历一个页面中的25条电影信息
        item = bs.find_all("div",class_="item")
        for j in item:
            j_str = str(j)
            # print(j_str)
            movie_name = re.findall(r'<span class="title">(.*)</span>',j_str)
            data.append(movie_name)



getData(url)

# 解析数据
def parseData():
    pass

# 保存数据
def saveData():
    pass

# 主程序

if __name__ == '__main__':
    pass

