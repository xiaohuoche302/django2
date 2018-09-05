from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="brother" id="link2">Lacie</a> and
<p class="sister" id="link3">Tillie</p>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'lxml')
#格式化
# print(soup.prettify())

#标签名
# print(soup.title)

# .name 标签名
# print(soup.title.name)

# print(soup.title.string)

#第一个p
# print(soup.p)

#连用 p>b
# print(soup.p.b)

#.attrs 属性字典{"属性名":[]}
# print(soup.p.attrs['class'])
# print(soup.p['class'])

#标签下所有的文本
# print(soup.p.text)
# print(soup.p.get_text)
# print(soup.p.string)

#父
# print(soup.title.parent)
#祖父
# print(soup.title.parents)


# print(soup.a)
#所有，返回一个列表
# print(soup.find_all('a'))

# print(soup.find(id = "link3"))

# print(soup.find_all("p","title"))

#以T开头的文本
# print(soup.find_all(text=re.compile('^T')))

#中间含有s的文本
# print(soup.find_all(text=re.compile('s')))

# print(soup.find_all('a',attrs={'class':"sister"}))
# print(soup.find_all(class_='sister'))
# print(soup.find_all(id='link2'))

# print(soup.find_all('a',class_=['sister','brother'],limit=1))

#返回列表
print(soup.select('.sister'))
print(soup.select('a.sister'))