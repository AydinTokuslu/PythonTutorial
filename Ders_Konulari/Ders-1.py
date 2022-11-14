

def faktoriyelAl(sayi):
    faktoriyel=1
    for i in range(1,sayi+1):
        faktoriyel=faktoriyel * i
    return faktoriyel

print(faktoriyelAl(4))