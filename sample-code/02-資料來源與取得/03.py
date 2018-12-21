import requests
# 引入函式庫
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r = requests.get('https://www.dcard.tw/_api/forums/job/posts?popular=true', headers=headers)
# 想要爬資料的目標網址
response = r.text
# 模擬發送請求的動作

import json
data = json.loads(response)

for d in data:
    print(d['title'])