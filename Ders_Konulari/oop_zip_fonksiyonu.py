# zip fonksiyonu
# zip fonksiyonu bir iterator döndürüyor.

# liste1 = [1,2,3,4]
# liste2 = ["a","b","c","d"]
#
# liste3 = list(zip(liste1, liste2))
# liste4 = set(zip(liste1, liste2))
# liste5 = tuple(zip(liste1, liste2))
# print(liste3)  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# print(liste4)  # {(1, 'a'), (2, 'b'), (4, 'd'), (3, 'c')}
# print(liste5)  # ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

liste1=list("Python")
liste2 = [1,2,3,4]
liste3 = ["A","B","C"]
liste4 = list(zip(liste1, liste2, liste3))
print(liste4)  # [('P', 1, 'A'), ('y', 2, 'B'), ('t', 3, 'C')]
# eleman sayısı kadar eşleşiyor.



