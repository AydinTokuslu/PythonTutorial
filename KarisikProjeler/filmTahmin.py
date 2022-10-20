

filmler = ["JOKER","INCEPTION","PIYANIST","GREENMILE","LEON","GODFATHER","JURASSICPARK","TITANIC"]

print("**** film tahmin oyununa hoşgeldiniz ****")
secilenFilm=int(input("1-" + str((len(filmler))) + " arasında bir sayı giriniz : "))-1


def filmGetir(filmler, secilenFilm):
    tahminSayisi=0
    dogruTahminSayisi=0
    kelime=""
    tahminEdilecekFilm=filmler[secilenFilm]

    #print(tahminEdilecekFilm)
    #print(filmler[secilenFilm][(len(filmler)):]+"-")
    print(str(len(filmler[secilenFilm]))+" harfli bir film seçtiniz.")
    print("filmi tahmin etmek için "+str(2*(len(filmler[secilenFilm])))+" tahmin hakkınız vardır.")
    print("yanlış tahmin sayısı : "+str(tahminSayisi-dogruTahminSayisi)+"/"+str(2*(len(filmler[secilenFilm]))))
    filmtahmin = []
    while True:

        harf = input("tahmin ettiğiniz harfi giriniz : ").upper()
        filmtahmin.append(harf)
        if harf in filmler[secilenFilm]:
            print("doğru harf girdiniz")

            dogruTahminSayisi+=1
            tahminSayisi += 1
            print("yanlış tahmin sayısı : " + str(tahminSayisi - dogruTahminSayisi) + "/" + str(2 * (len(filmler[secilenFilm]))))

            if dogruTahminSayisi == (len(filmler[secilenFilm])):
                    print("tebrikler kazandınız. ")
                    break
        elif harf in filmtahmin:
            print("bu harfi zaten girdiniz, tekrar girmenize gerek yoktu")
        else:
            print("yanlış harf girdiniz")
            tahminSayisi+=1
            print("yanlış tahmin sayısı : " + str(tahminSayisi - dogruTahminSayisi) + "/" + str(2 * (len(filmler[secilenFilm]))))
        if tahminSayisi == 2*(len(filmler[secilenFilm])):
            print("maalesef kaybettiniz, tekrar bekleriz.")
            break



filmGetir(filmler, secilenFilm)


