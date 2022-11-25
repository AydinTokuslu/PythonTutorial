# reduce fonksiyonu

# reduce fonksiyonu functools kütüphanesi içinde
# pythonda ekok yok, ebob fonksiyonu var
# ekok (a,b) = a *b / ebob(a,b)

from functools import reduce
from math import gcd  # ebob

# liste = [2,4,6,9,10]

# def toplama(x, y):
#     return x + y
# def carpma(x, y):
#     return x * y
#
# #sonuc1 = reduce(toplama, liste)  # fonksiyon ve element olacak
# sonuc1 = reduce(lambda x, y : x + y, liste)  # fonksiyon ve element olacak
# print(sonuc1)  # 21
#
# #sonuc2 = reduce(carpma, liste)  # fonksiyon ve element olacak
# sonuc2 = reduce(lambda x, y : x * y, liste)  # fonksiyon ve element olacak
# print(sonuc2)  # 432

# def ekok(x,y):
#     return int((x * y) / gcd(x,y))
#
# print(ekok(6,8))  # 24.0
# ekok_ = reduce(ekok, liste)
# print(ekok_)  # 180


# taş, kağıt, makas
def tas_makas(x,y):
    kume = {x,y}
    if x == y:
        return x
    if kume == {"taş", "makas"}:
        return "taş"
    if kume == {"taş", "kağıt"}:
        return "kağıt"
    if kume == {"kağıt", "makas"}:
        return "makas"
liste = ["taş","kağıt","taş","makas","kağıt","makas","taş"]
sonuc = reduce(tas_makas, liste)  # liste elemanlarını sırayla fonksiyona göre karşılaştırıyor.
print(sonuc)  # taş




