import requests, json

ACCESS_TOKEN = ''

url = 'https://graph.facebook.com/v3.0/me?fields=likes&access_token={}'.format(ACCESS_TOKEN)
data = json.loads(requests.get(url).text)
for d in data['likes']['data']:
    print(d)