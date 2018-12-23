url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm'
r = requests.get(url)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, "html5lib")

print(soup.find(id="ftext").text)
for d in soup.find(class_="FcstBoxTable01").find_all('tr'):
    print(d.text)