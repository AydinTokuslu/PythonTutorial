import json

class Sistem:
    def __init__(self):
        self.durum=True
        self.veriler=self.verileriAl()

    def calistir(self):
        self.menuGoster()
        secim=self.menuSecimYap()

        if secim == 1:
            self.girisYap()
        if secim == 2:
            pass
        if secim == 3:
            pass
        if secim == 4:
            pass

    def menuGoster(self):
        print("""
1-Giriş Yap
2-Kayıt Ol
3-Şifremi Unuttum
4-Çıkış
        """)
    def menuSecimYap(self):
        while True:
            try:
                secim=int(input("Seçiminizi giriniz: "))
                while secim < 1 or secim > 4:
                    secim = int(input("Lütfen 1 ila 4 arasında değer giriniz: "))
                break
            except ValueError:
                print("Lütfen sayı giriniz!\n")
        return secim

    def verileriAl(self):
        try:
            with open("kullanicilar.json","r") as dosya:
                veriler=json.load(dosya)
        except FileNotFoundError:
            with open("kullanicilar.json","w") as dosya:
                dosya.write("{}")

            with open("kullanicilar.json", "r") as dosya:
                veriler = json.load(dosya)
        return veriler

        dosya.close()

    def girisYap(self):
        kadi=input("Kullanıcı adınızı giriniz")
        sifre=input("Sifrenizi giriniz")
        self.kontrolEt()

    def kayitOl(self):
        pass
    def sifremiUnuttum(self):
        pass
    def cikis(self):
        pass

    def kontrolEt(self,kadi,sifre):
        self.veriler=self.verileriAl()
        for kullanici in self.veriler["kullanicilar"]:
            if kullanici["kadi"] == kadi and kullanici["sifre"] == sifre and kullanici["timeout"] == "" and kullanici["Aktif"] == "Y":
                return True
        return False

    def timeOutVarMi(self):
        pass
    def aktifMi(self):
        pass
    def girisBasarisiz(self,sebep):
        print(sebep)
    def girisBasarili(self):
        pass
    def kayitVarMi(self,kadi,sifre):
        pass
    def kayitBasarisiz(self, sebep):
        pass
    def aktivasyonKoduGonder(self):
        pass
    def aktivasyonKontrolEt(self):
        pass
    def kaydet(self):
        pass
    def ePostaVarMi(self):
        pass
    def sifreDegistir(self):
        pass




sistem=Sistem()
while sistem.durum:
    sistem.calistir()