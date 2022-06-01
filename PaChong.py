import re
import urllib.request
import urllib.parse
import xlwings
from bs4 import BeautifulSoup
import sys
import xlwings as xw

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
    # 定义datalist来接收所有电影的信息
    datalist = []

    for i in range(0,10):
        # 构建url
        url_real = url + str(i * 25)
        print(url_real)
        # 获取页面数据
        html = askURL(url_real)
        # 生成bs对象
        bs = BeautifulSoup(html,"html.parser")

        # 遍历一个页面中的25条电影信息
        item = bs.find_all("div",class_="item")
        for j in item:
            # 定义data来接收一个电影的所有信息
            data = []
            j_str = str(j)
            # print(j_str)
            """添加电影名到列表"""
            movie_name = re.findall(r'<span class="title">(.*)?</span>',j_str) # 匹配电影名，如果电影有外文名，可能会匹配到一个列表
            data.append(movie_name[0])  # 中文名
            if len(movie_name) == 2:    # 添加电影外文名
                movie_fr_name = re.sub("\s{2}","",movie_name[1].replace("/",""))
                data.append(movie_fr_name)
            else:
                data.append(" ")
            """添加链接到列表"""
            movie_link = re.findall(r'<a href="(.*)">',j_str)
            data.append(movie_link[0])
            # print(movie_link[0])
            """添加一句话描述到列表"""
            movie_des = re.findall(r'<span class="inq">(.*)</span>', j_str)
            # movie_des = movie_des[0].replace("。","")
            # print(movie_des)
            if len(movie_des) >= 1:
                data.append(movie_des[0])
            else:
                data.append("")
            """添加评分"""
            movie_rate = re.findall(r'<span class="rating_num" property="v:average">(.*)</span>', j_str)
            # movie_des = movie_des[0].replace("。","")
            # print(type(movie_des))
            data.append(movie_rate[0])
            """添加评价人数"""
            movie_eva_count = re.findall(r'<span>(\d*)人评价</span>', j_str)
            # print(movie_eva_count[0])
            data.append(movie_eva_count[0])
            """添加其他电影信息"""
            # print(j_str)
            movie_info = re.findall(r'<p class="">(.*?)</p>', j_str,re.S)
            movie_info = movie_info[0].strip()
            movie_info = re.sub(r'<br/>\W*\s*'," ",movie_info,re.S)
            # print(movie_info)
            data.append(movie_info)
            datalist.append(data)
    return datalist


# 保存数据
def saveData(data_list,save_path):
    # 创建app,开启实时进度可视化，关闭自动添加工作簿
    app = xw.App(visible=True, add_book=False)
    # 手动添加一个excel工作簿,即打开一个excel
    wb = app.books.add()
    # 读取sheet1，准备接收原始数据
    sht = wb.sheets["sheet1"]
    sht.range("a1").value = ["电影名称", "外文名称","电影链接", "一句话描述", "电影评分","参评人数","其他信息"]
    sht.range("a2").value = data_list

    wb.save(path=save_path)
    wb.close()
    app.quit()

# 主程序

if __name__ == '__main__':
    save_path = r'C:\Users\chenxia\Desktop\豆瓣评分top250电影.xlsx'
    data_list = getData(url)
    saveData(data_list,save_path)




