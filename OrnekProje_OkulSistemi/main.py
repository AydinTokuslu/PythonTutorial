import school

Ogrenci1= school.Okul.Ogrenci("Yılmaz","Alaca",150, "11-A",100)
#Ogrenci1.disiplin()
#print(Ogrenci1.isim)
#Ogrenci1.goruntule()
#Ogrenci1.puan_degis()
#Ogrenci1.puan_degis()
#Ogrenci1.puan_goruntule()
#Ogrenci1.hoca_yakalama()
#Ogrenci1.goruntule()

Ogretmen=school.Okul.Ogretmen("Ahmet","Siyah",12345)
'''
sifre=int(input("Lütfen şifreyi giriniz: "))
if sifre == Ogretmen.sifre:
    Ogrenci1.disiplin()
else:
    print("Böyle bir yetkiniz yoktur!")
'''
Okul = school.Okul("Vefa okulu")

while True:
    print("""
    sevgili {} sakinleri, okulumuza hoş geldiniz.
    """.format(Okul.isim))
    islem=input("Öğrenci işlemleri için '1'e basın, Öğretmen işlmeleri için '2'ye basın (Çıkmak için '*'a basın): ")
    if islem == "1":
        print("Öğrenci bilgi sistemindesiniz!\n")
        islem2=input("Puan görüntülemek için '1'e basın. Öğrenci bilginizi görüntülemek için '2'e basın: ")
        if islem2 == "1":
            if Ogrenci1.disiplin_puani == None:
                pass
            else:
                Ogrenci1.puan_goruntule()
        elif islem2 == "2":
            Ogrenci1.goruntule()
        else:
            print("Yanlış değer girdiniz.Sistemi meşgul ettiğiniz için görevli öğretmene bilgi verildi.")
            Ogrenci1.hoca_yakalama()
    elif islem =="2":
        print("Öğretmen bilgi sistemindesiniz!\n")
        islem3 = input("""
        Yapabileceğiniz işlemler,
        Disiplin için '1',
        Ders Notu için '2'
        Öğretmen bilgisi için '3'e basın :  
        """)
        if islem3 == "1":
            sifre =int(input("Lütfen öğretmen şifrenizi giriniz : "))
            if sifre == Ogretmen.sifre:
                Ogrenci1.disiplin()
            elif sifre != Ogretmen.sifre:
                print("Yanlış şifre girdiniz! Hocaya haber verildi!")
                Ogrenci1.hoca_yakalama()
        elif islem3 == "2":
            sifre = int(input("Lütfen öğretmen şifrenizi giriniz : "))
            if sifre == Ogretmen.sifre:
                if Ogrenci1.disiplin_puani == None:
                    pass
                else:
                    Ogrenci1.puan_degis()
            elif sifre != Ogretmen.sifre:
                print("Yanlış şifre girdiniz! Hocaya haber verildi!")
                Ogrenci1.hoca_yakalama()
        elif islem3 == "3":
            Ogretmen.Ogretmen_bilgi()
        else:
            print("Yanlış değer girdiniz.Sistemi meşgul ettiğiniz için görevli öğretmene bilgi verildi.")
            Ogrenci1.hoca_yakalama()
    elif islem == "*":
        pass