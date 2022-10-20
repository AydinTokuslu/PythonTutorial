urun = {"Domates": 2.10,
        "Patates" : 3.20,
        "Biber": 1.50,
        "Sogan" : 2.30,
        "Havuc" : 3.10,
        "Elma" : 1.20,
        "Muz" : 1.90,
        "Cilek" : 6.10,
        "Kavun" : 4.30,
        "Uzum" : 2.70,
        "Limon" : 0.50}

urunMiktar={"Domates": 100,
        "Patates" : 100,
        "Biber": 100,
        "Sogan" : 100,
        "Havuc" : 100,
        "Elma" : 100,
        "Muz" : 100,
        "Cilek" : 100,
        "Kavun" : 100,
        "Uzum" : 100,
        "Limon" : 100}

menu = """
1- Urun Listeleme
2- Urun Satın Alma
3- Ürün Miktarını Gösterme
4- Urun Stok Girişi
5- Yeni Ürün Girişi
6- Ürün Silme
7- Çıkış
"""

kasa = 5000

def urunListeleme(urun):
        for i in urun.keys() and urun.items():
                print("""{:<10} ----   ücreti : |{:^8}| """.format(i[0], i[1]))



def urunSatinAlma(urun,kasa):
        urunListeleme(urun)
        satinAlinacakUrun=input("Satın almak istediğiniz ürünü giriniz : ")
        satinAlinacakMiktar=int(input("Satın almak istediğiniz miktarı giriniz : "))
        if satinAlinacakUrun in urun:
                urunMiktar[satinAlinacakUrun]-=satinAlinacakMiktar
                urunListeleme(urun)
                print("""
{} ürününden {} kilo satın aldınız. Ödeyeceğiniz tutar : {} tldir.""".format(satinAlinacakUrun,satinAlinacakMiktar, urun[satinAlinacakUrun]*satinAlinacakMiktar))
                kasa+=urun[satinAlinacakUrun]*satinAlinacakMiktar
                print("kasadaki para miktarı : {}".format(kasa))
                urunMiktariniGosterme(urunMiktar)
        else:
                print("Markette böyle bir ürün bulunmamaktadır. Tekrar tercih yapınız.")


def urunMiktariniGosterme(urunMiktar):
        for i in urunMiktar.keys() and urunMiktar.items():
                print("""{:<10} ----   miktarı : |{:^8}| """.format(i[0], i[1]))


def urunStokGirisi(urun,urunMiktar,kasa):
        urunListeleme(urun)
        gelenUrun=input("Lütfen stok girişi yapılacak ürünü giriniz : ")
        gelenMiktar=int(input("Lütfen stok girişi yapılacak ürün miktarını giriniz : "))
        if gelenUrun in urun:
                urunMiktar[gelenUrun]+=gelenMiktar
                urunMiktariniGosterme(urunMiktar)
                print("Giriş yapılan {} ürününe {} kilo için ödenecek para : {}".format(gelenUrun,gelenMiktar,urun[gelenUrun]*gelenMiktar))
                kasa -= urun[gelenUrun]*gelenMiktar
                print("kasadaki para miktarı : {}".format(kasa))
        else:
                print("Markette böyle bir ürün bulunmamaktadır. Tekrar tercih yapınız.")



def yeniUrunGirisi(urun,urunMiktar,kasa):
        yeniUrun=input("Yeni ürün ismini giriniz : ")
        yeniUrunMiktar=int(input("Yeni ürün miktarını giriniz : "))
        yeniUrunFiyat=int(input("Yeni ürün fiyatını giriniz : "))
        urun[yeniUrun]=yeniUrunFiyat
        urunMiktar[yeniUrun]=yeniUrunMiktar
        print("Giriş yapılan yeni {} ürünü için ödenecek para : {}tldir.".format(yeniUrun, yeniUrunMiktar * yeniUrunFiyat))
        kasa -= (urun[yeniUrun]*yeniUrunMiktar)
        print("kasadaki kalan para miktarı : {}tldir.".format(kasa))
        urunMiktariniGosterme(urunMiktar)

def urunSilme(urun):
        silinecekUrun=input("Silmek istediğiniz ürün ismi giriniz : ")
        if silinecekUrun in urun:
                urun.pop(silinecekUrun)
                urunMiktar.pop(silinecekUrun)
                print("ürün başarı ile silindi")
                urunListeleme(urun)
        else:
                print("Böyle bir ürün bulunmamaktadır.")


while True:
        print(menu)
        secim=int(input("yapmak istediğiniz secimi giriniz : "))
        if secim == 1:
                urunListeleme(urun)
        elif secim == 2:
                urunSatinAlma(urun,kasa)
        elif secim == 3:
                urunMiktariniGosterme(urunMiktar)
        elif secim == 4:
                urunStokGirisi(urun,urunMiktar,kasa)
        elif secim == 5:
                yeniUrunGirisi(urun,urunMiktar,kasa)
        elif secim == 6:
                urunSilme(urun)
        elif secim == 7:
                quit()
