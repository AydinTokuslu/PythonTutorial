
sozluk={}

def kelime_ekle():
    kelime = input("hangi kelimeyi eklemek istiyorsunuz : ")
    if kelime in sozluk.keys():
        print("bu kelime eklidir")
    else:
        sozluk[kelime] ={"anlam":{},
                         "ornek":{}}
    print(sozluk)

def anlam_ekle(kelime):
    anlam=input("kelimenin anlamınız yazınız : ")
    x=1
    for i in sozluk[kelime]["anlam"]:
        x+=1
    sozluk[kelime]["anlam"][x]=anlam

def anlam_goster(kelime):
    print("{} kelimesinin anlamları : ".format(kelime))
    for i in sozluk[kelime]["anlam"].items():
        print("{}. {}".format(i[0],i[1]))

def anlam_degistirme(kelime):
    print("{} kelimesinin anlamları : ".format(kelime))
    for i in sozluk[kelime]["anlam"].items():
        print("{}. {}".format(i[0], i[1]))
    sira=int(input("kaçıncı anlamı değiştirmek istiyorsun : "))
    x=0
    for i in sozluk[kelime]["anlam"].items():
        x+=1
        if x == sira:
            yeni_anlam=input("yeni anlam giriniz : ")
            sozluk[kelime]["anlam"][x]=yeni_anlam

def ornek_ekle():
    kelime=input("hangi kelime ile işlem yapmak istiyorsunuz : ")
    if kelime in sozluk.keys():
        while True:
            print("""
1-Cümle Ekle
2-Cümleleri Gör
3-Cümleyi Düzenle
4-Ana Menüye Dön
""")
            secim=input("seçiminizi giriniz : ")
            if secim == "1":
                cumle = input("örnek cümle giriniz : ")
                anlam=input("yazdığınız örnek cümlenin anlamını giriniz : ")
                sozluk[kelime]["ornek"][cumle]=anlam
            elif secim == "2":
               cumle_goster(kelime)
            elif secim == "3":
                print("{} kelimesine ait örnek cümleler: ".format(kelime))
                x = 0
                for i in sozluk[kelime]["ornek"].items():
                    x += 1
                    print("""
                {}.
                İngilizcesi : {}
                Türkçesi : {} """.format(x, i[0], i[1]))
                sira = int(input("Kaçıncı cümleyi düzenlemek istiyorsunuz : "))
                y = 0
                for i in sozluk[kelime]["ornek"].items():
                    y += 1
                    if y == sira:
                        print("""
-{}
-{}""".format(i[0],i[1]))
                        yeni_cumle=input("Yeni ingilizce cümleyi giriniz: ")
                        yeni_anlam=input("Yeni anlamı giriniz: ")
                        sozluk[kelime]["ornek"]={yeni_cumle:yeni_anlam}
            elif secim == "4":
                break
            else:
                print("hatalı işlem yaptınız")
    else:
        print("Bu kelime ekli değildir.")

def anlam():
        kelime = input("hangi kelime ile işlem yapmak istiyorsunuz? : ")
        if kelime in sozluk.keys():
            while True:
                print("""
    1-Anlam Ekle
    2-Anlam Goster
    3-Anlam Degiştir
    4-Ana Menüye Dön""")
                secim=input("seçiminizi yapınız : ")
                if secim == "1":
                    anlam_ekle(kelime)
                elif secim == "2":
                    anlam_goster(kelime)
                elif secim == "3":
                    anlam_degistirme(kelime)
                elif secim == "4":
                    break
        else:
            print("Bu kelime ekli değildir.")

def kelime_bul():
    kelime=input("Hangi kelimeyi görmek istiyorsunuz : ")
    if kelime in sozluk.keys():
        anlam_goster(kelime)
        cumle_goster(kelime)
    else:
        print("kelime mevcut değildir.")

def cumle_goster(kelime):
    print("{} kelimesine ait örnek cümleler: ".format(kelime))
    x = 0
    for i in sozluk[kelime]["ornek"].items():
        x += 1
        print("""
                    {}.
                    İngilizcesi : {}
                    Türkçesi : {} """.format(x, i[0], i[1]))
def ana_fonksiyon():
    while True:
        print("""
    1-Kelime Bul
    2-Yeni Kelime Ekle
    3-Kelimeye Anlam Ekle
    4-Kelimeye Cümle Örneği Ekle
    5-Çıkış
    """)
        secim=input("işleminizi seçiniz : ")
        if secim == "1":
            kelime_bul()
        elif secim == "2":
            kelime_ekle()
        elif secim == "3":
            anlam()
        elif secim == "4":
            ornek_ekle()
        elif secim == "5":
            print("yine bekleriz")
            quit()
        else:
            print("hatalı işlem girdiniz, tekrar deneyiniz.")


ana_fonksiyon()
