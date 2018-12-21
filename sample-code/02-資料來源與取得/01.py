# 下載檔案
import urllib.request
import zipfile 
res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
urllib.request.urlretrieve(res, './data/51.csv')

# 讀檔案
fh = open("./data/51.csv", newline='')
f = fh.read()
fh.close()

# 解析檔案內容
import csv
reader = csv.reader(f.split('\n'), delimiter=',')
for row in reader:
    print(row)
    
# 開啟 CSV 檔案
with open('./data/51.csv', newline='') as csvfile:
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  # 以迴圈輸出每一列
  for row in rows:
    print(row)