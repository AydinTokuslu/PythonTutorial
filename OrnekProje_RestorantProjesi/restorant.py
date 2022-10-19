


masalar = {}
yemek = {}
for i in range(1,21):
    masalar[i]=0

def masalari_goruntule():
    for i in range(1, 21):
        print("{}. masa hesabı : {}".format(i, masalar[i]))


def hesap_ekle():
    masa_no=int(input("Masa numarasını giriniz : "))
    ucret = float(input("Ücreti giriniz : "))
    toplam = masalar[masa_no] + ucret
    masalar[masa_no] = toplam


def hesap_ode():
    masa_no = int(input("Masa numarasını giriniz : "))
    ucret = float(input("Ücreti giriniz : "))
    toplam = masalar[masa_no] + ucret
    if toplam >= 0:
        masalar[masa_no] = toplam
    else:
        print("Hatalı işlem yaptınız")

def yemek_kontrol():
    with open("yemek.txt") as dosya:
        bilgiler = dosya.readlines()
        for satir in bilgiler:
            satir = satir.replace("\n","")
            satir = satir.split(" ")
            yemekler = satir[0]
            ucretler = satir[1]
            yemek[yemekler] = ucretler
        print(yemekler)

def hesap_kontrolu(dosya_adi):
    try:
        dosya = open(dosya_adi)
        bilgiler=dosya.read()
        bilgiler = bilgiler.split("\n")
        bilgiler.pop()
        dosya.close()
        flag=True
    except FileNotFoundError:
        dosya = open(dosya_adi,"w")
        dosya.close()
        print("yeni dosya oluşturuldu")
        flag=False
    if flag:
        for i in enumerate(bilgiler):
            masalar[i[0]] = float(i[1])
    else:
        pass

def guncelle():
    dosya=open("restorant.txt","w")
    dosya.write("0")
    for i in range(1,21):
        ücret=masalar[i]
        ücret =str(ücret)
        dosya.write("\n"+ücret)
    dosya.close()

def yemek_dosyasi():
    dosya = open("yemek.txt","a")

    while True:
        print("""
        1-Yemek ekle
        2- Ana menüye dön""")
        secim = input("seçiminiz : ")
        if secim == "1":
            yemek_ismi = input("Eklemek istediğiniz yemek adını giriniz : ")
            yemek_ucreti = input("Yemeğin ücreti ne kadar? : ")
            dosya.write(yemek_ismi+" "+yemek_ucreti+"\n")
        elif secim == "2":
            break
    dosya.close()

def menu_goster():
    for i in yemek.items():
        print("Yemek ismi : {:<10}, Ücreti : {}".format(i[0],i[1]))

def ana_fonksiyon():
    hesap_kontrolu("restorant.txt")
    while True:
        yemek_kontrol()
        guncelle()
        print("""
1-Masaları Görüntüle
2-Hesap Ekle
3-Hesap Öde
4-Yemek Ekle
5-Menüyü Göster
6-Çıkış""")
        secim=input("Seçiminizi yapınız : ")
        if secim == "1":
            masalari_goruntule()
        elif secim == "2":
            hesap_ekle()
        elif secim == "3":
            hesap_ode()
        elif secim == "4":
            yemek_dosyasi()
        elif secim == "5":
            menu_goster()
        elif secim == "6":
            quit()

ana_fonksiyon()