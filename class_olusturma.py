class Kelimeler():
    def __init__(self):
        self.anlamlari = []
        self.cumleler = []

kelime_listesi = []

while True:
    print("""
1-Kelime Ekle
2-Anlam Ekle
3-Cümle Örneği Ekle
4-Kelime Bul
5-Çıkış""")
    secim = input("Seçiminiz : ")
    if secim == "1":
        kelime = input("Eklemek istediğiniz kelimeyi giriniz : ")
        kelime = Kelimeler()
        kelime_listesi.append(kelime)
    elif secim == "2":
        kelime = input("Anlam eklemek istediğiniz kelimeyi giriniz : ")
        anlam = input("Anlamı giriniz : ")
        kelime = Kelimeler()
        kelime.anlamlari.append(anlam)
    elif secim == "3":
        kelime = input("Cümle eklemek istediğiniz kelimeyi giriniz : ")
        ingilizce_cumle = input("İngilizce cümle giriniz : ")
        turkce_cumle = input("İngilizce cümle giriniz : ")
        kelime = Kelimeler()
        kelime.cumleler[ingilizce_cumle] = turkce_cumle
    elif secim == "4":
        kelime = input("Kelime : ")
        print("""
Kelime : {}
Anlamları : """.format(kelime))
        x = 0
        for i in kelime.anlamlari:
            x += 1
            print("""
            {}. {}""".format(x,i))
            print("Cümle Örnekleri : ")
            y = 0
            for i in kelime.cumleleri.items():
                y += 1
                print("""
{}.
- {}
- {}""".format(y, i[0], i[1]))
