import re

from bs4 import BeautifulSoup

with open("./sample.html","rb") as f:
    html = f.read()
    bs = BeautifulSoup(html,"html.parser")

#格式: find_all(name,attrs,recursive,text,**kwargs)
# name参数之字符串过滤，给定一个字符串，去查找所有同名的标签，返回一个列表，包含所有匹配到的标签及其完整内容
# 注意搜索标签的名字，不搜索标签的内容
# a_list = bs.find_all("a")
# print(a_list)

# name参数之正则表达式过滤
# a_list = bs.find_all(re.compile("a"))
# print(a_list)

# name参数之列表
# a_list = bs.find_all(["meta","a"])
# for i in a_list:
#     print(i)

# name参数之方法
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)
#

a_list = bs.find_all(id="head")
print(a_list)
t_list = bs.find_all(class_=True)
for item in t_list:
    print(item)
t_list = bs.find_all(href=re.compile("http://news.baidu.com"))
print(t_list)
