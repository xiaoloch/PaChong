from bs4 import BeautifulSoup

with open("./sample.html","rb") as f:
    html = f.read()
    bs = BeautifulSoup(html,"html.parser")

# 获取整个标签 <获取的是同类型标签中的第一个标签>
# print(bs.title)
# print(bs.head)
# print(bs.a)
# print(type(bs.a))

# 获取标签的name和attrs属性
# print(bs.name)          # 输出[document],bs对象本身比较特殊，它的name即为[document]
# print(bs.head.name)     # 输出head, 对于其他内部标签，name属性就是标签本身的名称
# print(bs.a.attrs)       # 输出a标签的所有属性，得到的是一个字典
# print(bs.a["class"])    # 通过key获取标签某个属性
# bs.a["class"] = "newClass"  # 使用字典方法修改标签属性
# print(bs.a["class"])

# 获取标签的内容
# print(bs.title.string)
# print(type(bs.title.string))

# BeautifulSoup表示的是文档本身，是一种特殊的tag，有自己的属性
# print(type(bs.name))
# print(bs.name)
# print(bs.attrs)

# Comment 对象
print(bs.a)
print(bs.a.string)
print(type(bs.a.string))

