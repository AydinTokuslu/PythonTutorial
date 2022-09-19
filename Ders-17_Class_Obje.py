class Araba():

    def __init__(self,marka,model,fiyat,renk): # constructor
        self.gelenMarka=marka
        self.gelenModel=model
        self.gelenFiyat=fiyat
        self.gelenRenk=renk
        #print("araba oluştu")

    #marka="Renault"
    #model="Clio"
    #fiyat=50_000
    #renk="Kirmizi"

    def bilgieriYazdir(self):
        #print(self.marka,self.model,self.fiyat,self.renk)
        print(self.gelenMarka,self.gelenModel,self.gelenFiyat,self.gelenRenk)

    def renkDegistir(self,renk):
        self.gelenRenk=renk

#araba=Araba()
#deneme=Araba()

araba1=Araba("Ford","Fiesta",30000,"Mavi")
araba2=Araba("Renault","Clio",50000,"Kirmizi")

araba1.bilgieriYazdir()
araba1.renkDegistir("Siyah")
araba1.bilgieriYazdir()
araba2.bilgieriYazdir()
#print(araba.renk)

#araba.bilgieriYazdir()
#deneme.bilgieriYazdir()
