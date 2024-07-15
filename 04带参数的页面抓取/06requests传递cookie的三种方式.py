"""
模拟登录，访问需要登录之后才能打开的页面
    1、发送登录请求
    2、保存cookie信息
    3、携带cookie信息请求需要登录的页面
"""
import requests

login_url = "https://passport.china.com/logon"
params = {
    "userName": "17775990925",
    "password": "a546245426"
}
headers = {
    "Referer": "https://passport.china.com/logon",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# 发送请求进行登录
response = requests.post(login_url, data=params, headers=headers)
print(response.content.decode())

"""
方式一：以字典格式传递
    cookies = {}
    request.get(cookies=cookies)
    
方式二：以字符串格式传递
    headers = {
        'Cookie': "字符串格式cookie值"
    }
    request.get()
"""

# 获取cookie信息
cookie = response.cookies
# 请求需要登录的页面
res2 = requests.get("https://passport.china.com", cookies=cookie, headers=headers)
print(res2.content.decode())