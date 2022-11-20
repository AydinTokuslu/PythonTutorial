#lambda fonksiyonları, bir kere veya az kullanılacak fonksiyonların yerine kullanılır.

# def kare_al(x):
#     return x * x
#
# print(kare_al(5)) # 25

# kare_al = lambda x : x * x
# print(kare_al(5))  # 25
#
# kup_al = lambda x : x ** 3
# print(kup_al(5))  # 125
#
# toplam = lambda x, y : x + y
# print(toplam(5, 8))  # 13

# genel_toplam = lambda *args : sum(args)
# print(genel_toplam(2,3,6,8,9))  # 28

# print((lambda x,y,z : x * y + z)(3,5,6))  # 21
# print((lambda *args : sum(args)/len(args))(2,3,4,5,6,7,8))  # 5.0


liste = [("Ali", 20), ("Veli", 19), ("Emel", 30), ("Hakan", 24), ("Cenk", 27)]
#liste.sort()
#print(liste)  # [('Ali', 20), ('Cenk', 27), ('Emel', 30), ('Hakan', 24), ('Veli', 19)]
liste.sort(key=lambda  x : x[1])
print(liste)  # [('Veli', 19), ('Ali', 20), ('Hakan', 24), ('Cenk', 27), ('Emel', 30)]

liste2 = [{"Ad" : "Ahmet", "Soyad" : "Çalışkan", "Yaş" : 25}]