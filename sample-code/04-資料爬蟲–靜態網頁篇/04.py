from bs4 import BeautifulSoup

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html5lib")

print(soup.find(class_="release_movie_name").find(class_="gabtn").text.replace(' ', '').replace('\n', ''))

for d in soup.find_all(class_="release_movie_name"):
    print(d.find(class_="gabtn").text.replace(' ', '').replace('\n', ''))