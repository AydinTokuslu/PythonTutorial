import math

sayi=int(input("sayi giriniz: "))
faktoriyel=1

for i in range(1,sayi+1):
    faktoriyel*=i

print("Girdiğiniz {} sayısının faktoriyeli {} ".format(sayi,faktoriyel))
print("{}! = ".format(sayi)+str(faktoriyel))