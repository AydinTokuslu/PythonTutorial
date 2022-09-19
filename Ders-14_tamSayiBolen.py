

sayi=int(input("bir sayı giriniz : "))
def tamSayiBolenleriAl(sayi):
    tamBolenler = []
    for i in range(1, sayi):
        if sayi%i == 0:
            tamBolenler.append(i)
    return tamBolenler

print(tamSayiBolenleriAl(sayi))