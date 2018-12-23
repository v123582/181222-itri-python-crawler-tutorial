from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

browser = webdriver.Chrome(executable_path='chromedriver')

browser.get("http://taqm.epa.gov.tw/taqm/tw/MonthlyAverage.aspx")

selectSite = Select(browser.find_element_by_id("ctl04_ddlSite"))
selectSite.select_by_value('29')
selectYear = Select(browser.find_element_by_id("ctl04_ddlYear"))
selectYear.select_by_value('2013')

browser.find_element_by_id('ctl04_btnQuery').click()

# 取得資料
html_source = browser.page_source

soup = BeautifulSoup(html_source, 'html.parser')
table = soup.find('table', class_='TABLE_G')
print(table)

# 關閉瀏覽器
browser.quit();
