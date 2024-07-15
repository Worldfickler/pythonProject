"""
# 发送post请求的方法：
    requests.post()
参数传递：
    1. 表单参数：form-data：
        requests.post(url, data=字典参数)
    2. json参数：
        requests.post(url, json=字典参数)
"""
import requests

# 百度翻译手机版发送post请求，传递表单参数
url = "https://fanyi.baidu.com/sug"

params = {
    "kw": "python3"
}

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

respose = requests.post(url=url, data=params, headers=headers)
print(respose.content.decode())