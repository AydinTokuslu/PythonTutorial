import self as self


class Manav():
    def __init__(self,urunListesi=[],urunFiyatlari=[]):
        self.calisma=True
        self.urunListesi = urunListesi
        self.urunFiyatlari = urunFiyatlari

    def menu(self):
        self.urunListesi.append("domat - urun kodu :1")
        self.urunListesi.append("muz - urun kodu : 2")
        self.urunListesi.append("elma - urun kodu : 3")
        self.urunListesi.append("erik - urun kodu : 4")
        self.urunListesi.append("cilek - urun kodu : 5")

        self.urunFiyatlari.append(15.0)
        self.urunFiyatlari.append(18.0)
        self.urunFiyatlari.append(8.0)
        self.urunFiyatlari.append(47.0)
        self.urunFiyatlari.append(27.0)

        print(self.urunListesi+self.urunFiyatlari)
        secim = self.musteriSecim(self.urunFiyatlari)


    def kasa(self):
        print("Yapacağınız toplam ödeme : {}".format(toplamOdeme))


    def musteriSecim(self):

        secim=int(input("seçtiğiniz ürün kodunu giriniz : "))
        kilo=float(input("seçtiğiniz üründen kaç kilo alacaksınız? : "))
        urunTutari=self.urunFiyatlari.__getitem__(secim-1) * kilo
        toplamOdeme+=urunTutari

        devam=int(input("Alışverişe devam etmek istiyorsanız 1'i, kasa için 2 giriniz"))
        if devam == 1:
            self.musteriSecim()
        elif devam == 2:
            self.kasa()
        return toplamOdeme

manav=Manav()
#while manav.calisma:
manav.menu()

global toplamOdeme