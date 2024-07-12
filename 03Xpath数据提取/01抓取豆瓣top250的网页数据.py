import requests

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

with open('douban.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode('utf-8'))