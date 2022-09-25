from bs4 import BeautifulSoup
import requests
import lxml

url="https://www.trendyol.com/sr?fl=encokonecikanurunler"

requests = requests.get(url)

soup = BeautifulSoup(requests.content,"lxml") # bütün html dosyasını getirir, istediğimizi almak için parse ederiz

top_250 = soup.find("div", attrs={"class":"prdct-cntnr-wrppr"}).find_all("div")

urun_sira = 1

for film in top_250:
    adi = film.find("div", attrs={"class":"prdct-desc-cntnr-ttl-w two-line-text"}).link.text    #yili = film.find("td", attrs={"class":"titleColumn"}).span.text
    #puan = film.find("td", attrs={"class":"ratingColumn imdbRating"}).strong.get("title")

    print("ürün sıra : ", urun_sira)
    print("ürün adı : ", adi)
    #print("ürün yılı : ", yili)
    #print("ürün puan : ", puan)

    print("\n\n")
    urun_sira += 1
