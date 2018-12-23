import json

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,ja;q=0.5',
    'Connection': 'keep-alive',
    'Cookie': 'luauid=2108599161; _ga=GA1.3.696827056.1517415692; __auc=ed4a51af1614d05f6d120b43bfb; PERSONAL_SORT=B; SYS_SETAB=20140613; _T_MYPOOL_104I=3; 104i_viewJobJobHistory=%5B%224nm6l%22%2C%223i8q6%22%5D; _gid=GA1.3.516194520.1528488749; __asc=bb64e596163e2c7db70da629853; lup=2108599161.5057323988685.4690104285048.1.4507568175053; lunp=4690104285048',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'www.104.com.tw',
    'Referer': 'https://www.104.com.tw/cust/list/index/'
}
url = 'https://www.104.com.tw/cust/list/ajax/index?page=2&keyword=%E8%A1%8C%E9%8A%B7&area=6001001000,6001002000&order=1&mode=s&jobsource=checkc'
r = requests.get(url, headers=headers)
r.encoding = 'utf-8'

data = json.loads(r.text)['data']['list']
for d in data:
    print(d['c'], d['custName'])
