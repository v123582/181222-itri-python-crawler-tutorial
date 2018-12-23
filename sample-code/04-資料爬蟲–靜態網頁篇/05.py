url = 'https://gas.goodlife.tw'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")

print(soup.find(class_="main").text.replace(' ', '').replace('\n', ''))