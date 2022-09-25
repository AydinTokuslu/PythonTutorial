def not_hesapla(satir):
    satir=satir[:-1] # satır aralarındaki boşlukları alıyoruz.
    liste=satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])

    ortalama=(not1+not2+not3)/3

    if ortalama >= 90 and ortalama<=100:
        harf = "AA"
    elif ortalama >= 85:
        harf = "BA"
    elif ortalama >= 75:
        harf = "BB"
    elif ortalama >= 75:
        harf = "CC"
    else:
        harf = "FF"

    return ogrenciAdi+": "+ harf+ "\n"


def ortalamalari_oku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file:
        for satir in file:
            #print(satir)
            print(not_hesapla(satir))
def not_gir():
    ad = input("Öğrenci adı : ")
    soyad = input("Öğrenci soyadı : ")
    not1 = input("not 1 : ")
    not2 = input("not 2 : ")
    not3 = input("not 3 : ")

    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+ not1+","+not2+","+not3+"\n")


def notlari_kayitet():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file:
        liste=[]
        for i in file:
            liste.append(not_hesapla(i))

        #elde ettiğimiz sonuçları farklı bir dosyaya kayıt ediyoruz.
        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem=int(input("1-Notları oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n: "))

    if islem == 1:
        ortalamalari_oku()
    if islem == 2:
        not_gir()
    if islem == 3:
        notlari_kayitet()
    if islem == 4:
        break


