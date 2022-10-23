


masalar = {}
yemek = {}
for i in range(1,21):
    masalar[i]={}
for i in range(1,21):
    masalar[i]["hesap"]=0

def menu_goster():
    for i in yemek.items():
        print("Yemek İsmi : {:<10}, Ücreti : {}".format(i[0],i[1]))
def masalari_goruntule():
    for i in range(1, 21):
        print("{}. Masa Hesabı : {}".format(i, masalar[i]["hesap"]))

def hesap_ekle():

    masa_no = int(input("Masa numarasını giriniz : "))
    while True:
        print("""
    1-Yeni sipariş gir
    2-Masadaki Siparişleri Gör
    3-Ana Menüye dön""")
        secim=input("seçiminiz: ")
        if secim == "1":
            print("Yemekler:")#burda bütün menüyü kullanıcıya gösteriyoruz.
            x=0
            for i in yemek:
                x+=1
                print("{}. {}".format(x,i))
            urun = int(input("sipariş etmek istediğiniz ürünün sırasını giriniz : "))
            y=0
            for i in yemek.items():
                y+=1
                if y == urun:
                    miktar=int(input("kaç adet? : "))
                    toplam = masalar[masa_no] + float(yemek[i[0]])*miktar
                    masalar[masa_no]["hesap"] = toplam
                    if i[0] in masalar[masa_no].keys():
                        masalar[masa_no][i[0]] += miktar
                    else:
                        masalar[masa_no][i[0]] = miktar

                else:
                    pass
        elif secim == "2":
            a = 0
            for i in masalar[masa_no].items():
                a += 1
                if a != 1:
                    print("{:<3} Adet {}".format(i[1], i[0]))
        elif secim == "3":
            break

def hesap_cikar():
    masa_no = int(input("Masa numarasını giriniz : "))
    while True:
        print("""
    1-Nakit Çıkar
    2-Ürün Çıkar
    3-Hesabı Sil
    4-Masadaki Siparişleri Gör
    5-Ana Menüye Dön""")
        secim=input("işlemini seçiniz : ")
        if secim == "1":
            ucret = float(input("Ücreti giriniz : "))
            toplam = masalar[masa_no]["hesap"] - ucret
            if toplam >= 0:
                masalar[masa_no]["hesap"] = toplam
            else:
                print("Hatalı işlem yaptınız")
        elif secim == "2":
            print("Yemekler:") #burda bütün menüyü kullanıcıya gösteriyoruz.
            x = 0
            for i in yemek:
                x += 1
                print("{}. {}".format(x, i))
            urun = int(input("Çıkarmak istediğiniz ürünün sırasını giriniz : "))
            y = 0
            for i in yemek.items():
                y += 1
                if y == urun:
                    miktar = float(input("kaç adet? : "))
                    toplam = masalar[masa_no]["hesap"] - miktar*float(yemek[i[0]])
                    if miktar >= int(masalar[masa_no][i[0]]):
                        masalar[masa_no].pop(i[0])
                    else:
                        mevcut = float(masalar[masa_no][i[0]])

                        toplam = mevcut - miktar
                        masalar[masa_no][i[0]] = toplam

                    if toplam >= 0:
                        masalar[masa_no]["hesap"] = toplam
                    else:
                        print("Hatalı işlem yaptınız.")
                else:
                    pass
        elif secim == "3":
            print("Masadaki hesap : {}".format(masalar[masa_no]["hesap"]))
            masalar[masa_no]["hesap"] = 0
            liste = []
            x = 1
            for i in masalar[masa_no].items():
                x += 1
                if x != 1:
                    liste.append(i[0])
                else:
                    pass
            h = 0
            for i in liste:
               masalar[masa_no].pop(i)

        elif secim == "4":
            a = 0
            for i in masalar[masa_no].items():
                a += 1
                if a != 1:
                    print("{:<3} Adet {}".format(i[1], i[0]))
        elif secim == "5":
            break

def yemek_kontrol():
    with open("yemek.txt") as dosya:
        bilgiler = dosya.readlines()
        for satir in bilgiler:
            satir = satir.replace("\n","")
            satir = satir.split(" ")
            yemekler = satir[0]
            ucretler = satir[1]
            yemek[yemekler] = ucretler

def hesap_kontrolu(dosya_adi):
    try:
        dosya = open(dosya_adi)
        bilgiler=dosya.readlines()
        for satir in bilgiler:
            satir = satir.replace("\n", "")
            satir = satir.split("$")
            masa_hesap = satir[0]
            masa_hesap = masa_hesap.split(" ")
            masa_no=masa_hesap[0]
            hesap=masa_hesap[1]
            masalar[int(masa_no)]["hesap"] = float(hesap)
            yemekler = satir[1]
            yemekler = yemekler.split("$")
            try:
                for yemek in yemekler:
                    yemek=yemek.split(" ")
                    masalar[int(masa_no)][yemek[0]] = int(yemek[1])
            except:
                pass
        dosya.close()

    except FileNotFoundError:
        dosya = open(dosya_adi,"w")
        dosya.close()
        print("yeni dosya oluşturuldu")

def guncelle():
    dosya=open("restorant.txt","w")

    for i in range(1,21):
        ücret=masalar[i]["hesap"]
        ücret =str(ücret)
        dosya.write(str(i)+"-"+ücret+"$")
        a = 0
        for t in masalar[i].items():
            a += 1
            if a != 1:
                yemek = t[0]
                miktar = str(t[1])
                dosya.write(yemek+" "+miktar+"%")
            else:
                pass
        dosya.write("\n")
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



def ana_fonksiyon():
    hesap_kontrolu("restorant.txt")
    while True:
        yemek_kontrol()
        guncelle()
        print("""
1-Masaları Görüntüle
2-Hesap Ekle
3-Hesap Çıkar
4-Yemek Ekle
5-Menüyü Göster
6-Çıkış""")
        secim=input("Seçiminizi yapınız : ")
        if secim == "1":
            masalari_goruntule()
        elif secim == "2":
            hesap_ekle()
        elif secim == "3":
            hesap_cikar()
        elif secim == "4":
            yemek_dosyasi()
        elif secim == "5":
            menu_goster()
        elif secim == "6":
            quit()

ana_fonksiyon()