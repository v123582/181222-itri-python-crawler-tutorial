#練習：一個網址的結構大概如圖所示，試著用 Python 分別把每個值取出來。

url = 'https://www.trivago.com.tw:3000/search#taipei'

# __________

print('protocol : %s' % (protocol)) # https
print('domain : %s' % (domain)) # www.trivago.com.tw:
print('port : %s' % (port)) # 3000
print('path : %s' % (path)) # search
print('fragment : %s' % (fragment)) # taipei