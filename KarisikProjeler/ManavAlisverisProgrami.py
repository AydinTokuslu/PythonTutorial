import self as self


class Manav():
    def __init__(self,urunListesi=[]):
        self.durum=True
        self.urunListesi=urunListesi

    def menu(self):

        while True:
            print("""
            **** Elif Manava hoş geldiniz ****
            1- Urun Ekleme
            2- Urun Silme
            3- Urun Seçme
            4- Urun Odeme
            5- Urun Listeleme
            6- Çıkış
            """)

            tercih = int(input("Lütfen yapmak istediğiniz işlemi giriniz : "))

            if tercih == 1:
                self.urunEkle()
                break
            if tercih == 2:
                self.urunSilme()
                break
            if tercih == 3:
                self.urunSecme()
                break
            if tercih == 4:
                self.urunOdeme()
                break
            if tercih == 5:
                self.urunListeleme()
                break
            if tercih == 6:
                self.cikis()
                break


    def urunEkle(self):
        urunIsmi = input("Ürün ismi giriniz : ")
        urunFiyati = int(input("Ürün fiyatı giriniz : "))

        self.urunListesi.append(urunIsmi + " - " + str(urunFiyati))
    def urunOdeme(self):
        self.urunSecme()
        print("Yapacağınız toplam ödeme : {}".format(self.toplamOdeme))

    def cikis(self):
        self.durum=False
    def urunSilme(self):
        silinecekUrun=input("Lütfen silmek istediğiniz ürünü yazın : ")
        self.urunListesi.remove(silinecekUrun)

    def urunListeleme(self):
        print(self.urunListesi)
    def urunSecme(self):

        toplamOdeme=0
        secim=input("Lütfen satın almak istediğiniz ürün ismini giriniz : ")
        kilo=float(input("Lütfen seçtiğiniz üründen kaç kilo alacağınızı giriniz : "))

        if self.urunListesi.__contains__(secim):
            secilen=self.urunListesi("secim")

        secilenUrun= self.urunListesi(secim.split(" - ")[1])
        print(secilenUrun)
        #secilenUrunTutari= int(secilenUrun[1])
        #urunTutari= secilenUrunTutari * kilo
        urunTutari= secilenUrun * kilo
        toplamOdeme+=urunTutari

        devam=int(input("Alışverişe devam etmek istiyorsanız 1'i, kasa için 2 giriniz"))
        if devam == 1:
            self.musteriSecim()
        elif devam == 2:
            self.kasa()
        return toplamOdeme

    def calistir(self):
        self.menu()


manav=Manav()
while manav.durum:
    manav.calistir()