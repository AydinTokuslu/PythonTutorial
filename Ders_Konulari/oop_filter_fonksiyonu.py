# filter fonksiyonu
#
# liste = [1,2,3,5,6,8,11,17,123,101]
#
# def cift_mi(x):
#     if x % 2 == 0:
#         return True
#     return False
#
# #ciftler = list(filter(cift_mi, liste))
# ciftler = list(filter(lambda x : x % 2 == 0, liste))
# #print(ciftler)  # [2, 6, 8]
#
# def iki_basamakli(x):
#     if x >= 10 and x <= 100:
#         return True
#     return False
#
# #iki_basamaklilar = list(filter(iki_basamakli, liste))
# iki_basamaklilar = list(filter(lambda x : x >= 10 and x <= 100, liste))
# print(iki_basamaklilar)  # [11, 17]
#
# kelimeler = ["ayna", "ahmet", "ana", "kalem", "defter", "kazak", "son"]
# a_ile_baslayanlar = list(filter(lambda kelime : kelime.startswith("a"), kelimeler))
# print(a_ile_baslayanlar)  # ['ayna', 'ahmet', 'ana']
#
# icinde_a_gecenler = list(filter(lambda kelime : "a" in kelime, kelimeler))
# print(icinde_a_gecenler)  #['ayna', 'ahmet', 'ana', 'kalem', 'kazak']
#
# palindromlar = list(filter(lambda kelime : kelime == kelime[::-1], kelimeler))
# print(palindromlar)
#
# liste = [1,2, (1,2,3), True, "string", "örnek", {1,2,4}]
# #stringler = list(filter(lambda x : isinstance(x, str), liste))  # isinstance(x, str) string olup olmadığını kontrol eder.
# stringler = list(filter(lambda x : isinstance(x, int), liste))  # isinstance(x, int) int olup olmadığını kontrol eder.
#
# print(stringler)  # [1, 2, True]

liste = [{"Ad": "Ahmet", "Yaş" :20},{"Ad": "Banu", "Yaş" :22},{"Ad": "Can", "Yaş" :18},{"Ad": "Anıl", "Yaş" :28}]
a_ile_baslayanlar = list(filter(lambda kisi : kisi["Ad"].startswith("A"), liste))
print(a_ile_baslayanlar)  # [{'Ad': 'Ahmet', 'Yaş': 20}, {'Ad': 'Anıl', 'Yaş': 28}]
yirmiden_buyuk = list(filter(lambda kisi : kisi["Yaş"]>20, liste))
print(yirmiden_buyuk)  # [{'Ad': 'Banu', 'Yaş': 22}, {'Ad': 'Anıl', 'Yaş': 28}]















