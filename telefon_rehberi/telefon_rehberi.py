


def kayitlari_listele():
    read_file()
    #print(f"Rehberdeki Kayıt Sayısı : {}")  # bu çalışmıyor.

def kayit_ara():
    print("Kayıt Arama Bölümü")
    aranan_isim = print("aramak istediğiniz kişinin ismini giriniz : ")
    if aranan_isim in records_list:
        print(f"{name} {surname} {tel_number}")

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
    #kayit_dict = {"name": name, "surname": surname, "tel number": tel_number}
    #records_list.append(kayit_dict)
    with open("kayit_listesi.txt","a", encoding="utf-8") as file:
        file.write(name+" "+surname+" "+tel_number+" "+"\n")
        records_list.append(file)



def kayit_sil():
    print("Kayıt Silme Bölümü")
    name = print("silmek istediğiniz kişinin ismini giriniz : ")
    kayitlar = read_file()
    if name in kayitlar:
        kayitlari_listele()


# def menu_loop():
#     while True:
#         display_menu()
#         option = input("Seçenek (1-5): \n")
#         if option.isdigit() and 1 <= int(option) <= 5:
#             break
#     return option


def display_menu():
    print("""
1-Kayıtları Listele
2-Kayıt Ara
3-Kayıt Ekle
4-Kayıt Sil
5-Çıkış
""")
def main_loop():
    while True:
        display_menu()
        #option = menu_loop()
        option = input("Seçenek (1-5): ")
        if option == "1":
            kayitlari_listele()
        elif option == "2":
            kayit_ara()
        elif option == "3":
            kayit_ekle()
        elif option == "4":
            kayit_sil()
        elif option == "5":
            break


main_loop()