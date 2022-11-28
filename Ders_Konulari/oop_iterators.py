# iterator, iterable ve iteration kavramları
# __iter__() ve __next__()

sayilar = [1,2,3]

i_sayilar = iter(sayilar)

# print(i_sayilar.__next__())  # 1, iterator sırayla listeyi getirir
# print(next(i_sayilar)) # 2
# print(next(i_sayilar)) # 3

# veya
while True:
    try:
        sayi = next(i_sayilar)
        print(sayi)
    except StopIteration:
        break