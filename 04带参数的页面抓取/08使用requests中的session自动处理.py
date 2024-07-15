"""
方式一：以字典格式传递
    cookies = {}
    request.get(cookies=cookies)

方式二：以字符串格式传递
    headers = {
        'Cookie': "字符串格式cookie值"
    }
    request.get()

方式三：requests.session.cookies =

"""

import requests

login_url = "https://passport.china.com/logon"
params = {
    "userName": "17775990925",
    "password": "a546245426"
}
headers = {
    "Referer": "https://passport.china.com/logon",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

# 1、使用requests.session创建一个请求的对象
http = requests.session()
# 2、发送请求进行登录
response = http.post(login_url, data=params, headers=headers)
# 3、请求需要登录的页面
res2 = http.get("https://passport.china.com", headers=headers)
print(res2.content.decode())
