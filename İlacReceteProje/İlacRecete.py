import time

#kullanıcından hasta ismi alınsın.
#1- ilaç listesi oluşturun (Aspirin, Cibadrex, vb)
#2- hastalık listesi oluşturalım (alerji, Başağrısı,vb.)
#3- hastalığa ve ilaca bağlı bir reçete oluşturalım
#4- reçeteleri ana listin içine atalım

class Eczane():
    def __init__(self,hasta_adi,hasta_soyadi,hasta_sikayet):
        self.hasta_adi = hasta_adi
        self.hasta_soyadi = hasta_soyadi
        self.hasta_sikayet = hasta_sikayet
    def get_hastaAdi(self):
        return self.hasta_adi
    def get_hastaSoyadi(self):
        return self.hasta_soyadi
    def get_hastaSikayet(self):
        return self.hasta_sikayet
    def set_hastaAdi(self, hasta_adi):
        self.hasta_adi = hasta_adi
    def set_hastaSoyadi(self, hasta_soyadi):
        self.hasta_soyadi = hasta_soyadi
    def set_hastaSikayet(self, hasta_sikayet):
        self.hasta_sikayet = hasta_sikayet



hasta_list = []
recete_list = {1 : "Parol",
               2 : "Aspirin",
               3 : "Glifor",
               4 : "Aferin",
               5 : "Majezik",
               6 : "Ecoprin",
               7 : "Beloc",
               8 : "Calpol",
               9 : "Ventolin",
               }

hastalikList=["Allerji","Basagrisi","Diyabet","Sogukalginligi","Migren","Kalp Hastaliklari","Cocuk Hastaliklari","Genel Cerrahi"]
ilac_fiyatlari = {"Parol" : 50,
                  "Aspirin" : 40,
                  "Glifor" : 65,
                  "Aferin" : 55,
                  "Majezik" : 80,
                  "Ecoprin" : 90,
                  "Beloc" : 120,
                  "Calpol" : 100,
                  "Ventolin" : 150
                  }
doktor_listesi = {"Hakan" : "Allerji",
                  "Mithat" : "Allerji",
                  "Cemil" : "Basagrisi",
                  "Elif" : "Diyabet",
                  "Hande" : "Diyabet",
                  "Nuray" : "Sogukalginligi",
                  "Fatma" : "Sogukalginligi",
                  "Aydın" : "Migren",
                  "Enis" : "Migren",
                  "Hüseyin" : "Kalp Hastaliklari",
                  "Hüsamettin" : "Kalp Hastaliklari",
                  "Fırat" : "Kalp Hastaliklari",
                  "Hilal" : "Cocuk Hastaliklari",
                  "Bilal" : "Cocuk Hastaliklari",
                  "Aslı" : "Genel Cerrahi",
                  "Asuman" : "Genel Cerrahi",
                  "Sare" : "Genel Cerrahi" }
ilac_odeme = 0

def recete_kontrol(ilac_odeme):
    recete_k = True
    while recete_k:
        recete_no = int(input("Lütfen reçete numaranızı giriniz (1-8) : "))
        if recete_no in recete_list:
            print("İstediğiniz ilaç mevcuttur. Reçete ekranına yönlendiriliyorsunuz...")
            print(f"Reçeteniz : {recete_list[recete_no]}")
            recete_k = False
            sec = input("İlacınızı satın almak için 1'i, ana menüye dönmek için 2'yi tuşlayınız. ")
            if sec == "1":
                if recete_list[recete_no] in ilac_fiyatlari.keys():
                    print(
                        f"ilacınız olan {recete_list[recete_no]}'in fiyatı : {ilac_fiyatlari[recete_list[recete_no]]}'tldir")
                ilac_odeme += ilac_fiyatlari[recete_list[recete_no]]
                print(f"Yapacağınız toplam ödeme {ilac_odeme} tldir.")
                sec = input("Ödeme yapmak için 1'i, başka bir ilaç almak için 2'yi tuşlayınız : ")
                if sec == "1":
                    odeme(ilac_odeme)
                elif sec == "2":
                    recete_kontrol(ilac_odeme)
                else:
                    print("Yanlış tercihte bulundunuz. tekrar deneyiniz.")
            elif sec == "2":
                main()
            else:
                print("Yanlış tercihte bulundunuz, tekrar giriş yapıp deneyiniz.")
        else:
            secim = input("İstediğiniz ilaç maalesef mevcut değildir. Tekrar giriş yapmak için 1'i, çıkış için 2'yi tuşlayınız.")
            if secim == "1":
                hasta_girisi()
            elif secim == "2":
                quit()
            else:
                print("Yanlış seçim yaptınız. çıkışa yönlendiriiyorsunuz. ")
                quit()


def hasta_kayit():
    #hasta = Eczane()
    print("Giriş yapılan hasta kayıtlı değildir. Yeni kayıt yapılacaktır.")
    hasta_adi = input("lütfen hasta adı giriniz : ")
    #hasta_list.append(hasta.hasta_adi)
    hasta_list.append(hasta_adi)
    print("Hasta kaydı tamamlanmıştır.\nReçete ekranına yönlendiriliyorsunuz....")
    for i in range(3):
        time.sleep(1)
        print(".")
    hastalıkListesi()
    ilacYazim()

def hastalıkListesi():
    print("Hastalık çeşitleri : ")
    print("--------------------")
    for i in hastalikList:
        print(i)

def ilacYazim():
    hastalik=input("Rahatsızlığınızı giriniz : ")
    for i in hastalikList:
        if hastalik == i:
            recete_kontrol(ilac_odeme)
        elif hastalik != i:
            hastalikList.append(hastalik)
        else:
            print("Hastalığınız sistemde tespit edilemedi. Farklı bir birime yönlendiriliyorsunuz. ")

