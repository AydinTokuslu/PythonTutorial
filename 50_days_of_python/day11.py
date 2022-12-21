# Write a function called equal_strings. The function takes two
# strings as arguments and compares them. If the strings are equal
# (if they have the same characters and have equal length), it
# should return True, if they are not, it should return False. For
# example, ‘love’ and ‘evol’ should return True.
import random
from random import choice, choices
def equal_strings(str1,str2):
    ortak_eleman = ""
    #global ortak_eleman
    global random_list
    random_list = []
    if len(str1) == len(str2):
        print("iki kelimenin uzunluğu aynıdır")
        for i in range(len(str1)):
            if str1[i] in str2:
                print("aynı harflere sahiplerdir.")
                ortak_eleman += str1[i]
                #match(ortak_eleman, str2)
            elif str2[i] in str1:
                print("aynı harflere sahiplerdir.")
            else:
                print("aynı harflere sahip değillerdir.")
                return False
        # print("ortak_elemanlar : ", ortak_eleman)

    else:
        print("iki kelimenin uzunluğu aynı değildir")
        return False
    #print("ortak_elemanlar : ", ortak_eleman)
# def match(ortak_eleman, str2):
#     random_list.append(random.choices(ortak_eleman, k=len(ortak_eleman)))
#     print(random_list)
#     if ortak_eleman == str2:
#         print("iki kelime aynı harflere sahiptir.")
#         return True
#     else:
#         print("iki kelime aynı harflere sahip değildir.")

print(equal_strings("love", "eval"))