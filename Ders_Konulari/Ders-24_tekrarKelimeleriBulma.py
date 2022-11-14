def yazdir(kisiListesi):
    yeniListe=[]
    for kisi in kisiListesi:
        yeniListe.append(kisi.strip().lower().capitalize())

    for kisi in yeniListe:
        sayi=yeniListe.count(kisi)
        if sayi >=2:
            print(kisi)
            for i in range(sayi):
                yeniListe.remove(kisi)

kisiler=["Mehmet","Mert","aLi","Tuncay ","   MeHMet","mehmet   ","MeRt","ecem","Melisa","Ela","ali","kerem","mert  ","hasan","aydin","elif","elif  ","Elif ","sare",]

yazdir(kisiler)