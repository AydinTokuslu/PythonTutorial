class calisan:
    #def __init__(self,name,surname,age):  # age girilmezse, age default olarak 0 alınır.
    def __init__(self,name,surname="girilmedi",age=0):  # age girilmezse, age default olarak 0 alınır.
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
        print(f"Ad : {self.name}   Soyad : {self.surname}   Yaş : {self.age}")


#calisan1=calisan("Ali","Veli", 20)  # calisan1, instance, nesne
calisan1=calisan("Ali",age=20)  # calisan1, instance, nesne
#print(calisan1.name, calisan1.surname, calisan1.age)

#calisan2=calisan("Ahmet","Mehmet", 25)  # calisan2, instance, nesne
calisan2=calisan("Ahmet","Mehmet")  # calisan2, instance, nesne
#print(calisan2.name, calisan2.surname, calisan2.age)

calisan1.show_info()
calisan2.show_info()