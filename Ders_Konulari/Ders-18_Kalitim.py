class Personel():
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.maas=maas

    def bilgileriYazdir(self):
        print("""
        {} {} Bilgileri şunlardır : 
        Yaşı : {}
        Cinsiyet : {}
        Maaş : {}
        """.format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas))

    def __str__(self):
        return """
        {} {} Bilgileri şunlardır : 
        Yaşı : {}
        Cinsiyet : {}
        Maaş : {}
        """.format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas)

class Yonetici(Personel):
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
        super().__init__(ad,soyad,yas,cinsiyet,maas)

    def maasArtir(self,pObject, arttirmaMiktari=1000):
        pObject.maas += arttirmaMiktari

personel=Personel("mert","sis","22","erkek",10000)
#personel.bilgileriYazdir()
print(personel)


yonetici=Yonetici("tolgayan","cayliyak","25","erkek",20000)
#print(yonetici)
yonetici.maasArtir(personel)
personel.bilgileriYazdir()
