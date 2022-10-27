
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
        cumle = input("örnek cümle giriniz : ")
        anlam=input("yazdığınız örnek cümlenin anlamını giriniz : ")
        sozluk[kelime]["ornek"]={cumle:anlam}

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


while True:
    kelime_ekle()
    anlam()
