


yemek={}

def yemekEkle():
    dosya = open("menu.txt", "a", encoding="utf-8")
    while True:
        print("""
        1-Menüyü Göster
        2-Yemek Ekle
        3-Ana Menüye Dön""")
        secim=input("seçiminiz : ")
        if secim == "1":
            a=0
            with open("menu.txt") as dosya:
                for i in dosya:
                    a+=1
                    print(dosya.readlines())
                dosya.close()
        elif secim == "2":
            yemekIsmi=input("Yemek ismi giriniz : ")
            yemekFiyati=input("Yemek fiyatını giriniz : ")
            dosya.write(yemekIsmi+" "+yemekFiyati+"\n")
        elif secim == "3":
            break
    dosya.close()

def yemekKontrolu():
    with open("menu.txt") as dosya:
        bilgiler=dosya.readlines()
        for satir in bilgiler:
            satir=satir.replace("\n","")
            satir=satir.split(" ")
            yemekler=satir[0]
            fiyatlar=satir[1]
            yemek[yemekler]=fiyatlar

def menu():
    yemekEkle()
    for i in yemek.items():
        print("Yemek İsmi : {:<10}, Fiyatı : {}".format(i[0],i[1]))

def siparis():
    pass


def siparisGoruntule():
    pass


def siparisIptalEtme():
    pass


def hesapOdeme():
    pass

def masalariGoruntule():
    pass

isim=""
soyisim=""
def kayit():
    isim=input("isminizi giriniz : ")
    soyisim = input("soyisminizi giriniz: ")


def main():
    kayit()
    print("Merhaba Sayın "+ isim+ " "+ soyisim)
    print("***** Python Restorana Hoş Geldiniz *****")
    while True:
        print("""
    1-Menü
    2-Sipariş
    3-Spariş Görüntüle
    4-Sipariş İptal Etme
    5-Hesap Ödeme
    6-Masaları Goruntule
    7-Çıkış""")
        secim=input("Seçimizi giriniz : ")
        if secim == "1":
            menu()
        elif secim == "2":
            siparis()
        elif secim == "3":
            siparisGoruntule()
        elif secim == "4":
            siparisIptalEtme()
        elif secim == "5":
            hesapOdeme()
        elif secim == "6":
            masalariGoruntule()
        elif secim == "7":
            quit()
        else:
            print("Yanlış değer girdiniz. Tekrar deneyiniz.")



main()