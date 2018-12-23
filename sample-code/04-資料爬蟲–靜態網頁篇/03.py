url = 'https://www.dcard.tw/f'
r = requests.get(url)
r.encoding = 'utf-8'
print(r.text)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url = 'https://www.dcard.tw/f'
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'
print(r.text)