hasta_adi = ""
hasta_soyadi = ""
hasta_sikayet = ""

def hasta_girisi():
    #hasta = Eczane()
    dosya = open("hasta_bilgileri.txt", "a", encoding="utf-8")
    hastalıkListesi()
    global hasta_adi
    global hasta_soyadi
    global hasta_sikayet
    hasta_adi = input("Lütfen hasta adını giriniz : ")
    #hasta.set_hastaAdi(input("Lütfen hasta adını giriniz : "))
    hasta_soyadi = input("Lütfen hasta soyadını giriniz : ")
    #hasta.set_hastaSoyadi(input("Lütfen hasta soyadını giriniz : "))
    hasta_sikayet = input("Lütfen yukarıdaki listeden hasta şikayetini giriniz : ")
    #hasta.set_hastaSikayet(input("Lütfen yukarıdaki listeden hasta şikayetini giriniz : "))
    print("Kaydınız tamamlanmıştır. Ana menüye yönlendiriliyorsunuz...")
    #dosya.write(hasta.hasta_adi+"/"+hasta.hasta_soyadi+"/"+hasta.hasta_sikayet+"\n")
    dosya.write(hasta_adi+"/"+hasta_soyadi+"/"+hasta_sikayet+"\n")
    main()
    dosya.close()
    #return hasta.set_hastaAdi(), hasta.set_hastaSoyadi(), hasta.set_hastaSikayet()
    return hasta_adi, hasta_soyadi, hasta_sikayet


def randevu_alma():
    #hasta = Eczane()
    print("Görevli Doktor Listesi : ")
    print("S.No : Doktor İsmi :         Branşı : ")
    print("-------------------------------------")
    a = 0
    for i in doktor_listesi.items():
        a += 1
        print("{:<3}-   Dr.{:<10} ------> {:<10}".format(a, i[0], i[1]))
    doktor = input("Lütfen muayene olmak istediğiniz doktor ismini DR ünvanı olmadan giriniz : ")
    if doktor in doktor_listesi.keys():
        muayene_gun = input("Lütfen muayene olmak istediğiniz günü giriniz : ")
        muayene_saati = input("Lütfen muayene olmak istediğiniz saati giriniz : ")
        #print(f"Sayın {hasta.get_hastaAdi()} {hasta.get_hastaSoyadi()}, {hasta.get_hastaSikayet()} şikayetiyle yapmış olduğunuz muayeneniz Dr.{doktor} ile {muayene_gun} günü ve saat {muayene_saati}'de yapılacaktır.")
        print(f"Sayın {hasta_adi} {hasta_soyadi}, {hasta_sikayet} şikayetiyle yapmış olduğunuz muayeneniz Dr.{doktor} ile {muayene_gun} günü ve saat {muayene_saati}'de yapılacaktır.")
    else:
        print("Yanlış doktor ismi girdiniz. Tekrar deneyiniz.")


def odeme(ilac_odeme):
    print(f"Ödemeniz gereken toplam tutar : {ilac_odeme}")
    sec = input("Ödemenizi kredi kartı ile ödemek için 1'i, havale ile ödemek için 2'yi tuşlayınız")
    if sec == "1":
        kart_no = input("Lütfen TR yazmadan ve boşluk bırakmadan 16 haneli kart numaranızı giriniz : ")
        if len(kart_no) != 16:
            print("Eksik veya fazla rakam girişi yaptınız. ")
            print("Lütfen TR yazmadan ve boşluk bırakmadan 16 haneli kart numaranızı giriniz : ")
            odeme(ilac_odeme)
        elif len(kart_no) == 16:
            print("Kart üzerinde yazan Ad ve Soyad bilgilerini giriniz : ")
            print("Kart üzerinde yazan son kullanma tarihini giriniz : ")
            print("Kart üzerinde yazan güvenlik numarasını giriniz : ")
            print(f"Ödemeniz gereken toplam tutar : {ilac_odeme}")
            print("Ödemeniz başarı ile yapılmıştır. Teşekkür eder, yine bekleriz. Ana menüye yönlendiriliyorsunuz...")
            main()
    elif sec == "2":
        print("Havala yapacağınız banka bilgileri aşağıda belirtilmiştir. Ödeme sonrası bilgi vermeyi unutmayınız")
        print("TR1234 5678 9000 0123")
        print("Havale işlemi için teşekkür eder, yine bekleriz. Ana menüye yönlendiriliyorsunuz...")
        main()
    else:
        print("Yanlış işlem girdiniz. İşleminizi tekrar ediniz. ")
        odeme(ilac_odeme)


def hasta_bilgilerini_goruntuleme():
    with open("hasta_bilgileri.txt", encoding="utf-8") as dosya:
        bilgiler = dosya.readlines()
        bilgiler = bilgiler.replace("\n","")
        for bilgi in bilgiler:
            print(bilgi)



def main():
    while True:
        print("""
    1-Hasta Bilgilerini Görüntüleme
    2-Reçete Sorgulama
    3-Randevu Almak
    4-Ödeme
    5-Çıkış""")
        secim=input("Lütfen seçiminizi yapınız : ")
        if secim == "1":
            hasta_bilgilerini_goruntuleme()
        elif secim == "2":
            recete_kontrol(ilac_odeme)
        elif secim == "3":
            randevu_alma()
        elif secim == "4":
            odeme(ilac_odeme)
        elif secim == "5":
            quit()
        else:
            print("Yanlış tercihte bulundunuz. Tekrar deneyiniz.")
hasta_bilgilerini_goruntuleme()
hasta_girisi()

