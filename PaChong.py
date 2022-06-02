import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import sys
import xlwings as xw
import pymysql



# 获取网页对象
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
    for i in datalist:
        print(i)
    return datalist

# 保存数据到excel
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

# 初始化数据库
def iniDatabase():
    conn = pymysql.connect(host="192.168.29.128", port=3306, user="root", password="123", database="PaChong",
                           charset="utf8")
    cur = conn.cursor()

    sql = '''create table students(
    id int primary key auto_increment not null,
    movie_cn_name varchar(100) not null,
    movie_fr_name varchar(100),
    movie_link varchar(100),
    movie_des varchar(100),
    movie_score float not null,
    movie_rated int not null,
    movie_info varchar(200)
    )
    '''
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()

# 保存数据到MySQL数据库
def saveData_db(data_list):
    conn = pymysql.connect(host="192.168.29.128",port=3306,user="root",password="123",database="PaChong",charset="utf8")    # 创建数据库连接
    cur = conn.cursor()     # 创建游标对象
    for item in data_list:
        '''给除数字外其他所有的列表元素加引号，因为sql中values后的括号中的内容，如果是字符串，必须带引号，直接用列表下标取出来的数据是不带引号的，所以要额外添加。数字则不用'''
        for i in range(len(item)):
            if i == 4 or i == 5:
                continue
            item[i] = '"'+item[i]+'"'
        '''将列表中的元素用“，”连接起来'''
        values = ",".join(item)
        '''一定要声明所有字段，如果不声明，那么values后的括号中就需要带上id字段的值'''
        sql = "insert into students (movie_cn_name,movie_fr_name,movie_link,movie_des,movie_score,movie_rated,movie_info) values(%s)" %values
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

# 主程序
if __name__ == '__main__':
    url = "https://movie.douban.com/top250?start="
    save_path = r'C:\Users\chenxia\Desktop\豆瓣评分top250电影.xlsx'
    data_list = getData(url)
    saveData(data_list,save_path)
    # iniDatabase()
    saveData_db(data_list)




