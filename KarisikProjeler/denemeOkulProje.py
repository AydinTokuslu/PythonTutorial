okul={}

def anaFonksiyon():
    menu="""
1- Sınıf Ekle
2- Sınıfları Listele
3- Şube Ekle
4- Şubeleri Listele
5- Ögrenci Ekle
6- Öğrenci Listele
7- Ders Ekle
8- Dersleri Listele
9- Not Ekle
10- Ders notlarını göster
11- Çıkış
"""
    print(menu)
    secim = input("Seçiminizi giriniz : ")
    if secim == "1":
        sinif_ekle(okul)
    elif secim == "2":
        sinif_listele(okul)
    elif secim == "3":
        sube_ekle(okul)
    elif secim == "4":
        sube_listele(okul)
    elif secim == "5":
        ogrenci_ekle(okul)
    elif secim == "6":
        ogrenci_listele(okul)
    elif secim == "7":
        ders_ekle(okul)
    elif secim == "8":
        ders_listele(okul)
    elif secim == "9":
        not_ekle(okul)
    elif secim == "10":
        not_goster(okul)
    elif secim == "11":
        quit()
    else:
        print("Hatalı giriş yaptınız")


def not_goster(okul:dict):
    sinif = input("Öğrencinin sınıfını giriniz :")
    sube = input("Öğrencinin şubesini giriniz :")
    ogrenci = input("Öğrencinin ismini giriniz :")
    for i in okul[sinif][sube][ogrenci].items():
        print("{:<15}   :  {}".format(i[0],i[1]))

def not_ekle(okul:dict):
    sinif = input("Öğrencinin sınıfını giriniz :")
    sube = input("Öğrencinin şubesini giriniz :")
    ogrenci = input("Öğrencinin ismini giriniz :")
    while True:
        print("""
1- Not Ekle
2- Ana Menüye Dön""")
        sec = input("seçiminizi yapınız : ")
        if sec == "1":
            ders = input("Dersin adını giriniz : ")
            dersNot = int(input("Not değerini giriniz"))
            okul[sinif][sube][ogrenci][ders] += dersNot
        elif sec == "2":
            break


def ders_listele(okul:dict):
    sinif = input("Öğrencinin sınıfını giriniz :")
    sube = input("Öğrencinin şubesini giriniz :")
    ogrenci = input("Öğrencinin ismini giriniz :")
    t=0
    for i in okul[sinif][sube][ogrenci]:
        t+=1
        print("{}. Ders : {}".format(t,i))

def ders_ekle(okul:dict):
    sinif = input("Hangi sınıftaki öğrenciye ders ekleyeceksiniz? :")
    sube = input("Hangi şubedeki öğrenciye ders ekleyeceksiniz? :")
    ogrenci = input("Hangi öğrenciye ders ekleyeceksiniz? :")
    while True:
        print("""
1- Yeni Ders Ekle
2- Ders Çıkar
3- Dersleri Listele
4- Ana Menüye dön.""")
        sec = input("seçiminizi yapınız : ")
        if sec == "1":
            ders_listesi=["İngilizce","Türkçe","Matematik","Fen","Fizik","Kimya","Biyoloji","Tarih","Çince","Resim"]
            x=0
            for i in ders_listesi:
                x+=1
                print("{}. {}".format(x,i))

            ders = int(input("Eklemek istediğiniz dersin sırasını giriniz : "))-1
            okul[sinif][sube][ogrenci][ders_listesi[ders]]=0
            print("Ders ekleme işlemi başarılı")
        elif sec == "2":
            x = 0
            for i in okul[sinif][sube][ogrenci]:
                x += 1
                print("{}. Ders : {}".format(x, i))
            cikarilacakDers = int(input("Çıkarmak istediğiniz dersin sıra numarasını giriniz : "))
            def cikarma(cikarilacakDers):

                y = 0
                for i in okul[sinif][sube][ogrenci]:
                    y += 1
                    if y == cikarilacakDers:
                        cikacak =i
                        return cikacak
            okul[sinif][sube][ogrenci].pop(cikarma(cikarilacakDers))
        elif sec == "3":
            x=0
            for i in okul[sinif][sube][ogrenci]:
                x+=1
                print("{}. Ders : {}".format(x,i))
        elif sec == "4":
            break

def ogrenci_listele(okul:dict):

    for i in okul:
        print("{}. sınıf :".format(i))
        for t in okul[i]:
            print("{:>10} Şubesi".format(t))
            z=0
            for y in okul[i][t]:
                z+=1
                print("{:>20}. {}".format(z,y))

def ogrenci_ekle(okul:dict):
    sinif = input("Hangi sınıfa öğrenci ekleyeceksiniz? : ")
    sube = input("Hangi şubeye öğrenci ekleyeceksiniz? : ")
    while True:
        print("""
1- Yeni Öğrenci Ekle
2- Öğrenci Çıkar
3- Öğrenci İsmi Düzenle
4- Şubenin Öğrencilerini Listele
5- Ana Menüye Dön
""")
        sec = input("işleminizi seçiniz : ")
        if sec == "1":
            ogrenci = input("Öğrenci ismini giriniz : ")
            okul[sinif][sube][ogrenci] = {}
            print("Ekleme işlemi başarılı")
        elif sec == "2":
            cikacakOgrenci = input("Çıkarmak istediğiniz öğrencinin adı : ")
            okul[sinif][sube].pop(cikacakOgrenci)
            print("Çıkarma işlemi başarılı")
        elif sec == "3":
            degisecekOgrenci= input("Düzenlemek istediğiniz öğrencinin adı : ")
            okul[sinif][sube].pop(degisecekOgrenci)
            isim=input("Yeni ismi giriniz")
            okul[sinif][sube][isim]={}
            print("Düzenleme işlemi başarılı")
        elif sec == "4":
            t=0
            for i in okul[sinif][sube]:
                t+=1
                print("{}. {}".format(t,i))
        elif sec == "5":
            break


def sube_listele(okul:dict):
    sinif = input("Hangi sınıfa ait şubeleri görmek istiyorsunuz? : ")
    for i in okul:
        print("{}. Sınıf Şubeleri".format(i))
        for t in okul[i]:
            print("{:>20} Şubesi".format(t))


def sube_ekle(okul:dict):
    sinif = input("Hangi sınıfa şube ekleyeceksiniz? : ")
    while True:
        print("""
1- Yeni Şube Ekle
2- Sınıfın şubelerini listele
3- Ana Menüye Dön""")
        sec = input("işleminizi seçiniz : ")
        if sec == "1":
            print("Sadece A, B, C ve D şubelerini ekleyebilirsiniz.")
            sube = input("Şube ismi giriniz : ")
            if sube == "A" or sube == "B" or sube == "C" or sube == "D":
                okul[sinif][sube] = {}
            else:
                print("Hatalı giriş yaptınız")
        elif sec == "2":
            for i in okul[sinif]:
                print("{} Şubesi".format(i))
        elif sec == "3":
            break


def sinif_listele(okul:dict):
    for i in okul:
        print("{}. sınıf".format(i))


def sinif_ekle(okul:dict):
    print("Sadece 1., 2., 3. ve 4. sınıfları ekleyebilirsiniz.")
    sinif_ismi = input("Eklemek istediğiniz sınıfı giriniz : ")
    if sinif_ismi == "1" or sinif_ismi == "2" or sinif_ismi == "3" or sinif_ismi == "4":
        okul[sinif_ismi]={}
    else:
        print("hatalı giriş yaptınız")


while True:
    anaFonksiyon()


