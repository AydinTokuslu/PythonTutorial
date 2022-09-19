from random import randint

oyunDurumu=True

while oyunDurumu:
    rastgeleSayi=randint(1,100)
    hak=7
    while True:
        if hak > 0:
            tahmin=int(input("lütfen bir tahminde bulunuz (1-100) : "))
        else:
            print("sayıyı doğru tahmin edemediniz : sayı :{}".format(rastgeleSayi))
            break
        if tahmin != rastgeleSayi:
            hak -= 1
            if tahmin>rastgeleSayi:
                print("sayı aşağıda. Kalan tahmin hakkınız : {}".format(hak))
            else:
                print("sayı yukarıda. Kalan tahmin hakkınız : {}".format(hak))
        else:
            print("tebrikler sayıyı doğru tahmin ettiniz")
            break
    kontrol=input("Oyuna devam etmek istiyor musunuz? (E/H) : ")
    if kontrol=="E":
        oyunDurumu=True
    else:
        oyunDurumu=False