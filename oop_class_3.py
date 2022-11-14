from datetime import date

class kisi:
    kisi_sayisi = 0  # class variable yazarak tüm class'ta olmuş oldu
    zam_orani = 1.1  # class variable
    def __init__(self,isim, yas):
        self.isim = isim
        self.yas = yas
        kisi.kisi_sayisi += 1  # self ile yapsaydık, instance variable'a ait olurdu
    def bilgilerini_soyle(self):  # selfli olanlar, instance method
        return f"Ad : {self.isim}, Yaş : {self.yas}"

    @classmethod
    def kisi_sayisini_soyle(cls):  #cls, bunun class üzerinden kullanılacağını gösterir.
        return cls.kisi_sayisi
    @classmethod
    def string_ile_olustur(cls, str_):
        isim, yas = str_.split("-")
        return cls(isim, yas)
    @classmethod
    def dogum_yili_ile_olustur(cls, isim, dogum_yili):  # nesne ismi ile değil, class ismi ile çağrılır.
        return cls(isim, date.today().year - dogum_yili)  # burda cls, class (kisi) oluyor.





kisi1 = kisi("Ali", 20)
kisi2 = kisi("Veli", 30)
#print(kisi1.bilgilerini_soyle())
#print(kisi.kisi_sayisini_soyle())  # 2
kisi3 = kisi.string_ile_olustur("Ayse-25") # nesne ismi ile değil, class ismi ile çağrılır.
#print(kisi.kisi_sayisini_soyle())  # 3
#print(kisi3.isim)  # Ayse
kisi4 = kisi.dogum_yili_ile_olustur("Elif", 1986) # nesne ismi ile değil, class ismi ile çağrılır.
print(kisi.kisi_sayisini_soyle())  # 4
print(kisi4.isim, kisi4.yas)  # Elif 36