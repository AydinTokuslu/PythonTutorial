# lambda fonksiyonu;
# kısa kodlar yazacaksak,
# fonksiyon kullanmanın anlamlı olmadığı yerlerde
# bir kere kullanıp bitireceğimiz işlemler için kullanırız.


# f = lambda x: 3 * x + 2
# print(f(2))
#
# f = lambda x, y, z: x + 2 * y + 3 * z
# print(f(2, 3, 4))
#
# #lambda başka fonksiyonların da içine atanabilir.
# nameList = ["Mehmet ali Alabora", "ezgi mola", "halit Ergenç", "haluk Bilginer", "ece uslu", "cüneyt arkın",
#             "ebru Cündübeyoglu"]
# #soyadlarına göre sıralıcaz.
# def sortKey(name):
#     splitList=name.split(" ")
#     return splitList[-1].lower()
#
# nameList.sort(key=sortKey)
# print(nameList)
# #lambda ile yaparsak
# nameList.sort(key=lambda name:name.split(" ")[-1].lower())
# print(nameList)

# employeeList = [
#     ("Ahmet", "Satış", 10000, 0),
#     ("Ezgi", "Hukuk", 8000, 0),
#     ("Elif", "İdari İşler", 5000, 0),
#     ("Mehmet", "Yönetim", 0, 5000)
# ]
# rate=5.95 # dolar kuru, son element dolar maaşı gösteriyor.
# #MAAŞLARINA GÖRE SIRALICAZ
# employeeList.sort(key=lambda employee:employee[2])
# employeeList.sort(key=lambda employee:employee[2] if employee[2] != 0 else employee[3]*rate, reverse=True)
# #print(employeeList)
# #[('Mehmet', 'Yönetim', 0, 5000), ('Ahmet', 'Satış', 10000, 0), ('Ezgi', 'Hukuk', 8000, 0), ('Elif', 'İdari İşler', 5000, 0)]
# print(max(employeeList,key=lambda employee:employee[2] if employee[2] != 0 else employee[3]*rate))
# print(min(employeeList, key=lambda employee:employee[2] if employee[2] != 0 else employee[3]*rate))
# # ('Mehmet', 'Yönetim', 0, 5000)
# # ('Elif', 'İdari İşler', 5000, 0)

def Quadratic(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = Quadratic(2, 3, -4)
print(f(1)) # 1
print(f(2)) # 10
g = Quadratic(3, 2, -2)
print(f(3), g(3)) # 23 31









