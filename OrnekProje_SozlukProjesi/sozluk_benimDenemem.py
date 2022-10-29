sozluk = {}


def kelime_ekle():
    kelime=input("Eklemek istediğiniz kelimeyi giriniz :")
    if kelime in sozluk.keys():
        print("bu kelime listede vardır")
    else:
        sozluk[kelime] = {"anlam": {},
                          "ornek": {}}



def kelime_goster():
    print("Mevcut kelimeler : ")
    a=0
    for i in sozluk.keys():
        a+=1
        print("{}. {}".format(a,i))


def kelime_sil():
    kelime_goster()
    sira = int(input("silmek istediğiniz kelimenin sıra numarasını giriniz : "))
    liste = []
    y = 0
    for a in sozluk.keys():
        y += 1
        if y == sira:
            liste.append(a)
    sozluk.pop(liste[0])


def kelime_bul():
    kelime=input("bulmak istediğiniz kelimeyi giriniz : ")
    if kelime in sozluk.keys():
        anlam_goster(kelime)
        cumle_goster(kelime)
    else:
        print("belirttiğiniz kelime listede mevcut değildir.")


def anlam_ekle(kelime):
    anlam=input("kelimenin anlamını giriniz : ")
    x=1
    for i in sozluk[kelime]["anlam"]:
        x+=1
    sozluk[kelime]["anlam"][x]=anlam


def anlam_goster(kelime):
    print("{} kelimesinin anlamları : ".format(kelime))
    for i in sozluk[kelime]["anlam"].items():
        print("{}. {}".format(i[0], i[1]))


def anlam_degistir(kelime):
    anlam_goster(kelime)
    sira=int(input("kelimenin kaçıncı anlamını değiştirmek istiyorsunuz : "))
    y=0
    for i in sozluk[kelime]["anlam"].items():
        y+=1
        if y == sira:
            yeni_anlam=input("yeni anlamı giriniz : ")
            sozluk[kelime]["anlam"][y]=yeni_anlam


def anlam():
    kelime=input("hangi kelime ile işlem yapmak istiyorsunuz : ")
    if kelime in sozluk.keys():
        while True:
            print("""
1-Anlam Ekle
2-Anlam Goster
3-Anlam Degiştir
4-Ana Menüye Dön""")
            secim=input("seçiminizi giriniz : ")
            if secim == "1":
                anlam_ekle(kelime)
            elif secim == "2":
                anlam_goster(kelime)
            elif secim == "3":
                anlam_degistir(kelime)
            elif secim == "4":
                break
    else:
        print("Bu kelime ekli değildir.")


def cumle_goster(kelime):
    print("{} kelimesine ait örnek cümleler : ".format(kelime))
    x=0
    for i in sozluk[kelime]["ornek"].items():
        x+=1
        print("""
        {}.
        İngilizcesi : {}
        Türkçesi : {}
        """.format(x, i[0], i[1]))


def ornek_ekle():
    kelime = input("hangi kelime ile işlem yapmak istiyorsunuz : ")
    if kelime in sozluk.keys():
        while True:
            print("""
    1-Cümle Ekle
    2-Cümleleri Goster
    3-Cümleyi Düzenle
    4-Ana Menüye Dön""")
            secim = input("seçiminizi giriniz : ")
            if secim == "1":
                ornek_cumle=input("örnek ingilizce cümleyi giriniz : ")
                ornek_cumle_anlam=input("örnek ingilizce cümlenin türkçe anlamını giriniz : ")
                sozluk[kelime]["ornek"][ornek_cumle]=ornek_cumle_anlam
            elif secim == "2":
                cumle_goster(kelime)
            elif secim == "3":
                cumle_goster(kelime)
                sira=int(input("kaçıncı cümleyi düzenlemek istiyorsunuz, sıra no giriniz : "))
                y = 0
                for i in sozluk[kelime]["ornek"].items():
                    y += 1
                    if y == sira:
                        print("""
                        {}
                        {}""".format(i[0], i[1]))
                        yeni_cumle=input("yeni ingilizce cümleyi giriniz : ")
                        yeni_cumle_anlam=input("yeni ingilizce cümlenin türkçe anlamını giriniz : ")
                        sozluk[kelime]["ornek"]={yeni_cumle : yeni_cumle_anlam}
            elif secim == "4":
                break
            else:
                print("hatalı işlem girdiniz.")
    else:
        print("Bu kelime ekli değildir.")


def dosya_yaz():
    with open("sozluk.txt","w", encoding="utf-8") as dosya:
        for kelime in sozluk.keys():
            dosya.write(kelime+"$")
            for anlam in sozluk[kelime]["anlam"].items():
                dosya.write(str(anlam[0]) + "=" + anlam[1]+ "-")
            dosya.write("%")  # anlam ve örnek bölümünü ½ ile ayırıyoruz.
            for cumle in sozluk[kelime]["ornek"].items():
                dosya.write(cumle[0] + "@" + cumle[1] + "/")  # @, ingilizce ve türkçe bölümünü ayırır.
            dosya.write("\n")  # bir alt satıra geçsin
    dosya.close()


def dosya_oku():
    with open("sozluk.txt", encoding="utf-8") as dosya:
        bilgiler=dosya.readlines()
        for satir in bilgiler:
            satir=satir.replace("\n","")
            satir=satir.split("$")
            kelime=satir[0]
            sozluk[kelime]={"anlam": {},
                            "ornek": {}}
            anlam_cumle=satir[1]
            anlam_cumle=anlam_cumle.split("%")
            anlam=anlam_cumle[0]
            anlam=anlam.split("-")
            try:
                for a in anlam:
                    anlam=a.split("=")
                    sozluk[kelime]["anlam"][int(anlam[0])]=anlam[1]
            except:
                pass
            cumle=anlam_cumle[1]
            cumle=cumle.split("/")
            try:
                for a in cumle:
                    cumle=a.split("@")
                    sozluk[kelime]["ornek"][cumle[0]]=cumle[1]
            except:
                pass
    dosya.close()



def ana_fonksiyon():
    dosya_oku()
    while True:
        dosya_yaz()
        print("""
1-Kelime Bul
2-Yeni Kelime Ekle
3-Kelimeye Anlam Ekle
4-Kelimeye Cümle Örneği Ekle
5-Kelimeleri Listele
6-Kelime Sil
7-Çıkış
    """)
        secim=input("Seçiminizi giriniz : ")
        if secim == "1":
            kelime_bul()
        elif secim == "2":
            kelime_ekle()
        elif secim == "3":
            anlam()
        elif secim == "4":
            ornek_ekle()
        elif secim == "5":
            kelime_goster()
        elif secim == "6":
            kelime_sil()
        elif secim == "7":
            quit()
        else:
            print("hatalı işlem yaptınız, tekrar deneyiniz.")


ana_fonksiyon()