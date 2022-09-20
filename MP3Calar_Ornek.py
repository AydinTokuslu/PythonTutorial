from random import choice

class MP3Calar():
    def __init__(self, sarkiListesi=[]):
        self.suanCalanSarki= ""
        self.ses=100
        self.sarkiListesi=sarkiListesi
        self.durum=True

    def sarkiSec(self):
        sayac = 1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac, sarki))
            sayac += 1

        secilenSarki = int(input("Seçmek istediğiniz şarkının numarasını giriniz : "))

        while secilenSarki < 1 or secilenSarki > len(self.sarkiListesi):
            secilenSarki = int(
                input("Seçmek istediğiniz şarkının DOĞRU numarasını giriniz (1-{}): ".format(self.sarkiListesi)))

        self.suanCalanSarki = self.sarkiListesi[secilenSarki - 1]

    def sesArttir(self):
        if self.ses == 100:
            pass
        else:
            self.ses += 10
    def sesAzalt(self):
        if self.ses == 0:
            pass
        else:
            self.ses -= 10

    def rastgeleSarkiSec(self):
        rssec = choice(self.sarkiListesi)
        self.suanCalanSarki = rssec

    def sarkiEkle(self):
        sanatci = input("Sanatçı/Grubu giriniz : ")
        sarki = input("Şarkıyı giriniz : ")

        self.sarkiListesi.append(sanatci + " - " + sarki)
    def sarkiSil(self):
        sayac = 1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac, sarki))
            sayac += 1
        silinecekSarki = int(input("Silmek istediğiniz şarkının numarasını giriniz : "))
        while silinecekSarki < 1 or silinecekSarki > len(self.sarkiListesi):
            silinecekSarki = int(
                input("Silmek istediğiniz şarkının DOĞRU numarasını giriniz (1-{}): ".format(self.sarkiListesi)))

        self.sarkiListesi.pop(silinecekSarki - 1)

    def kapa(self):
        self.durum=False
        
    def menuGoster(self):
        print("""
--- Mert Mekatronik Mp3 Çalara hoş geldiniz ---
Şarkı listesi : {}
Şuan Çalan Şarkı : {}
Ses Düzeyi : {}

1)Şarkı Seç
2)Ses Arttır
3)Ses Azalt
4)Rastgele Şarkı Seç
5)Şarkı Ekle
6)Şarkı Sil
7)Kapa        
""".format(self.sarkiListesi,self.suanCalanSarki,self.ses))

    def secim(self):
        sec=int(input("Seçiminizi giriniz : "))

        while sec < 1 or sec > 7:
            sec = int(input("Seçtiğiniz değer yanlış, lütfen belirtilen aralıklarda değer giriniz (1-7) : "))
        return sec

    def calistir(self):
        self.menuGoster()
        secim=self.secim()
        if secim == 1:
            self.sarkiSec()
        if secim == 2:
            self.sesArttir()
        if secim == 3:
            self.sesAzalt()
        if secim == 4:
            self.rastgeleSarkiSec()
        if secim == 5:
            self.sarkiEkle()
        if secim == 6:
            self.sarkiSil()
        if secim == 7:
            self.kapa()


mp3calar=MP3Calar()
while mp3calar.durum:
    mp3calar.calistir()