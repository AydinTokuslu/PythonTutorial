import time

ilacList={1:"Parol",
          2:"Parol",
          3:"Glifor",
          4:"Aferin",
          5:"Majezik",
          6:"Ecoprin",
          7:"Beloc",
          8:"Calpol",
          9:"Ventolin",
          10:"Aspirin"}

hastalikList=["Allerji","Basagrisi","Diyabet","Sogukalginligi","Migren","Kalp Hastaliklari","Cocuk Hastaliklari","Genel Cerrahi"]

recete1=["Parol"]
recete2=["Parol", "Aspirin"]
recete3=["Glifor"]
recete4=["Aferin", "Parol"]
recete5=["Majezik"]
recete6=["Ecoprin", "Beloc"]
recete7=["Calpol", "Ventolin"]
recete8=["Aspirin"]

hastaList=[]
hasta=""
receteNoList=[]

receteList=["recete1","recete2","recete3","recete4","recete5","recete6","recete7","recete8"]

def receteOlustur():
    recete1.append("Parol")
    recete2.append("Parol")
    recete3.append("Glifor")
    recete4.append("Aferin")
    recete4.append("Parol")
    recete5.append("Majezik")
    recete6.append("Ecoprin")
    recete6.append("Beloc")
    recete7.append("Calpol")
    recete7.append("Ventolin")
    recete8.append("Aspirin")


def ilacGetir(receteNo):
    if receteNo == "recete1":
        print("reçetedeki ilacınız : {}".format(recete1))
    elif receteNo == "recete2":
        print("reçetedeki ilacınız : {}".format(recete2))
    elif receteNo == "recete3":
        print("reçetedeki ilacınız : {}".format(recete3))
    elif receteNo == "recete4":
        print("reçetedeki ilacınız : {}".format(recete4))
    elif receteNo == "recete5":
        print("reçetedeki ilacınız : {}".format(recete5))
    elif receteNo == "recete6":
        print("reçetedeki ilacınız : {}".format(recete6))
    elif receteNo == "recete7":
        print("reçetedeki ilacınız : {}".format(recete7))
    elif receteNo == "recete8":
        print("reçetedeki ilacınız : {}".format(recete8))
    else:
        print("yanlış değer girdiniz, tekrar deneyiniz.")
        receteKontrol()
    cikis()

def receteKontrol():
    receteNo=input("reçete numaranızı giriniz : ")
    if receteNo in receteList:
        print("Belirttiğiniz reçete sistemde mevcuttur.")
        secim=input("Reçete bilgisine ulaşmak için 1'i\nAna menü için 2'ye basınız. : ")
        if secim == "1":
            ilacGetir(receteNo)
        elif secim == "2":
            hastaGiris()
        else:
            print("hatalı giriş yaptınız....")
            receteKontrol()
    elif receteNo not in receteList:
        receteList.append(receteNo)
        print("belirttiğiniz reçete sistemde bulunmamaktadır.")
        print("Reçeteler listesi : ")
        print("-------------------")
        for i in receteList:
            print(i)
        ilacGetir(receteNo)
    else:
        print("Hatalı giriş yaptınız")
        hastaGiris()


def hastaKayit():
    print("Belirttiğiniz hasta sistemimizde kayıtlı değildir. Yeni kayıt oluşturulacaktır. ")
    yeniHasta=input("Hasta adı giriniz : ")
    hastaList.append(yeniHasta)
    print("Hasta kaydı tamamlanmıştır.")
    print("Hastalık tanı ekranına yönlendiriliyorsunuz. ")
    for i in range(1,5):
        try:
            time.sleep(1)
        except:
            Exception
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
            receteKontrol()
        elif hastalik != i:
            hastalikList.append(hastalik)
        else:
            print("Hastalığınız sistemde tespit edilemedi. Farklı bir birime yönlendiriliyorsunuz. ")

def cikis():
    islem = input("Çıkış yapmak için 1'i\nAna menüye dönmek için 2'yi tuşlayın")
    if islem == "1":
        quit()
    elif islem == "2":
        hastaGiris()
    else:
        print("yanlış değer girdiniz.")

def hastaControl(hasta):
    if hasta in hastaList:
        receteKontrol()
    elif hasta not in hastaList:
        hastaKayit()
    else:
        print("hatalı giriş yaptınız")
        hastaGiris()


def hastaGiris():
    hasta=input("lütfen hasta adı giriniz : ")
    hastaControl(hasta)

hastaGiris()