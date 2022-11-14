# class variables - instance variable
# sınıf değişkeni - nesne değişkeni

class calisan:
    personel_sayisi = 0  # class variable yazarak tüm class'ta geçerli olmuş oldu
    #zam_orani = 1.1  # class variable
    def __init__(self,isim, maas):
        self.isim = isim
        self.maas = maas
        calisan.personel_sayisi += 1  # self ile yapsaydık, instance variable'a ait olurdu


print(calisan.personel_sayisi)  # 0
calisan1 = calisan("Ali", 5000)
print(calisan.personel_sayisi)  # 1
calisan2 = calisan("Ahmet", 6000)
print(calisan.personel_sayisi)  # 2

#print(calisan1.__dict__)  # {'isim': 'Ali', 'maas': 5000}, calisan1 instance variable
#print(calisan2.__dict__)  # {'isim': 'Ahmet', 'maas': 6000}, calisan2 instance variable

# print(calisan.zam_orani)  # 1.1
# print(calisan1.zam_orani)  # 1.1

# calisan.zam_orani = 1.2
# print(calisan.zam_orani)  # 1.2
# print(calisan1.zam_orani)  # 1.2
# print(calisan2.zam_orani)  # 1.2

# calisan1.zam_orani = 1.2
# # print(calisan.zam_orani)  # 1.1
# # print(calisan1.zam_orani)  # 1.2
# # print(calisan2.zam_orani)  # 1.1
#
# print(calisan1.__dict__)  # {'isim': 'Ali', 'maas': 5000, 'zam_orani': 1.2}
# print(calisan2.__dict__)   # {'isim': 'Ahmet', 'maas': 6000}