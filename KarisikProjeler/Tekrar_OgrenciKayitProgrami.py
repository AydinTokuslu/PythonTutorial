def not_hesapla(satir):
    satir = satir[:-1]
    liste=satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama = (not1+not2+not3)/3
    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >=85:
        harf = "BA"
    elif ortalama >= 75:
        harf = "BB"
    elif ortalama >= 65:
        harf = "CC"
    else:
        harf = "FF"

    return ogrenciAdi+": "+ harf + "\n"


def notlari_oku():
    with open("notlar.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            print(not_hesapla(satir))


def not_gir():
    ad = input("Öğrenci adını giriniz : ")
    soyad = input("Öğrenci soyadını giriniz : ")
    not1 = input("not 1 : ")
    not2 = input("not 2 : ")
    not3 = input("not 3 : ")

    with open("notlar.txt","a",encoding="utf-8") as dosya:
        dosya.write(ad +" "+ soyad +": "+ not1+","+not2+","+not3+"\n")


def notlari_kayitet():
    with open("notlar.txt","r") as dosya:
        liste=[]
        for i in dosya:
            liste.append(not_hesapla(i))
    with open("notSonuc.txt","w",encoding="utf-8") as file:
        for i in liste:
            file.write(i)

while True:
    islem=input("Lütfen bir işlem seçiniz.\n1-Notları oku\n2-Not gir\n3-Notları kayıt et\n4-Çıkış\n: ")
    if islem == "1":
        notlari_oku()
    if islem == "2":
        not_gir()
    if islem == "3":
        notlari_kayitet()
    if islem == "4":
        break