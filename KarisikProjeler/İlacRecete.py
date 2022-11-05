import time

#kullanıcından hasta ismi alınsın.
#1- ilaç listesi oluşturun (Aspirin, Cibadrex, vb)
#2- hastalık listesi oluşturalım (alerji, Başağrısı,vb.)
#3- hastalığa ve ilaca bağlı bir reçete oluşturalım
#4- reçeteleri ana listin içine atalım

hasta_list = []
recete_list = {1 : "Parol",
               2 : "Parol, Aspirin",
               3 : "Glifor",
               4 : "Aferin, Parol",
               5 : "Majezik",
               6 : "Ecoprin, Beloc",
               7 : "Calpol, Ventolin",
               8 : "Aspirin"
               }

hastalikList=["Allerji","Basagrisi","Diyabet","Sogukalginligi","Migren","Kalp Hastaliklari","Cocuk Hastaliklari","Genel Cerrahi"]






def recete_kontrol():
    recete_no = int(input("Lütfen reçete numaranızı giriniz (1-8) : "))
    if recete_no in recete_list:
        for i in recete_list:
            if recete_no == i:
                print("İstediğiniz ilaç mevcuttur. Reçete ekranına yönlendiriliyorsunuz...")
                print(f"Reçeteniz : {recete_list[recete_no]}")

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
    print("Giriş yapılan hasta kayıtlı değildir. Yeni kayot yapılacaktır.")
    hasta = input("lütfen hasta adı giriniz : ")
    hasta_list.append(hasta)
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
            recete_kontrol()
        elif hastalik != i:
            hastalikList.append(hastalik)
        else:
            print("Hastalığınız sistemde tespit edilemedi. Farklı bir birime yönlendiriliyorsunuz. ")

def hastaControl(hasta):
    if hasta in hasta_list:
        recete_kontrol()
    elif hasta not in hasta_list:
        hasta_kayit()
    else:
        print("hatalı giriş yaptınız, tekrar giriniz")
        hasta_girisi()


def hasta_girisi():
    hasta=input("lütfen hasta adı giriniz : ")
    hastaControl(hasta)

hasta_girisi()
