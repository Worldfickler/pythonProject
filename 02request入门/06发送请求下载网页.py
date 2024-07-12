import requests

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

with open("baidu.html", "w", encoding="utf8") as f:
    f.write(response.content.decode('utf-8'))
