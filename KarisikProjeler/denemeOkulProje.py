okul={}
menu="""
1- Sınıf Ekle
2- Sınıfları Listele
3- Şube Ekle
4- Şubeleri Listele
5- Ögrenci Ekle
6- Öğrenci Listele
7- Ders Ekle
8- Dersleri Listele
"""

def ders_listele(okul:dict, sinif:str, sube:str, ogrenci:str):
    t=0
    for i in okul[sinif][sube][ogrenci]:
        t+=1
        print("{}. Ders : {}".format(t,i))

def ders_ekle(kul:dict, sinif:str,sube:str, ogrenci:str, ders:str):
    okul[sinif][sube][ogrenci][ders]=0

def ogrenci_listele(okul:dict, sinif:str,sube:str):
    t=0
    for i in okul[sinif][sube]:
        t+=1
        print("{}. öğrenci :  {}".format(t,i))

def ogrenci_ekle(okul:dict, sinif:str,sube:str,ogrenci:str):
    okul[sinif][sube][ogrenci]={}

def sube_listele(okul:dict, sinif:str):
    for i in okul[sinif]:
        print("{} Şubesi".format(i))


def sube_ekle(okul:dict, sinif:str, sube:str):
    okul[sinif][sube]={}

def sinif_listele(okul:dict):
    for i in okul:
        print("{}. sınıf".format(i))

def sinif_ekle(sinif_ismi:str, okul:dict):
    okul[sinif_ismi]={}

while True:
    print(menu)
    secim=input("Seçiminizi giriniz : ")
    if secim == "1":
        a = input("Eklemek istediğiniz sınıfı giriniz : ")
        sinif_ekle(a,okul)
        #print(okul.items())
    elif secim == "2":
        sinif_listele(okul)
    elif secim == "3":
        sinif = input("Hangi sınıfa şube ekleyeceksiniz? : ")
        while True:
            print("""
1- Yeni Şube Ekle
2- Ana Menüye Dön""")
            sec=input("işleminizi seçiniz : ")
            if sec == "1":
                sube = input("Şube ismi giriniz : ")
                sube_ekle(okul,sinif,sube)
            elif sec == "2":
                break
        #print(okul)
    elif secim == "4":
        sinif=input("Hangi sınıfa ait şubeleri görmek istiyorsunuz? : ")
        sube_listele(okul,sinif)
    elif secim == "5":
        sinif=input("Hangi sınıfa öğrenci ekleyeceksiniz? : ")
        sube=input("Hangi şubeye öğrenci ekleyeceksiniz? : ")
        while True:
            print("""
1- Yeni Öğrenci Ekle
2- Ana Menüye Dön""")
            sec = input("işleminizi seçiniz : ")
            if sec == "1":
                ogrenci = input("Öğrenci ismini giriniz : ")
                ogrenci_ekle(okul, sinif, sube, ogrenci)
                print("Ekleme işlemi başarılı")
            elif sec == "2":
                break

    elif secim == "6":
        sinif = input("Hangi sınıfın öğrencilerini görmek istiyorsunuz? : ")
        sube=input("Hangi şubenin öğrencilerini görmek istiyorsunuz? : ")
        ogrenci_listele(okul,sinif,sube)
    elif secim == "7":
        sinif = input("Hangi sınıftaki öğrenciye ders ekleyeceksiniz? :")
        sube=input("Hangi şubedeki öğrenciye ders ekleyeceksiniz? :")
        ogrenci=input("Hangi öğrenciye ders ekleyeceksiniz? :")
        while True:
            print("""
1- Yeni Ders Ekle
2- Ana Menüye dön.""")
            sec = input("seçiminizi yapınız : ")
            if sec == "1":
                ders = input("Eklemek istediğiniz dersin adını giriniz : ")
                ders_ekle(okul, sinif, sube, ogrenci,ders)
                print("Ekleme işlemi başarılı")
            elif sec == "2":
                break
    elif secim == "8":
        sinif = input("Öğrencinin sınıfını giriniz :")
        sube = input("Öğrencinin şubesini giriniz :")
        ogrenci = input("Öğrencinin ismini giriniz :")
        ders_listele(okul,sinif,sube,ogrenci)

