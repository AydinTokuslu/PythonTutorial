# @property, @setter, @deleter

class Kisi:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
        #self.adsoyad = ad + " " + soyad
    @property
    def adsoyad(self):
        return f"{self.ad} {self.soyad}"

    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"

    @adsoyad.setter
    def adsoyad(self, isim):
        ad, soyad = isim.split(" ")
        self.ad = ad
        self.soyad = soyad

    @adsoyad.deleter #adsoyadı silme decoratorı
    def adsoyad(self):
        print("silindi")
        self.ad = None
        self.soyad = None

kisi1 = Kisi("Ali", "Uzun")
#del kisi1, kisi1'i sileriz
#del kisi1.ad, kisi1'in adını sileriz.
kisi1.ad = "Ahmet"
#kisi1.adsoyad = "Ali Kısa", AttributeError: can't set attribute 'adsoyad'
kisi1.adsoyad = "Ayşe Yıldız"
#del kisi1.adsoyad

print(kisi1.ad)  # Ali, Ahmet
print(kisi1.adsoyad)  # Ali Uzun, Ahmet Uzun
print(kisi1.email)  # Ali.Uzun@sirket.com, Ahmet.Uzun@sirket.com

