from bs4 import BeautifulSoup
import requests

url="https://www.amazon.com.tr/gp/bestsellers/electronics/ref=zg_bs_nav_0"

requests = requests.get(url)

soup = BeautifulSoup(requests.content,"lxml") # bütün html dosyasını getirir, istediğimizi almak için parse ederiz

urunTop = soup.find("div", attrs={"class":"a-cardui _cDEzb_card_1L-Yx"}).find_all("div")

urun_sira = 1

for urun in urunTop:
    urunAdi = urun.find("div", attrs={"class":"_cDEzb_p13n-sc-css-line-clamp-3_g3dy1"}).span.text
    urunPuani = urun.find("div", attrs={"class":"a-icon-row"}).a.get("title")
    urunFiyati = urun.find("span", attrs={"class":"_cDEzb_p13n-sc-price_3mJ9Z"}).link.text

    print("ürün sıra : ", urun_sira)
    print("ürün adı : ", urunAdi)
    print("ürün puan : ", urunPuani)
    print("ürün fiyatı : ", urunFiyati)

    print("\n\n")
    urun_sira += 1


    ##OLMADI