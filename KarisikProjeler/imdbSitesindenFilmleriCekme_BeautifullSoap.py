from bs4 import BeautifulSoup
import requests
import lxml

url="https://www.imdb.com/chart/top"

requests = requests.get(url)

soup = BeautifulSoup(requests.content,"lxml") # bütün html dosyasını getirir, istediğimizi almak için parse ederiz

top_250 = soup.find("tbody", attrs={"class":"lister-list"}).find_all("tr")

film_sira = 1

for film in top_250:
    adi = film.find("td", attrs={"class":"titleColumn"}).a.text
    yili = film.find("td", attrs={"class":"titleColumn"}).span.text
    puan = film.find("td", attrs={"class":"ratingColumn imdbRating"}).strong.get("title")

    print("film sıra : ", film_sira)
    print("film adı : ", adi)
    print("film yılı : ", yili)
    print("film puan : ", puan)

    print("\n\n")
    film_sira += 1


