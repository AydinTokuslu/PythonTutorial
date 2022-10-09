

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

miktar = 0
kasa = 5000


def urunSilme(urun):
    silinecekUrun = input("Lütfen silmek istediğiniz ürün ismini giriniz: ")
    if silinecekUrun in urun:
        urun.pop(silinecekUrun)
        urunMiktar.pop(silinecekUrun)
        print("Ürün başarı ile silindi")
        urunListeleme(urun)
    else:
        print("Markette böyle bir ürün bulunmamaktadır. Tekrar seçim yapınız.")

def yeniUrunGirisi(urun, urunMiktar, kasa):
    yeniUrun = input("Lütfen yeni giriş yapılacak ürün ismini giriniz : ")
    yeniUrunMiktar= int(input("Lütfen ürün miktarını giriniz : "))
    yeniUrunFiyat= int(input("Lütfen ürün fiyatını giriniz : "))
    urun[yeniUrun] = yeniUrunFiyat
    urunMiktar[yeniUrun] = yeniUrunMiktar
    print("Giriş yapılan yeni {} için ödenecek para miktarı : {}'tldir.".format(yeniUrun, yeniUrunMiktar * yeniUrunFiyat))
    kasa -= (yeniUrunMiktar * yeniUrunFiyat)
    print("Kasadaki para miktarı : {}'tldir.".format(kasa))
    urunMiktariniGosterme(urunMiktar)


def urunStokGirisi(urun, urunMiktar, kasa):
    gelenUrun = input("Lütfen stok girişi yapılacak ürün ismini giriniz: ")
    miktar = int(input("Lütfen stok girişi yapılacak ürün miktarını giriniz : "))
    if gelenUrun in urun:
        urunMiktar[gelenUrun] += miktar
        urunMiktariniGosterme(urunMiktar)
        print("Giriş yapılan {} için ödenecek para miktarı : {}'tldir.".format(gelenUrun, miktar * urun[gelenUrun]))
        kasa -= (miktar * urun[gelenUrun])
        print("Kasadaki para miktarı : {}'tldir.".format(kasa))
    else:
        print("Markette böyle bir ürün bulunmamaktadır. Tekrar seçim yapınız.")

def urunListeleme(urun):
    for i in urun.items():
        print("""{:<10} ----   ücreti : |{:^8}| """.format(i[0], i[1]))


def urunMiktariniGosterme(urunMiktar):
    for i in urunMiktar.items():
        print("""{:<10} ----   miktarı : |{:^8}| """.format(i[0], i[1]))


def urunSatinAlma(urun, kasa):
    satinAlinacakUrun = input("Lütfen satın almak istediğiniz ürünün ismini giriniz : ")
    miktar = int(input("Lütfen satın almak istediğiniz miktarı giriniz : "))
    if satinAlinacakUrun in urun:
        urunMiktar[satinAlinacakUrun] -= miktar
        urunListeleme(urun)
        print("""
{} ürününden {} kilo satın aldınız. Ödeyeceğiniz tutar : {}""".format(satinAlinacakUrun, miktar, miktar*urun[satinAlinacakUrun]))
        kasa += (miktar * urun[satinAlinacakUrun])
        print("Kasadaki para miktarı : {}'tldir.".format(kasa))
        urunMiktariniGosterme(urunMiktar)
    else:
        print("Markette böyle bir ürün bulunmamaktadır. Tekrar seçim yapınız.")
while True:
    print(menu)
    secim = int(input("Lütfen seçiminizi giriniz : "))
    if secim == 1:
        urunListeleme(urun)
    elif secim == 2:
        urunSatinAlma(urun, kasa)
    elif secim == 3:
        urunMiktariniGosterme(urunMiktar)
    elif secim == 4:
        urunStokGirisi(urun, urunMiktar, kasa)
    elif secim == 5:
        yeniUrunGirisi(urun, urunMiktar, kasa)
    elif secim == 6:
        urunSilme(urun)
    elif secim == 7:
        quit()