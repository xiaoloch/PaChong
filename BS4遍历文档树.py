from bs4 import BeautifulSoup

with open("./sample.html","rb") as f:
    html = f.read()
    bs = BeautifulSoup(html,"html.parser")

# contents：获取Tag的所有子节点，返回一个list
print(bs.contents)
print(bs.head.contents)
print(bs.head.contents[1])

# 获取Tag的所有子节点，返回一个生成器
print(bs.body.children)
for child in bs.body.children:
    print(child)



