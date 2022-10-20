



def menu():
    print("""
1-Bakiye Sorgulama
2-Para Yatırma
3-Para Çekme
4-Para Gönderme
5-Şifre Değiştirme
6-Çıkış
""")

bakiye=5000
sifre = "1234qwer"
kartNumarasi="1234567891234567"

def bakiyeSorgulama(bakiye):
    print("Bakiyeniz : {}tldir.".format(bakiye))

def paraYatirma(bakiye):
    yatirilacakPara=int(input("Yatırmak istediğiniz para miktarını giriniz : "))
    bakiye += yatirilacakPara
    bakiyeSorgulama(bakiye)

def paraCekme(bakiye):
    cekilecekPara = int(input("Çekmek istediğiniz para miktarını giriniz : "))
    if bakiye > cekilecekPara:
        bakiye -= cekilecekPara
        bakiyeSorgulama(bakiye)
    else:
        print("Maalesef bakiyenizde o kadar para bulunmamaktadır.")
        bakiyeSorgulama(bakiye)


def paraGonderme(bakiye):
    gönderilecekPara = int(input("Göndermek istediğiniz para miktarını giriniz : "))
    if bakiye > gönderilecekPara:
        iban=input("Para göndereceğiniz iban numarasını giriniz : ")
        if iban.startswith("TR") and len(iban) == 18:
            print("iban numarası doğrudur.")
            bakiye -= gönderilecekPara
            bakiyeSorgulama(bakiye)
        else:
            print("iban numarası doğru değildir.")
    else:
        print("Maalesef bakiyenizde o kadar para bulunmamaktadır.")
        bakiyeSorgulama(bakiye)


def sifreDegistirme(sifre):
    print("Şifrenizi değiştirmek istediğinizden emin misiniz : ")
    cevap = input("Şifre değiştirmek için 1'i vazgeçmek için 2'yi giriniz.")
    if cevap == "1":
        print("mevcut şifreniz : {}".format(sifre))
        yeniSifre=input("yeni şifrenizi giriniz : ")
        sifre=sifre.replace("1234qwer",yeniSifre)
        print("şifreniz değişmiştir. şifreniz : {}".format(sifre))
    elif cevap == "2":
        print("başka bir işlem yapmak için tuşlayınız")
    else:
        print("yanlış numara girişi yaptınız, tekrar deneyiniz. ")


def kartKontrol(kartNumarasi):
    girilenKartNumarasi=input("Lütfen 16 haneli kart numarasını giriniz")
    if girilenKartNumarasi == kartNumarasi:
        print("kart bilgileriniz doğrudur")
    else:
        print("kart bilgileriniz doğru değildir, bilgilerinizi tekrar giriniz :")
        kartKontrol(kartNumarasi)


def sifreKontrol(sifre):
    girilenSifre = input("Lütfen kart şifrenizi giriniz")
    if girilenSifre == sifre:
        print("şifre bilgileriniz doğrudur")
    else:
        print("şifre bilgileriniz doğru değildir, bilgilerinizi tekrar giriniz :")
        sifreKontrol(sifre)


while True:
    print("******* ATM'YE HOŞ GELDİNİZ *******")
    kartKontrol(kartNumarasi)
    sifreKontrol(sifre)
    menu()
    islem=input("Lütfen yapmak istediğiniz işlemin numarasını giriniz : ")
    if islem == "1":
        bakiyeSorgulama(bakiye)
    elif islem == "2":
        paraYatirma(bakiye)
    elif islem == "3":
        paraCekme(bakiye)
    elif islem == "4":
        paraGonderme(bakiye)
    elif islem == "5":
        sifreDegistirme(sifre)
    elif islem == "6":
        quit()
    else:
        print("yanlış işlem tercih ettiniz. Tekrar deneyiniz")
