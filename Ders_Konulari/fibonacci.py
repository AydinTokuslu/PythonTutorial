# programın fibonacci dizisinin toplamını
# baştan verilen elemana kadar hesaplayın

def fibonacci():
    sayi = int(input("fibonacci serisini durdurmak için bir sayı giriniz : "))
    genel_toplam = 2
    fibo = [0, 1, 1]
    for i in range(2, sayi):
        toplam = 0
        toplam += fibo[i] + fibo[i-1]
        fibo.append(toplam)
        genel_toplam += toplam
    print(fibo)
    print(genel_toplam)

fibonacci()