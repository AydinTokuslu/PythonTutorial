# magic methodlar, python'da gömülü özel fonksiyonlardır.  __ le başlarlar.
# Yaptıkları iş, bir class tanımladığımızda onun üzerinde yapılablecek işlemleri belirlememizi sağlar.
# 2 tane önemli magic fonksiyon : __str__ ve __repr__
# __str__ ve __repr__ : Oluşturduğumuz class'dan ürettiğimiz bir nesnenin nasıl string'e dönüştürüleceği,
# yani yazdır dediğimizde ekrana nasıl yazdırılacağını belirtir, kullanımları farklıdır.
# __str__ : kullanıcı için, __repr__ : kod yazan kendimiz için

# from datetime import date
# # a = "Python"
# # print(str(a))  # Python
# # print(repr(a))  # 'Python'
#
# bugun = date.today()
# print(bugun)  # 2022-11-14
# print(str(bugun))  # 2022-11-14
# print(repr(bugun))  # datetime.date(2022, 11, 14)

class Futbolcu:
    def __init__(self, isim, soyisim, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
    def __str__(self):
        return f"Ad : {self.isim}, Soyad : {self.soyisim}, Yaş : {self.yas}"

    def __repr__(self):
        return f"Futbolcu({self.isim}, {self.soyisim}, {self.yas})"

futbolcu1 = Futbolcu("Ali", "Veli", 20)
print(futbolcu1)  # <__main__.Futbolcu object at 0x000001E33032BFD0>, adresini gösterir.
# istediğimiz string igib yazdırmak için __str__ magic methodu kullanırız.
# print fonksyonunun birinci tercihi __str__ olur, bulamazsa __repr__'i kullanır.
print(futbolcu1.__repr__())  # nesne üzerinden de çağırabiliriz ,nesneyi tekrar oluştururuz


