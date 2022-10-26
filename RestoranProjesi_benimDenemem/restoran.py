

masalar={}
yemek={}

def yemekEkle():
    dosya = open("menu.txt", "a", encoding="utf-8")
    yemekIsmi=input("Yemek ismi giriniz : ")
    yemekFiyati=input("Yemek fiyatını giriniz : ")
    dosya.write(yemekIsmi+" "+yemekFiyati+"\n")
    dosya.close()
def menuGoster():
    while True:
        print("""
            1-Menüyü Göster
            2-Yemek Ekle
            3-Ana Menüye Dön""")
        secim = input("seçiminiz : ")
        if secim == "1":
            menu()
        elif secim == "2":
            yemekEkle()
        elif secim == "3":
            break

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
    a=0
    for i in yemek.items():
        a+=1
        print("{}. Yemek İsmi : {:<10}, Fiyatı : {}".format(a,i[0],i[1]))

def siparis():

    masa_no=int(input("Masa numaranızı giriniz : "))
    while True:
        print("""
    1-Yeni sipariş gir
    2-Masadaki siparişleri görüntüle
    3-Ana menüye dön""")
        secim = input("seçiminizi giriniz : ")
        if secim == "1":
            menu()
            siparis=input("sipariş etmek istediğiniz yemeğin numarasını giriniz : ")
            y=0
            for i in yemek.items():
                y+=1
                if y==siparis:
                    siparisAdet=int(input("kaç adet sipariş vermek istiyorsunuz? : "))
                    toplam=masalar[masa_no]+int(yemek[siparis[0]]*siparisAdet)
                    print(yemek[siparis[0]])
                    masalar[masa_no]["hesap"]=toplam
        elif secim == "2":
            a=0
            for i in masalar[masa_no].items():
                a+=1
                if a != 1:
                    print("{:<3} Adet {}".format(i[1],i[0]))
        elif secim == "3":
            break
        else:
            print("Yanlış değer girdiniz, tekrar deneyiniz")




def siparisIptalEtme():
    pass


def hesapOdeme():
    pass

for i in range(1,11):
    masalar[i]={}

for i in range(1,11):
    masalar[i]["hesap"]=0

def masalariGoruntule():
    for i in range(1,11):
        print("{}. Masa Hesabı : {}".format(i,masalar[i]["hesap"]))


def main():
    isim = input("isminizi giriniz : ").upper()
    soyisim = input("soyisminizi giriniz: ").upper()
    yemekKontrolu()
    print("Merhaba Sayın "+ isim+ " "+ soyisim)
    print("***** Python Restoranta Hoş Geldiniz *****")
    while True:
        print("""
    1-Menü
    2-Sipariş
    4-Sipariş İptal Etme
    5-Hesap Ödeme
    6-Masaları Goruntule
    7-Çıkış""")
        secim=input("Seçimizi giriniz : ")
        if secim == "1":
            menuGoster()
        elif secim == "2":
            siparis()
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