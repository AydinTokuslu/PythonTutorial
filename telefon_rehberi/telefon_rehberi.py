


def kayitlari_listele():
    read_file()
    #print(f"Rehberdeki Kayıt Sayısı : {}")  # bu çalışmıyor.

def kayit_ara(name, surname):
    print("Kayıt Arama Bölümü")
    name = print("aramak istediğiniz kişinin ismini giriniz : ")
    records_list = read_file()
    if name in records_list:
       kayitlari_listele()

def read_file():
    with open("kayit_listesi.txt","r", encoding="utf-8") as file:
        kayitlar = file.readlines()
        for kayit in kayitlar:
            kayit = kayit.replace("\n","")
            kayit = kayit.split()
            name = kayit[0]
            surname = kayit[1]
            tel_number = kayit[2]
            print(f"{name} {surname} {tel_number}")

name = ""
surname = ""
tel_number = ""

records_list = []
def kayit_ekle():
    print("Yeni Kayıt Ekle")
    global name
    global surname
    global tel_number
    name = input("İsim : ")
    surname = input("Soyisim : ")
    tel_number = input("Telefon numarası : ")
    print(f"Yeni kayıt : {name} {surname} {tel_number}\nYeni Kayıt Eklendi")
    kayit_dict = {"name": name, "surname": surname, "tel number": tel_number}
    records_list.append(kayit_dict)
    with open("kayit_listesi.txt","a", encoding="utf-8") as file:
        file.write(name+" "+surname+" "+tel_number+" "+"\n")



def kayit_sil():
    print("Kayıt Silme Bölümü")
    name = print("silmek istediğiniz kişinin ismini giriniz : ")
    kayitlar = read_file()
    if name in kayitlar:
        kayitlari_listele()


def menu():
    while True:
        print("""
    1-Kayıtları Listele
    2-Kayıt Ara
    3-Kayıt Ekle
    4-Kayıt Sil
    5-Çıkış
    
        """)
        option = input("Lütfen tercihinizi giriniz >>  ")
        if option == "1":
            kayitlari_listele()
        elif option == "2":
            kayit_ara(name, surname)
        elif option == "3":
            kayit_ekle()
        elif option == "4":
            kayit_sil()
        elif option == "5":
            exit()
        else:
            print("Yanlış tercihte bulundunuz, tekrar deneyiniz")



menu()