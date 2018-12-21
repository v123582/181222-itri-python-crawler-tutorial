import requests
import time

TWSE_URL = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'

stock_id = '2330'
current_date = time.strftime('%Y%m%d')
current_year = time.strftime('%Y')
current_month = time.strftime('%m')
resp = requests.get(TWSE_URL + '&date=' + current_date + '&stockNo=' + stock_id)
data = json.loads(resp.text)
print(data)