# Girilen sayılardan en büyük ve en küçük sayıları bulma
#
# sayilar = []
#
# flag = True
# en_buyuk = 0
# en_kucuk = 1000000000000
#
# while flag:
#     try:
#         sayi = float(input("sayıları giriniz (bitirmek için -1 giriniz) : "))
#         if sayi == -1:
#             flag = False
#         else:
#             sayilar.append(sayi)
#     except SyntaxError:
#         print("HATA : sadece sayı giriniz!")
#     except NameError:
#         print("HATA : sadece sayı giriniz!")
#     except Exception:
#         print("HATA : sadece sayı giriniz!")
# print(sayilar)
#
# toplam = 0
#
# for sayi in sayilar:
#     if sayi > en_buyuk:
#         en_buyuk = sayi
#     if sayi < en_kucuk:
#         en_kucuk = sayi
#     toplam += sayi
# print(en_kucuk, en_buyuk)
#
# ortalama = toplam / len(sayilar)
# print(ortalama)

sayilar = []

flag = True
while flag:
    try:
        a = int(input("Sayıları girin (bitirmek için -1): "))
        if a == -1:
            flag = False
        else:
            sayilar.append(float(a))
    except SyntaxError:
        print("HATA: Yalnızca sayı girin !")
    except NameError:
        print("HATA: Yalnızca sayı girin !")

try:
    en_buyuk = sayilar[0]
    en_kucuk = sayilar[0]
    ortalama = sayilar[0]
except IndexError:
    print("\nEn az bir sayı girmelisiniz")
    en_buyuk = "yok"
    en_kucuk = "yok"
    ortalama = "yok"
finally:
    toplam = 0

for sayi in sayilar:
    if sayi > en_buyuk:
        en_buyuk = sayi
    if sayi < en_kucuk:
        en_kucuk = sayi
    toplam += sayi

ortalama = toplam / len(sayilar)

print("\nen büyük sayı = {}\n" \
      "en küçük sayı = {}\n" \
      "ortalama      = {}".format(en_buyuk, en_kucuk, ortalama))