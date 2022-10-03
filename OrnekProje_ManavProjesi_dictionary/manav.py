a = {"elma":0,
     "armut":0,
     "portakal":0,
     "mandalina":0,
     "muz":0,
     "ıspanak":0}

urun_ucreti = {"elma":1.25,
     "armut":3.75,
     "portakal":2.50,
     "mandalina":2.25,
     "muz":6.50,
     "ıspanak":4.25}

menu = """
1- Urun Stok Ekle
2- Urun Satın Al
3- Urun Miktarını Goster
4- Tüm listeyi gör
5- Yeni Ürün Stok Ekle
6- Urun Sil
7- Yönetici Girişi
8- Çıkış
"""


def cikar(urun:str, miktar:int):
     a[urun] -= miktar
     print("ürün çıkarma işlemi tamamlandı")


def listeGor(a):
     x = 0
     for i in a.items():
          x += 1
          if x == 1:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 1:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 2:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 2:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 3:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 3:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 4:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 4:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 5:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 5:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 6:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 6:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 7:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 7:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 8:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 8:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 9:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 9:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))
          elif x == 10:
               y = 0
               for t in urun_ucreti.items():
                    y += 1
                    if y == 10:
                         print("""
                    {:<15} ---- miktarı : |{:^15}| ücreti : {}""".format(i[0], i[1], t[1]))


def ekle(urun:str, miktar:int):
     a[urun] += miktar
     print("Ekleme işlemi tamamlandı")

def goster(urun:str):
     print(a[d])

kasa=10000
sifre="1234"

while True:

     print(menu)
     secim = input("seçiminizi yapınız : ")

     if secim == "1":
          print("-------- Meyveler---------")
          listeGor(a)
          b = input("Hangi meyve getirildi : ")
          if b in a.keys():
               c = int(input("Kaç kilo getirdiniz : "))
               toplam_miktar= a[b] + c

               bos_alan = 5000 - a[b]
               if toplam_miktar > 5000 :
                    print("Elimizde bu kadar boş alan yoktur.\nAlabileceğimiz {} miktarı : {}".format(b,bos_alan))
               else:
                    if (c*urun_ucreti[b]) < kasa:
                         kasa -= (c * urun_ucreti[b])
                         print("{} Lira alacaksınız".format(c * urun_ucreti[b]))
                         ekle(b,c)
                    else:
                         print("kasada bu kadar para bulunmamaktadır.")
                         print("Elimizdeki para miktarı : {} tldir.".format(kasa))

          else:
               print("Bu ürün elimizde bulunmamaktadır.")
     elif secim == "2":
          print("-------- Meyveler---------")
          listeGor(a)

          b = input("Hangi meyveyi alacaksınız : ")
          if b in a.keys():
               c = int(input("Kaç kilo alacaksınız : "))
               if c <= a[b]:
                    kasa += (c*urun_ucreti[b])
                    print("{} Lira vereceksiniz".format(c * urun_ucreti[b]))
                    cikar(b, c)
                    print("""İstediğiniz {} ürünü {} kilo olarak çıkış yapılmıştır.
                    Elimizde kalan {} miktarı : {} kg""".format(b,c,b,a[b]))
               else:
                    print("""Elimizde yeterince {} bulunmamaktadır. 
                    Elimizdeki {} miktarı : {} kg""".format(b,b,a[b]))
          else:
               print("Bu ürün elimizde bulunmamaktadır.")
     elif secim == "3":
          d = input("Hangi meyveyi görmek istiyorsunuz : ")
          if d in a.keys():
               print("""
               Elimizdeki {} miktarı : {} 
               Kilo fiyatı ise       : {}""".format(d,a[d], urun_ucreti[d]))

          else:
               print("Bu ürün elimizde bulunmamaktadır.")
     elif secim == "4":
          listeGor(a)
     elif secim == "5":
          b = input("Hangi meyveyi ekleyeceksiniz : ")
          c = int(input("Kaç kilo ekleyeceksiniz : "))
          d = int(input("Kilo fiyatını giriniz : "))
          if (c * d) < kasa:
               kasa -= (c * d)
               print("{} Lira alacaksınız".format(c * d))
               a[b] = c
               urun_ucreti[b]=d
               z = 0
               for i in a:
                    z += 1
                    if z == 10:
                         print("Bu ürün ile depo dolmuştur, Başka ürün ekleyemezsiniz")
               print("Stoka yeni ürün ekleme işlemi tamamlandı")
          else:
               print("kasada bu kadar para bulunmamaktadır.")
               print("{} kg ürün alabilirsiniz.".format(kasa/d))
     elif secim == "6":
          b = input("Hangi meyveyi silmek istiyorsunuz : ")
          a.pop(b)
          print("Ürün başarıyla silindi")
     elif secim == "7":
          sifreGir=input("Şifre giriniz :")
          if sifreGir == sifre:
               altmenu = """
          1- Kasadaki parayı gör
          2- Şifreyi değiştir
          """
               print(altmenu)
               sec = input("Seçiminizi yapınız : ")
               if sec == "1":
                    print("Kasadaki para miktarı : {}".format(kasa))
               elif sec == "2":
                   sif = input("Eski şifrenizi giriniz: ")
                   if sif == sifre:
                       sifreYeni = input("Yeni şifrenizi giriniz : ")
                       sifre = sifreYeni
                   else:
                        print("Hatalı giriş yaptınız")
               else:
                    print("Hatalı giriş yaptınız")
          else:
               print("Böyle bir işlem yoktur. Yanlış şifre girdiniz")
     elif secim == "8":
          quit()
     else:
          print("Böyle bir işlem bulunmamaktadır.")

