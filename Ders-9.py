
# asal sayı bulma

def asal_mi(sayi):
    for i in range(2,sayi):
        if sayi%i==0:
            return False
    return True

sayi=int(input("sayı giriniz : "))
asal_sayilar=[]

for i in range(2,sayi+1):
    if asal_mi(i):
        asal_sayilar.append(i)

print(asal_sayilar)