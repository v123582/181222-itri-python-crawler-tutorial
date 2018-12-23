from selenium import webdriver # pip install selenium
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

browser = webdriver.Chrome(executable_path='chromedriver')
# https://sites.google.com/a/chromium.org/chromedriver/downloads

browser.get("http://rdc28.cwb.gov.tw/TDB/ntdb/pageControl/typhoon")

html_source = browser.page_source
soup = BeautifulSoup(html_source, 'html.parser')
table = soup.find('table', class_='tyde_t')
print(table)
browser.quit();

url = 'http://rdc28.cwb.gov.tw/TDB/ctrl_typhoon_list/get_typhoon_list_table/'
r = requests.post(url, data={'year': 'all', 'model': 'all'})

soup = BeautifulSoup(r.text, "html5lib")

for d in soup.find('table').find_all('tr')[2:]:
    print(d.find_all('td')[2].text, d.find_all('td')[4].text)
