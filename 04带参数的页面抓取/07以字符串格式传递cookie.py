import requests

login_url = "https://passport.china.com/logon"
params = {
    "userName": "17775990925",
    "password": "a546245426"
}
headers = {
    "Referer": "https://passport.china.com/logon",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Cookies": 'SESSION_COOKIE=128; Hm_lvt_cbec92dec763e6774898d6d85460f707=1721034840; HMACCOUNT=E5BCE77F3EB5F2EA; JSESSIONID=C7A9367722BEF38D0B80D27E08620E2E; lastlogindate=2024-07-15; lastloginip=123.235.48.246; Hm_lpvt_cbec92dec763e6774898d6d85460f707=1721036509; nickname=china_2823hxfg16791058; lastlogindate=2024-07-15; lastlogintime="17:42:14"; lastloginip=123.235.48.246; bindMobile="1@177*****925"; CHINACOMID=75ed7bf5-ab94-46ef-815d-81efd01f671b7; CP_USER=FKBo6w-aaDELXK1EnoT3DPk1faoTCuWOzIpsuaQNIsJWqiRz6o9drrZQMJZRRbngi7eJikd0sv41eZDrzksZGmumfJyC7TEP5dMN41%2F1QIHag0K39t%2FVBxzGqQTN85yGQKsLIHYEn0hORp7bAAnEJFS3hTK5kFcZre4%2FGCjiN7OfXDGy9eh53nib-nLC0D4U9sAz2fCm4OX38oR5BdZZuFVAiEwFlncomlLJ6WjemIAiC44IuLq2ow%3D%3D; CP_USERINFO=4Gkk4uas%2FGU6V4cAn8Kr14YtZHaRsQ3bb0iKxhYvuaLYLT-rPEFbvbaQzjvqSKm2v8Fd1lQ14weg0PM1aAxGqjzFStaNWwdXEhS3Zzs0jusNqPIZSkWIUHBpa7NyrsBUv2O8QVvh3O4yqW9wAjnfpw%3D%3D; china_variable=jpEe7N32pYz8SAjCjL8fnh2eLZiI1D/EC6dYmS6/lLUOPrHJGj-IxLIHbACvhNcaC9z3Z8pi2hy0JtYoQGGXmsutg32di8lhAZaSKKJ8BFBt-lJZl7B3R-LY1hWhKpza; lastlogintime="17:42:14"'
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