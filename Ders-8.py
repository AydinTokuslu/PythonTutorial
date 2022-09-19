
# asal sayı bulma
sayi=int(input("sayı giriniz : "))

sayac=2
asal_sayilar=[]


while sayi>0:
    asal_sayilar.append(sayi)
    while sayac<sayi:
        if sayi % sayac == 0:
            asal_sayilar.remove(sayi)
            break

        sayac+=1
    sayac=2
    sayi-=1

print(asal_sayilar)