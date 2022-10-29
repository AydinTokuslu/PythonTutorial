okul={}


def sinif_ekle(okul):
    print("Yalnızca 1, 2, 3 ve 4ncü sınıf ekleyebilirsiniz.")
    sinif_ismi=input("eklemek istediğiniz sinif ismini giriniz : ")
    if sinif_ismi == "1" or sinif_ismi == "2" or sinif_ismi == "3" or sinif_ismi == "4":
        okul[sinif_ismi]={}
    else:
        print("hatalı işlem girdiniz")


def sinif_listele(okul):
    for i in okul:
        print("{} Sınıf ".format(i))


def sube_ekle(okul):
    sinif=input("hangi sınıfa şube ekleyeceksiniz : ")
    while True:
        print("""
1-Yeni Şube Ekle
2-Şubeleri Listele
3-Ana Menüye Dön""")
        secim=input("Seçiminizi yapınız : ")
        if secim == "1":
            print("Yalnızca A, B, C ve D Şubelerini ekleyebilirsiniz.")
            sube_ismi=input("Eklemek istediğiniz şube ismini giriniz : ").upper()
            if sube_ismi == "A" or sube_ismi == "B" or sube_ismi == "C" or sube_ismi == "D":
                okul[sinif][sube_ismi]={}
            else:
                print("hatalı işlem girdiniz.")
        elif secim == "2":
            for i in okul[sinif]:
                print("{} Şubesi : ".format(i))
        elif secim == "3":
            break
        else:
            print("hatalı işlem girdiniz.")


def sube_listele(okul):
    sinif=input("hangi sınıfın şubelerini görmek istiyorsunuz : ")
    for i in okul:
        print("{} Sınıf Şubeleri : ".format(i))
        for a in okul[i]:
            print("{:>20} Şubesi ".format(a))


def ogrenci_ekle(okul):
    sinif=input("öğrenciyi hangi sınıfa ekleyeceksiniz : ")
    sube=input("öğrenciyi hangi şubeye ekleyeceksiniz : ").upper()
    while True:
        print("""
1- Yeni Öğrenci Ekle
2- Öğrenci Çıkar
3- Öğrenci İsmi Düzenle
4- Şubenin Öğrencilerini Listele
5- Ana Menüye Dön""")
        secim=input("seçiminizi giriniz : ")
        if secim == "1":
            ogrenci=input("öğrenci ismini giriniz : ").upper()
            okul[sinif][sube][ogrenci]={}
            print("ekleme işlemi başarılı")
        elif secim == "2":
            cikacak_ogrenci=input("çıkarmak istediğiniz öğrenci ismini giriniz : ").upper()
            if cikacak_ogrenci in okul[sinif][sube]:
                okul[sinif][sube].pop(cikacak_ogrenci)
                print("çıkarma işlemi başarılı")
            else:
                print("belirttiğiniz öğrenci okulumuzda bulunmamaktadır.")
        elif secim == "3":
            degisecek_ogrenci=input("İsmi düzenlenecek öğrenci ismini giriniz : ").upper()
            if degisecek_ogrenci in okul[sinif][sube]:
                okul[sinif][sube].pop(degisecek_ogrenci)
            else:
                print("belirttiğiniz öğrenci okulumuzda bulunmamaktadır.")
            isim=input("yeni ismi giriniz : ").upper()
            okul[sinif][sube][isim]={}
            print("isim düzenleme işlemi başarılı")
        elif secim == "4":
            t=0
            for i in okul[sinif][sube]:
                t+=1
                print("{}. {} ".format(t,i))
        elif secim == "5":
            break
        else:
            print("hatalı işlem yaptınız. tekrar deneyiniz. ")


def ogrenci_listele(okul):
    for i in okul:
        print("{}. Sınıf".format(i))
        for a in okul[i]:
            print("{:>10} Şubesi".format(a))
            t=0
            for z in okul[i][a]:
                t+=1
                print("{:>20} {}".format(t,z))


def ders_ekle(okul):
    sinif=input("ders ekleyeceğiniz sınıfı giriniz : ")
    sube=input("ders ekleyeceğiniz şubeyi giriniz : ").upper()
    ogrenci=input("hangi öğrenciye ders ekleyeceksiniz : ").upper()
    while True:
        print("""
1- Yeni Ders Ekle
2- Ders Çıkar
3- Dersleri Listele
4- Ana Menüye dön.""")
        sec = input("seçiminizi yapınız : ")
        if sec == "1":
            ders_listesi=["İngilizce","Türkçe","Matematik","Fen","Fizik","Kimya","Biyoloji","Tarih","Çince","Resim"]
            a=0
            for i in ders_listesi:
                a+=1
                print("{} - {}".format(a,i))

            ders=int(input("seçmek istediğiniz dersin numarasını giriniz : "))-1
            okul[sinif][sube][ogrenci][ders_listesi[ders]]=0
            print("Ders ekleme işlemi başarılı")

        elif sec == "2":
            x=0
            for i in okul[sinif][sube][ogrenci]:
                x+=1
                print("{}. Ders : {}".format(x,i))
            cikarilacak_ders=int(input("çıkarılacak dersin numarasını giriniz : "))
            def cikarma(cikarilacak_ders):

                y = 0
                for i in okul[sinif][sube][ogrenci]:
                    y += 1
                    if y == cikarilacak_ders:
                        cikacak =i
                        return cikacak
            okul[sinif][sube][ogrenci].pop(cikarma(cikarilacak_ders))
            print("ders çıkarma işlemi başarılı")
        elif sec == "3":
            a=0
            for i in okul[sinif][sube][ogrenci]:
                a+=1
                print("{}.Ders : {}".format(a,i))

        elif sec == "4":
            break
        else:
            print("hatalı işlem yaptınız. tekrar deneyiniz.")



def ders_listele(okul):
    sinif=input("öğrencinin sınıfını giriniz : ")
    sube=input("öğrencinin şubesini giriniz : ").upper()
    ogrenci=input("öğrencinin adını giriniz : ").upper()
    t=0
    for i in okul[sinif][sube][ogrenci]:
        t+=1
        print("{}. Ders :  {}".format(t,i))


def not_ekle(okul):
    sinif = input("öğrencinin sınıfını giriniz : ")
    sube = input("öğrencinin şubesini giriniz : ").upper()
    ogrenci = input("öğrencinin adını giriniz : ").upper()
    while True:
        print("""
1- Not Ekle
2- Ana Menüye Dön""")
        sec = input("seçiminizi yapınız : ")
        if sec == "1":
            ders=input("dersin adını giriniz : ")
            ders_notu=int(input("dersin notunu giriniz : "))
            okul[sinif][sube][ogrenci][ders] += ders_notu
        elif sec == "2":
            break
        else:
            print("hatalı işlem girdiniz.")


def not_goster(okul):
    sinif = input("öğrencinin sınıfını giriniz : ")
    sube = input("öğrencinin şubesini giriniz : ").upper()
    ogrenci = input("öğrencinin adını giriniz : ").upper()
    for i in okul[sinif][sube][ogrenci].items():
        print("{:>15}  :  {}".format(i[0],i[1]))


def anaFonksiyon():
    while True:
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

anaFonksiyon()