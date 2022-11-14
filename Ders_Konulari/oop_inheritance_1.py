class Calisan: # herhangi bir yerden miras almadığı için () kullanmıyoruz.
    zam_orani = 1.1
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
    def bilgileri_goster(self):  # instance method
        return "Ad : {}, Soyad : {}, Maas : {}, Email : {}".format(self.isim, self.soyisim,self.maas,self.email)


calisan1 = Calisan("Ali", "Caliskan", 5000)
calisan2 = Calisan("Veli", "Uzun", 6000)

#print(calisan2.email)

class Yazilimci(Calisan):  # Calisan class'ından miras alacağı için () yazıyoruz.
    def __init__(self, isim, soyisim, maas, bildigi_dil):
        super().__init__(isim, soyisim, maas)  # yukarıdan isim, soyisim, maas bilgilerini super() ile getirir.
        # self.isim = isim  # yukarıda yazan bu özellikleri tekrar yazmak yerine super().__init__ kullanırız.
        # self.soyisim = soyisim # yukarıda yazan bu özellikleri tekrar yazmak yerine super().__init__ kullanırız.
        # self.maas = maas # yukarıda yazan bu özellikleri tekrar yazmak yerine super().__init__ kullanırız.
        # self.email = isim + soyisim + "@sirket.com" # yukarıda yazan bu özellikleri tekrar yazmak yerine super().__init__ kullanırız.
        self.bildigi_dil = bildigi_dil
    zam_orani = 1.2
    def bilgileri_goster(self):
        return "Ad : {}, Soyad : {}, Maas : {}, Email : {}, Dil : {}".format(self.isim, self.soyisim,self.maas,self.email, self.bildigi_dil)
    def dilini_soyle(self):
        return f"Bildiğim dil : {self.bildigi_dil}"

yazilimci1 = Yazilimci("Ayşe","Yıldız",7000, "Python")
yazilimci2 = Yazilimci("Fatma","Ay",8000, "Java")
#print(yazilimci1.email)
#print(yazilimci1.zam_orani)  # 1.1
#print(calisan2.zam_orani)  # 1.1

# print(yazilimci1.zam_orani)  # 1.2, zam oranını Yazilimci için 1.2 yaptık
# print(calisan2.zam_orani)  # 1.1

# print(calisan2.bilgileri_goster())
# print(yazilimci1.bilgileri_goster())

print(yazilimci1.dilini_soyle())  # Bildiğim dil : Python