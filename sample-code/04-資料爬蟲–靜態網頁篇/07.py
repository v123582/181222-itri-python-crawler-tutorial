url = 'https://www.ettoday.net/news/news-list.htm'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

for d in soup.find(class_="part_list_2").find_all('h3'):
    print(d.find(class_="date").text, d.find_all('a')[-1].text)
