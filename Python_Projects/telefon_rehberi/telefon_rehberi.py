import pickle
import os


def display_menu():
    print("""
1-Kayıtları Listele
2-Kayıt Ara
3-Kayıt Ekle
4-Kayıt Sil
5-Çıkış
 
""")

records_list = [] #list()
def menu_loop():
    while True:
        display_menu()
        option = input("Seçenek (1-5): \n")
        if option.isdigit() and 1 <= int(option) <= 5:
            break
    return option


def main_loop():
    while True:
        option = menu_loop()
        if option == "1":
            list_records()
        elif option == "2":
            search_records()
        elif option == "3":
            add_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            break




def search_records():
    print("Kayıt Arama")
    name = input("İsim : ")
    surname = input("Soyisim : ")
    records_list = search_record_from_file(name, surname)
    print("Telefon Numarası : ", end="")
    for record in records_list:
        print(f"{record.get('tel_number'):11:11}", end="")
    print("\n")


def add_record():
    print("Yeni Kayıt Ekle")
    name = input("İsim : ")
    surname = input("Soyisim : ")
    tel_number = input("Telefon Numarası : ")
    print(f"Yeni kayıt : {name} {surname} - {tel_number}")
    if are_you_sure():
        add_record_file(name, surname, tel_number)
        print("Kayıt Eklendi\n")




def delete_record():
    print("Kayıt Silmek")
    name = input("İsim : ")
    surname = input("Soyisim : ")
    records_list = search_record_from_file(name, surname)
    print("Telefon Numarası : ", end="")
    for record in records_list:
        print(f"{record.get('tel_number'):11:11}", end="")
    print("\n")
    if are_you_sure():
        delete_records_from_file(records_list)
        print("Kayıt Silindi")

def are_you_sure():
    while True:
        answer = input("Emin misiniz? (E)vet/(H)ayır)\n")
        if answer.upper() == "E":
            return True
        elif answer.upper() == "H":
            return False

def read_file():
    with open("data.txt", "r") as dosya:
        bilgiler = dosya.readlines()
        for bilgi in bilgiler:
            bilgi = bilgi.replace("\n", "")
            bilgi = bilgi.split(" ")
            name = bilgi[0]
            surname = bilgi[1]
            tel_number = bilgi[2]
            #print(name)
            #print(surname)
            #print(tel_number)

def list_records():
    #records_list = read_file()
    print(f"Kayıt Sayısı : {len(records_list)}\n")
    print(f"{'isim':^10} {'soyisim':^10} {'Telefon':^11}")
    for record in records_list:
        print(f"{record.get('name', ' '):10.10} {record.get('surname', ' '):10.10} {record.get('tel_number', ' '):11.11}")
    print()  # :10.10 = 10'a tamamla, 10'dan fazlaysa kes, 10 olsun


def write_file(name, surname, tel_number):
    dosya = open("data.txt","a", encoding="utf-8")
    dosya.writelines(name+" "+ surname+" "+ tel_number+"\n")
    dosya.close()


def add_record_file(name, surname, tel_number):
    record_dict = {"name" : name, "surname" : surname, "tel_number" : tel_number}
    records_list.append(record_dict)
    write_file(name, surname, tel_number)


def search_record_from_file(name, surname):
    records_list = read_file()
    response_list = []
    for record in records_list:
        if record.get("name").upper() == name.upper() and\
            record.get("surname").upper() == surname.upper():
            response_list.append(record)
    return response_list


def delete_records_from_file(records_list):
    records_list = read_file()
    for record in records_list:
        for record_for_delete in records_list:
            if record.get("name") == record_for_delete.get("name") and \
                    record.get("surname") == record_for_delete.get("surname"):
                records_list.remove(record_for_delete)
    write_file(records_list)


main_loop()