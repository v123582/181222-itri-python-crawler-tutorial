# 下載檔案

import urllib.request
import zipfile 
res = "http://opendata.cwb.gov.tw/govdownload?dataid=F-D0047-093&authorizationkey=rdec-key-123-45678-011121314"
urllib.request.urlretrieve(res,"./data/F-D0047-093.zip")
f = zipfile.ZipFile('./data/F-D0047-093.zip')
f.extractall('./data')

# 讀檔案

fh = open("./data/64_72hr_CH.xml", "r")
xml = fh.read()
fh.close()

# 解析檔案內容

import xmltodict
d = dict(xmltodict.parse(xml))

locations = d['cwbopendata']['dataset']['locations']['location']
location = locations[0]
print(location['locationName'])
print(location['weatherElement'][0]['time'][0]['dataTime'])
print(location['weatherElement'][0]['time'][0]['elementValue'])
print(location['weatherElement'][0]['time'][1]['dataTime'])
print(location['weatherElement'][0]['time'][1]['elementValue'])