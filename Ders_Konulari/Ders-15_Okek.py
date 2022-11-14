
def ekok(a,b):
    ekok=a*b

    for sayi in range(ekok, max(a,b)-1, -1):
        if sayi%a == 0 and sayi%b == 0:
            ekok=sayi
    return ekok


birinciSayi=int(input("birinci sayıyı giriniz : "))
ikinciSayi=int(input("ikinci sayıyı giriniz : "))

print(ekok(birinciSayi,ikinciSayi))