#print("ali","veli","deli",sep="**")

tek_mi= lambda sayi:sayi%2==1
print(tek_mi(21))

def tek_mi(sayi): #ikisi de aynı şey
    return sayi%2==1
print(tek_mi(21))

toplam=lambda *sayilar:sum(sayilar)
print(toplam(24,23,65,87,41,12))