"""
准备工作
    安装requests库：pip install requests
    在代码中导入requests

需求：使用代码获取百度首页内容

步骤：
    1.百度地址：https://www.baidu.com/
    2.发送请求
        requests.get(url)
    3.获取返回的结果
"""
# 导入requests库
import requests

# 百度首页的地址
url = "https://www.baidu.com/"

# 使用requests发送get请求
response = requests.get(url=url)

# 打印返回的结果
print(response.text)