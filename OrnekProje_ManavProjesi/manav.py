a = {"elma":0,
     "armut":0,
     "portakal":0,
     "mandalina":0,
     "muz":0,
     "ıspanak":0
     }

menu = """
1- Urun Stok Ekle
2- Urun Stok Çıkar
3- Urun Miktarını Goster
4- Tüm listeyi gör
5- Yeni Ürün Stok Ekle
6- Urun Sil
7- Kasadaki Parayı Gör
8- Çıkış
"""


def cikar(urun:str, miktar:int):
     a[urun] -= miktar

def listeGor(a):
     for i in a.items():
          print("""
          {:^15} ---- miktarı : |{:^15}|""".format(i[0], i[1]))

def ekle(urun:str, miktar:int):
     a[urun] += miktar
     print("Ekleme işlemi tamamlandı")

def goster(urun:str):
     print(a[d])

kasa=10000
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

               bos_alan = toplam_miktar - a[b]
               if toplam_miktar > 1000 :
                    print("Elimizde bu kadar boş alan yoktur.\nAlabileceğimiz {} miktarı : {}".format(b,bos_alan))
               else:
                    kasa -= (c * 2)
                    print("{} Lira alacaksınız".format(c * 2))
                    ekle(b,c)
          else:
               print("Bu ürün elimizde bulunmamaktadır.")
     elif secim == "2":
          print("-------- Meyveler---------")
          listeGor(a)

          b = input("Hangi meyveyi alacaksınız : ")
          if b in a.keys():
               c = int(input("Kaç kilo alacaksınız : "))
               if c <= a[b]:
                    kasa += (c*2)
                    print("{} Lira vereceksiniz".format(c * 2))
                    cikar(b, c)
                    print("""İstediğiniz {} ürünü {} kilo olarak çıkış yapılmıştır.
                    Elimizde kalan {} miktarı : {}""".format(b,c,b,a[b]))
               else:
                    print("""Elimizde yeterince {} bulunmamaktadır. 
                    Elimizdeki {} miktarı : {}""".format(b,b,a[b]))
          else:
               print("Bu ürün elimizde bulunmamaktadır.")
     elif secim == "3":
          d = input("Hangi meyveyi görmek istiyorsunuz : ")
          if d in a.keys():
               goster(d)
          else:
               print("Bu ürün elimizde bulunmamaktadır.")
     elif secim == "4":
          listeGor(a)
     elif secim == "5":
          b = input("Hangi meyveyi ekleyeceksiniz : ")
          c = int(input("Kaç kilo ekleyeceksiniz : "))
          a[b] = c
     elif secim == "6":
          b = input("Hangi meyveyi silmek istiyorsunuz : ")
          a.pop(b)
          print("Ürün başarıyla silindi")
     elif secim == "7":
          print("Kasadaki para miktarı : {}".format(kasa))
     elif secim == "8":
          quit()
     else:
          print("Böyle bir işlem bulunmamaktadır.")

