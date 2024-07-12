"""
1.导入lxml
2.将获取到的网页数据转换为xml
3.通过xpath去定位和解析网页中的内容
"""
from lxml import etree

# 读取html页面内容(请求得到的response.content.decode('utf-8'))
page = open('douban.xml', 'r', encoding='utf-8').read()

# 将html页面转换为xml文档对象
html = etree.HTML(page)

