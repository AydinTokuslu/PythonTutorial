
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
                cumle = input("örnek ingilizce cümle giriniz : ")
                anlam=input("yazdığınız örnek ingilizce cümlenin türkçe anlamını giriniz : ")
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


def dosya_yaz():
    with open("ingilizce.txt","a", encoding="utf-8") as dosya:
        for kelime in sozluk.keys():
            dosya.write(kelime + "$")
            for anlam in sozluk[kelime]["anlam"].items():
                dosya.write(str(anlam[0]) + " = " + anlam[1] + "-")
            dosya.write("%")  # anlam ve örnek kısmını ½ ile ayırıyouz.
            for cumle in sozluk[kelime]["ornek"].items():
                dosya.write(cumle[0] + "@" + cumle[1] + "/")  # @ inglizce ve türkçe cümleyi ayırır.
            dosya.write("\n")  # sonraki her kelime grubu için ayırım işareti /
    dosya.close()

def dosya_oku():
    with open("ingilizce.txt", "r", encoding="utf-8") as dosya:
        bilgiler=dosya.readlines()
        for satir in bilgiler:
            satir = satir.replace("\n","")
            satir = satir.split("$")
            kelime = satir[0]
            sozluk[kelime] = {"anlam": {},
                              "ornek": {}}
            anlam_cumle = satir[1]
            anlam_cumle = anlam_cumle.split("%")
            anlam = anlam_cumle[0]
            anlam = anlam.split("-")
            try:
                for a in anlam:
                    anlam = a.split("=")
                    sozluk[kelime]["anlam"][int(anlam[0])] = anlam[1]
            except:
                pass
            cumle= anlam_cumle[1]
            cumle = cumle.split("/")
            try:
                for a in cumle:
                    cumle = a.split("@")
                    sozluk[kelime]["ornek"][cumle[0]] = cumle[1]
            except:
                pass
    dosya.close()



def kelime_listele():
    print("Mevcut Kelimeler: ")
    x = 0
    for i in sozluk.keys():
        x += 1
        print("{}. {}".format(x, i))


def kelime_sil():
    kelime_listele()
    sira=int(input("Silmek istediğiniz kelimenin sırasını yazınız : "))
    liste=[]
    y = 0
    for a in sozluk.keys():
        y += 1
        if y == sira:
            liste.append(a)
    sozluk.pop(liste[0])


def ana_fonksiyon():
    #dosya_oku()
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
            kelime_listele()
        elif secim == "6":
            kelime_sil()
        elif secim == "7":
            print("yine bekleriz")
            quit()
        else:
            print("hatalı işlem girdiniz, tekrar deneyiniz.")


ana_fonksiyon()
