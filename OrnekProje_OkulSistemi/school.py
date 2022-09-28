import random
class Okul:
    def __init__(self,isim):
        self.isim=isim

    class Ogrenci:
        def __init__(self,isim,soyisim,no,sinif,disiplin_puani,ders={"Türkce":0,"Matematik":0}):
            self.isim=isim
            self.soyisim=soyisim
            self.no=no
            self.sinif=sinif
            self.disiplin_puani=disiplin_puani
            self.ders=ders

        def disiplin(self):
            disiplin=input("öğrenci disipline gitti  mi= (Evet ya da Hayir yazınız) : ")
            if (disiplin == "Evet"):
                self.disiplin_puani-=10
                if(self.disiplin_puani<=0):
                    print("öğrenci kaydı silindi")
                    self.isim=None
                    self.soyisim = None
                    self.no = None
                    self.sinif = None
                    self.disiplin_puani = None
                else:
                    print("öğrencimizin disiplin puanı 10 puan düşürüldü! Yeni puanı:",self.disiplin_puani)
            elif(disiplin != "Evet" or disiplin == "Hayir"):
                print("Meşgul etme!")

        def goruntule(self):
            print("""
            isim : {}
            soyisim : {}
            no : {}
            sinif : {}
            disiplin puani : {}
            """.format(self.isim,self.soyisim,self.no,self.sinif,self.disiplin_puani))

        def puan_degis(self):
            girdi=input("Lütfen puanı değiştirmek istediğiniz dersi giriniz ('Türkce' yada 'Matematik'): ")
            if girdi == "Türkce":
                self.ders["Türkce"] = int(input("Lütfen puanı giriniz : "))
                if 0 <= self.ders["Türkce"] <= 100:
                    print("Başarılı bir şekilde puan değişti. Türkçe Puanınız :", self.ders["Türkce"])
                else:
                    print("Puan değişmedi")
                    self.ders["Türkce"] = 0
            elif girdi == "Matematik":
                self.ders["Matematik"] = int(input("Lütfen puanı giriniz : "))
                if 0 <= self.ders["Matematik"] <= 100:
                    print("Başarılı bir şekilde puan değişti. Matematik Puanınız :", self.ders["Matematik"])
                else:
                    print("Puan değişmedi")
                    self.ders["Matematik"] = 0
            else:
                print("Böyle bir ders yok!")

        def puan_goruntule(self):
            print("""
            Matematik notunuz : {}
            Türkçe notunuz : {}
            """.format(self.ders["Matematik"], self.ders["Türkce"]))

        def hoca_yakalama(self):
            sayi=random.randint(1,2)
            if sayi == 1:
                print("Hocaya yakalandık!")
                self.disiplin_puani -=2
            elif sayi == 2:
                print("Ynalış alarm!")
    class Ogretmen:
        def __init__(self,isim,soyisim,sifre):
            self.isim = isim
            self.soyisim = soyisim
            self.sifre = sifre
        def Ogretmen_bilgi(self):
            print("""
            isim : {}
            soyisim : {}
            """.format(self.isim,self.soyisim))