masalar={}
yemek={}

for i in range(1,11):
    masalar[i]={}
for i in range(1,11):
    masalar[i]["hesap"]=0



def masalariGoruntule():
    for i in range(1,11):
        print("{}. Masa Hesabı : {}".format(i, masalar[i]["hesap"]))


def menuGoster():
    for i in yemek.items():
        print("Yemek ismi : {:<10}, Ücreti : {}".format(i[0],i[1]))


def hesapEkle():
    masa_no=int(input("Masa numarası giriniz : "))
    while True:
        print("""
1-Yeni sipariş gir
2-Masadaki siparişleri gör
3-Ana menüye dön""")
        secim=input("seçiminizi giriniz : ")
        if secim == "1":
            print("Yemekler : ")
            x=0
            for i in yemek:
                x+=1
                print("{}. {}".format(x,i))
            siparis=input("Siparişinizin sıra numarasını giriniz : ")
            y=0
            for i in yemek.items():
                y+=1
                if y==siparis:
                    miktar=int(input("sipariş kaç adet : "))
                    toplam=masalar[masa_no] + float(yemek[i[0]])*miktar
                    masalar[masa_no]["hesap"]=toplam
                    if i[0] in masalar[masa_no].keys():
                        masalar[masa_no][i[0]]+=miktar
                    else:
                        masalar[masa_no][i[0]]=miktar
                else:
                    pass
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


def yemekEkle():
    dosya=open("yemek.txt","a", encoding="utf-8")
    while True:
        print("""
1-Yemek Ekle
2-Ana menüye dön""")
        secim = input("seçiminizi giriniz : ")
        if secim == "1":
            yemek_ismi=input("Eklemek istediğiniz yemeğin adı nedir? : ")
            yemek_ucreti=input("Yemeğin ücretini giriniz : ")
            dosya.write(yemek_ismi+" "+yemek_ucreti+"\n")
        elif secim == "2":
            break
    dosya.close()


def yemekKontrolu():
    with open("yemek.txt") as dosya:
        bilgiler=dosya.readlines()
        for satir in bilgiler:
            satir=satir.replace("\n","")
            satir=satir.split(" ")
            yemekler=satir[0]
            ucretler=satir[1]
            yemek[yemekler]=ucretler


def guncelle():
    dosya=open("restorant.txt","w",encoding="utf-8")
    for i in range(1,11):
        ucret=masalar[i]["hesap"]
        ucret=str(ucret)
        dosya.write(str(i)+" "+ucret+"$")
        a=0
        for t in masalar[i].items():
            a+=1
            if t!= 1:
                yemek=t[0]
                miktar=str(t[1])
                dosya.write(yemek+" "+miktar+"$")
            else:
                pass
        dosya.write("\n")
    dosya.close()


def hesapOde():
    masa_no=int(input("masa numarası giriniz : "))
    while True:
        print("""
1-Nakit çıkar
2-Sipariş çıkar
3-Hesabı sil
4-Masadaki siparişleri gör
5-Ana menüye dön""")
        secim = input("Seçiminizi giriniz : ")
        if secim == "1":
            ucret=float(input("ücreti giriniz : "))
            toplam=masalar[masa_no]["hesap"] - ucret
            if toplam>= 0:
                masalar[masa_no]["hesap"] = toplam
            else:
                print("hatalı işlem yaptınız.")
        elif secim == "2":
            print("Yemekler : ")
            x=0
            for i in yemek:
                x+=1
                print("{}. {}".format(x,i))
            siparis=int(input("çıkarmak istediğiniz sipariş numarasını giriniz : "))
            y=0
            for i in yemek.items():
                y+=1
                if y == siparis:
                    miktar=float("siparişiniz kaç adet : ")
                    toplam=masalar[masa_no]["hesap"] - miktar*float(yemek[i[0]])
                    if miktar >= int(masalar[masa_no][i[0]]):
                        masalar[masa_no].pop(i[0])
                    else:
                        mevcut=float(masalar[masa_no][i[0]])
                        toplam = mevcut - miktar
                        masalar[masa_no][i[0]]=toplam
                    if toplam>= 0:
                        masalar[masa_no]["hesap"]=toplam
                    else:
                        print("hatalı işlem yaptınız")
                else:
                    pass
        elif secim == "3":
            print("Masadaki hesap : {}".format(masalar[masa_no]["hesap"]))
            masalar[masa_no]["hesap"]=0
            liste=[]
            x=1
            for i in masalar[masa_no].items():
                x+=1
                if x != 1:
                    liste.append(i[0])
                else:
                    pass
            h=0
            for i in liste:
                masalar[masa_no].pop(i)
        elif secim == "4":
            a=0
            for i in masalar[masa_no].items():
                a+=1
                if a != 1:
                    print("{:<3} Adet {}".format(i[1], i[0]))
        elif secim == "5":
            break


def hesapKontrolu(dosya_adi):
    try:
        dosya=open(dosya_adi,"r",encoding="utf-8")
        bilgiler=dosya.readlines()
        for satir in bilgiler:
            satir=satir.replace("\n","")
            satir=satir.split("$")
            masa_hesap=satir[0]
            masa_hesap=masa_hesap.split(" ")
            masa_no=masa_hesap[0]
            hesap=masa_hesap[1]
            masalar[int(masa_no)]["hesap"]=float(hesap)
            yemekler=satir[1]
            yemekler=yemekler.split("$")
            try:
                for yemek in yemekler:
                    yemek=yemek.split(" ")
                    masalar[int(masa_no)][yemek[0]]=int(yemek[1])
            except:
                pass
        dosya.close()
    except FileNotFoundError:
        dosya=open(dosya_adi,"w")
        dosya.close()
        print("yeni dosya oluşturuldu.")


def main():
    hesapKontrolu("restorant.txt")
    while True:
        yemekKontrolu()
        guncelle()
        print("""
1-Masaları Goruntule
2-Hesap Ekle
3-Hesap Öde
4-Menüye Yemek Ekle
5-Menuyu Goster
6-Çıkış
""")
        secim=input("Seçiminizi giriniz : ")
        if secim == "1":
            masalariGoruntule()
        elif secim == "2":
            hesapEkle()
        elif secim == "3":
            hesapOde()
        elif secim == "4":
            yemekEkle()
        elif secim == "5":
            menuGoster()
        elif secim == "6":
            quit()
        else:
            print("Yanlış değer girdiniz, tekrar deneyiniz")


main()
