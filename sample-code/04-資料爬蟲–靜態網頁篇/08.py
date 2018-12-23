url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

for d in soup.find("table").find_all('tr'):
    if d.find('td'):
        print(d.find('td').find(class_="print_show").text.strip().replace('\n', ''))