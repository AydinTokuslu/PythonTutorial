
sahipolunanPara=2000

secim = input("Kart sokmak için 's', Ayrılmak için 'a' yazınız: ")

if secim == "s":
    while True:
        islem = int(input("""
                İşlemler
                -------------------
                1- Para Çekme
                2- Para Yatırma
                3- Hesap Bilgileri
                4- Kart İade
                
            Yapmak istediğiniz işlemin numarasını giriniz : """))
        if islem == 1:
            cekilmekIstenenMiktar=int(input("Çekmek istediğiniz para tutarını giriniz : "))
            if sahipolunanPara < cekilmekIstenenMiktar:
                print("Bu işlem geçersiz. Yeterli bakiyeniz bulunmamaktadır.")
            else:
                sahipolunanPara-=cekilmekIstenenMiktar
        if islem == 2:
            yatirilmakIstenenMiktar=int(input("Yatırmak istediğiniz para tutarını giriniz : "))
            sahipolunanPara+=yatirilmakIstenenMiktar
        if islem == 3:
            print("Hesap Bilgileri\n*****Hesap Sahibi : Aydin Tokus\nHesap IBAN:TR80 XXXX XXXX\nSahip olunan para : {}".format(sahipolunanPara))
        if islem == 4:
            print("Kartı iade aldınız, ATM'den ayrılabilirsiniz.")
            break

else:
    print("Atm'den ayrıldınız")