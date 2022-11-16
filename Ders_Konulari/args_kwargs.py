#birden fazla element ile işlem yapmak için *args'dan faydalanırız.

def topla(*args):  # *args : istediğiniz kadar parametre girebilirsiniz demek.
    for arg in args :
        print(arg)

#topla(1,2,3,4,5)
#topla(1,2,3,4,5, "Python", True)

def carp(*args):
    carpim = 1
    for arg in args:
        carpim *= arg
    #print(type(args))  #class tuple
    return carpim

#print(carp(3,4,5,6,7))

def ortalama(*args):
    return sum(args) / len(args)
#print(ortalama(5,8,10,17))  # 10.0

# def selamla(mesaj, *args):
#     print(mesaj)
#     print("*******************")
#     for arg in args:
#         print(arg)
# print(selamla("Merhaba", "Nasılsın", 23, True))

# def selamla(mesaj, *args):
#     sonuc = ""
#     sonuc += mesaj
#     sonuc += " "
#     for arg in args:
#         sonuc += arg
#         sonuc += " "
#     return sonuc
# print(selamla("Merhaba", "Ali","Nasılsın"))

def fonk(**kwargs): # **kwargs : istediğin sayıda istediğin kadar keyword argument girebilirsin demek
    print(kwargs)
#fonk(ad = "ali", soyad = "çalışkan", yas = 34)
# *args : istediğiniz kadar PARAMETRE (arguments =args) girebilirsiniz demek.
# **kwargs : istediğin sayıda istediğin kadar KEYWORD ARGUMENT (kwargs) girebilirsin demek
# keyword : kwargs

def fonk2(zorunlu, *args, **kwargs):
    print(zorunlu)
    print("**************")
    for arg in args:
         print(arg)
    print("**************")
    for kwarg in kwargs:
         print(kwarg)

fonk2(2, 3,4,5,6,7, ad="Ali", yas =23)
# 2 = zorunlu
# 3,4,5,6,7 = *args
# ad, yas = **kwargs

