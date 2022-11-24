# map fonksiyonu

# liste = [1,2,4,5,7]
#
# def kare_al(x):
#     return x * x
#
# liste2 = []
# for i in liste:
#     liste2.append(kare_al(i))
# print(liste2)
#
# map içine fonksiyon ve parametre alır.
# #liste3 = list(map(kare_al, liste))  # [1, 4, 16, 25, 49]
# #liste3 = set(map(kare_al, liste))  # {1, 4, 16, 49, 25}
# liste3 = tuple(map(kare_al, liste))  # (1, 4, 16, 25, 49)
#
# print(liste3)

# liste = [1,2,3,6,7,9]
# liste2 = list(map(lambda x : x * x, liste))
# print(liste2)  # [1, 4, 9, 36, 49, 81]

# liste1 = [1,3,4,7,8]
# liste2 = [3,5,9,0,1]
#
# def toplam(x,y):
#     return x + y
#
# sonuc = list(map(toplam, liste1,liste2))
# print(sonuc)  # [4, 8, 13, 7, 9]

# liste1 = [1,3,4,7,8]
# liste2 = [3,5,9,0,1]
# liste3 = [2,5,10]
#
# def toplam(x,y,z):
#     return x + y + z
#
# sonuc = list(map(toplam, liste1,liste2, liste3))
# print(sonuc)  # [6, 13, 23]
# sonuc2 = list(map(lambda x,y,z : x + y + z, liste1, liste2, liste3))
# print(sonuc2)  # [6, 13, 23]

# urunler = [["Ayakkabı", 150], ["Pantolon", 120], ["Gömlek", 100], ["Ceket", 200]]
#
# def indirim_yap(x):
#     urun, fiyat = x[0],x[1]
#     fiyat = fiyat * (9/10)
#     return [urun, fiyat]
#
# sonuc = list(map(indirim_yap, urunler))
# print(sonuc)

isimler = ["AhMet", "aYşE", "oNUR", "HÜseyİn"]

isimler2 = list(map(lambda x : x.lower(), isimler))
print(isimler2)  # ['ahmet', 'ayşe', 'onur', 'hüseyi̇n']
