url = 'https://www.104.com.tw/cust/list/ajax/index?page=2&keyword=%E8%A1%8C%E9%8A%B7&area=6001001000,6001002000&order=1&mode=s&jobsource=checkc'
r = requests.get(url)
r.encoding = 'utf-8'
print(r.text)