listemiz = list()

menu = """
1- Öğrenci Ekle
2- Öğrenci Çıkar
3- Listele
4- Çıkış
"""

def ekle(bilgi:tuple, liste:list):
    liste.append(bilgi)
    print("Ekleme işlemi başarı ile tamamlandı")

def control(bilgi:tuple, liste:list):
    if bilgi in liste:
        return True
    else:
        return False

def cıkar(bilgi:tuple, liste:list):
    if control(bilgi, liste):
        liste.remove(bilgi)
        print("Çıkarma işlemi başarı ile tamamlandı")
    else:
        print("Öğrenci listede bulunmamaktadır.")

def listele(liste:list):
    t=1
    for i in liste:
        print("""
        {}. Öğrencinin Bilgileri
        
        Öğrencinin Adı              : {}
        Öğrencinin Soyadı           : {}
        Öğrencinin Numarası         : {}
        Öğrencinin Not Ortalaması   : {}    
        """.format(t, i[0], i[1], i[2], i[3]))
        t += 1

while True:
    print(menu)
    secim = int(input("işlemi seçiniz : "))
    if secim == 1:
        ad = input("Öğrenci adı giriniz : ")
        soyad = input("Öğrenci soyadı giriniz : ")
        numara = input("Öğrenci numarasını giriniz : ")
        ortalama = input("Öğrencinin ortalamasını giriniz : ")

        bilgi = (ad,soyad,numara,ortalama)
        ekle(bilgi, listemiz)

    elif secim == 2:
        ad = print("Öğrenci adı giriniz : ")
        soyad = print("Öğrenci soyadı giriniz : ")
        numara = print("Öğrenci numarasını giriniz : ")
        ortalama = print("Öğrencinin ortalamasını giriniz : ")

        bilgi = (ad, soyad, numara, ortalama)
        cıkar(bilgi, listemiz)
    elif secim == 3:
        listele(listemiz)
    elif secim == 4:
        print("Yine bekleriz")
        quit()
    else:
        print("hatalı veri girdiniz")


