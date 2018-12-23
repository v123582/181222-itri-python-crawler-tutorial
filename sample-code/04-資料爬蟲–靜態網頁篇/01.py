import requests

url = 'https://www.aicoin.net.cn/'
r = requests.get(url)
print(r.text)

url = 'https://www.aicoin.net.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
r = requests.get(url, headers=headers)
print(r.text[0:100])
