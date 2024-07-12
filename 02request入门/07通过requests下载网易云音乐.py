import requests

url = 'https://m701.music.126.net/20240710170204/ae8af1ddd9066fbd5e8a445da7b2e205/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/29646048469/76ce/dbee/5866/cfb28b91404bc315224491f21dc1e850.m4a'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
with open('01.m4a', 'wb') as f:
    f.write(response.content)
