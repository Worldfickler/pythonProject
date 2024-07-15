"""
1.准备好top250电影数据全部的url，放在一个表中
2.遍历所有的url，进行数据抓取
3.优化代码
"""

import requests
from lxml import etree


class DouBan:
    base_url = 'https://movie.douban.com/top250?start={}&filter='

    def __init__(self):
        # 定义一个属性用来保存所有的url地址
        self.url_list = []
        # 生成所有页面的url地址保存到 url_list属性中
        for i in range(10):
            url = self.base_url.format(i * 25)
            self.url_list.append(url)

    def get_page_data(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }

        response = requests.get(url=url, headers=headers)

        page = response.content.decode()

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
    def run(self):
        for url in self.url_list:
            print("==========开始抓取页面数据：", url)
            self.get_page_data(url)

if __name__ == '__main__':
    db = DouBan()
    db.run()