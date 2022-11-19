# color = "mor"
# other_color = ""
#
# match color:
#     case "sari":
#         print("seçtiğim renk sarıdır")
#     case "mavi":
#         print("seçtiğim renk mavidir.")
#     case other_color:
#         print(f"seçtiğim renk {other_color}")

# color = ("sari", "siyah", "pembe")  # tuple içeriği birebir aynı seçeneklerde bulunması gerekiyor.
# other_color = ""
# match color:
#     case ("sari",):
#         print("seçtiğim renk sarıdır")
#     case ("mavi", "sari") | ("siyah", "mor"):
#         print("seçtiğim renk mavi veya siyahdır.")
#     case ("mavi", other_color, "pembe"):
#         print(f"seçtiğim renk {other_color}")
#     case (_, "siyah", "pembe"):  "_" : ne gelirse gelsin demek
#         print("seçtiğim renkler siyah ve pembedir.")
#     case ("mavi", *other_color):
#         print(f"seçtiğim renk {other_color}")

# my_dict = {"a" :  1, "b" : 2, "c" : 3}
#
# match my_dict:
#     case {"a" :1, **rest} as result:
#         print(rest)  # ilk elementten sonra gerisini rest'e at, {'b': 2, 'c': 3}
#         print(result) # hepsini result'a gönder, {'a': 1, 'b': 2, 'c': 3}

# my_dict = {"user_name": "python",
#            "first_name": "ferhat",
#            "last_name":"mousavi"
#            }
# match my_dict:  # dict içeriğinden hangileri kaç tane varsa bulduğuna gider.
#     #case {"first_name": "ferhat", "last_name":"mousavi"}:
#     case {"first_name": first_name, "last_name":last_name}:
#         print("isim soyisim bulundu", first_name, last_name)
#     #case {"user_name": "python"}:
#     case {"user_name": user_name}:
#         print("kullanıcı adı bulundu", user_name)
#     case _:
#         print("isim soyisim bulunamadı")

# number = 3
#
# match number:
#     case _ as result if result % 2 == 0: # "_" : ne gelirse gelsin demek
#         print(result, "ikiye bölünüyor")
#     case _ as result if result % 3 == 0: # "_" : ne gelirse gelsin demek
#         print(result, "üçe bölünüyor")
#     case _ as result if result % 4 == 0: # "_" : ne gelirse gelsin demek
#         print(result, "beşe bölünüyor")

# while True:
#     match input("bir harf giriniz : ").lower():
#         case "a":
#             print("bazı işler yap")
#         case "b":
#             print("başka işler yap")
#         case "q":
#             print("çıkıyorum")
#             break
#         case _:
#             print("bulamadım gitti")

while True:
    my_number = int(input("bir sayı giriniz : "))
    match my_number, my_number% 10 :
        case _, 1:
            print("birler basamağı 1 dir.", my_number)
        case number, 5 if number > 100:
            print("sayı 100 den büyük ve birler basamağı 5 dir", my_number)
        case _:
            break


















