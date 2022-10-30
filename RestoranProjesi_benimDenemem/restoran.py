

masalar={}
yemek={}

def yemekEkle():
    dosya = open("menu.txt", "a", encoding="utf-8")
    yemekIsmi=input("Yemek ismi giriniz : ")
    yemekFiyati=input("Yemek fiyatını giriniz : ")
    if yemekIsmi in yemek.keys():
        print("bu yemek menüde bulunmaktadır.")
    else:
        yemek[yemekIsmi]=yemekFiyati
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




def siparis(masalar):
    masalariGoruntule()
    masa_no=input("Masa numaranızı giriniz : ")
    masalar[masa_no] = {}
    while True:
        print("""
    1-Yeni sipariş gir
    2-Masadaki siparişleri görüntüle
    3-Ana menüye dön""")
        secim = input("seçiminizi giriniz : ")
        if secim == "1":
            menü_listesi = []
            for i in yemek.keys():
                menü_listesi.append(i)
            print(menü_listesi)

            siparis=input("sipariş etmek istediğiniz yemeğin ismini giriniz : ")
            masalar[masa_no][menü_listesi[siparis]] = {}


        elif secim == "2":
            t = 0
            for i in masalar[masa_no][siparis]:
                t += 1
                print("{}. {} ".format(t, i))
            #siparis_goster(masa_no)
            #a=0
            #for i in masalar[masa_no].items():
                #a += 1
                #print("{}. {:<3} Adet {}".format(a,i[1],i[0]))
                #masalar[masa_no]=siparis
        elif secim == "3":
            break
        else:
            print("Yanlış değer girdiniz, tekrar deneyiniz")




def siparisIptalEtme():
    pass

def hesap_goster(masa_no):
    for i in masalar[masa_no]["hesap"].items():
        print("{}. {}".format(i[0], i[1]))
def siparis_goster(masa_no):
    for i in masalar[masa_no][siparis].items():
        print("{}. {}".format(i[0], i[1]))
def hesapOdeme():
    pass

for i in range(1,11):
    masalar[i] = 0


def masalariGoruntule():
    print("Restoranttaki mevcut masalar : ")
    for i in masalar:
        print("{}. Masa".format(i))



def main():
    #isim = input("isminizi giriniz : ").upper()
    #soyisim = input("soyisminizi giriniz: ").upper()
    yemekKontrolu()
    print("Merhaba ")
    #print("Merhaba Sayın "+ isim+ " "+ soyisim)
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
            siparis(masalar)
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