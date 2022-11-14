def sayilariTopla(sayilar):

    if type(sayilar) != list:
        raise TypeError("Parametre Liste objesi olmalı")

    toplam=0

    for i in sayilar:
        toplam+=i

    return toplam

#print(sayilariTopla("mert"))
print(sayilariTopla([1,3,5,8,9,12,45]))