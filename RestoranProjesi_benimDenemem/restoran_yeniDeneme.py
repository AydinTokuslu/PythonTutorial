
masalar={}
yemek={}


def menu():
    print("Yemek çeşitleri : ")
    a = 0
    for i in yemek.items():
        a += 1
        print("{}. Yemek İsmi : {:<10}, Fiyatı : {}".format(a, i[0], i[1]))


def yemekEkle():
    dosya=open("yemek_menu.txt","a",encoding="utf-8")
    yemek_ismi=input("Eklemek istediğiniz yemek isminiz giriniz : ").upper()
    yemekFiyati = int(input("Yemek fiyatını giriniz : "))
    yemek[yemek_ismi]={}
    yemek[yemek_ismi]=yemekFiyati
    print("yemek ekleme işlemi başarılı")
    dosya.write(yemek_ismi+" = "+str(yemekFiyati)+"\n")
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


def siparisGir(masalar):
    masa_no=input("lütfen masa numaranızı giriniz : ")
    masalar[masa_no]={}
    menü_listesi = ["DONER", "KEBAP", "PATATES", "MAKARNA", "LAHMACUN", "HAMBURGER"]
    #for i in yemek.keys():
     #   menü_listesi.append(i)
    #print(menü_listesi)
    a = 0
    for i in menü_listesi:
        a += 1
        print("{} - {}".format(a, i))
    siparisNo=int(input("sipariş numaranızı giriniz : "))-1
    masalar[masa_no][menü_listesi[siparisNo]]=0
    siparisAdet=int(input("kaç adet sipariş vermek istiyorsunuz : "))
    masalar[masa_no][menü_listesi[siparisNo]] += siparisAdet
    print("siparişiniz başarıyla kaydedilmiştir.")

def siparis_goruntule():
    masa_no = input("lütfen masa numaranızı giriniz : ")
    for i in masalar[masa_no].items():
        print("{} Nolu Masanın Siparişi : {}, Adedi : {}".format(masa_no,i[0], i[1]))


def siparis_listele():
    masa_no = input("lütfen masa numaranızı giriniz : ")
    t=0
    for i in masalar:
        t+=1
        print("{:>15}   :  {}".format(i[0], i[1]))


def siparisIptalEtme():
    pass


def hesapOdeme():
    pass


def masalariGoruntule():
    masa_no = input("masa numaranızı giriniz : ")
    masalar[masa_no] = {}
    for i in range(1, 11):
        print("{}. Masa = Siparişi : {} ".format(i,masalar[masa_no]))




#def masa_sec():

    #print("masa seçme işlemi başarılı")


def siparisGoruntule(masalar):
    while True:
        print("""
    1-Sipariş Gir
    2-Sipariş Goruntule
    3-Sipariş Listele
    4-Ana Menü""")
        sec=input("seçiminizi giriniz : ")
        if sec == "1":
            siparisGir(masalar)
        elif sec == "2":
            siparis_goruntule()
        elif sec == "3":
            siparis_listele()
        elif sec == "4":
            break
        else:
            print("hatalı işlem girdiniz.")


def main():
    #isim = input("isminizi giriniz : ").upper()
    #soyisim = input("soyisminizi giriniz: ").upper()
    
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
            siparisGoruntule(masalar)
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