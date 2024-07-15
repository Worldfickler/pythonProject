"""
xpath数据提取的技巧
1.定位到包含所有数据的元素
2.再从中找到包含多条数据全部内容的元素
3.对定位到包含多条数据的列表进行遍历，得到包含多条数据的元素
4.再提取单条数据中的详细内容
"""

from lxml import etree

# 读取html页面内容(请求得到的response.content.decode('utf-8'))
page = open('douban.html', 'r', encoding='utf-8').read()

# 将html页面转换为xml文档对象
html = etree.HTML(page)

# 定位到包含多条数据的元素
data_list = html.xpath("//ol//li")
# 对定位到包含多条数据的列表进行遍历，得到包含多条数据的元素
for li in data_list:
    # 提取单条数据中的详细内容
    title = li.xpath(".//span[@class='title'][1]/text()")
    score = li.xpath(".//span[@class='rating_num'][1]/text()")
    number = li.xpath(".//div[@class='star']/span[last()]/text()")
    print("电影的名称：", title[0], "评分：", score[0], "评价人数：", number[0])
