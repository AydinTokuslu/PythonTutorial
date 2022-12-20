# Write a function called equal_strings. The function takes two
# strings as arguments and compares them. If the strings are equal
# (if they have the same characters and have equal length), it
# should return True, if they are not, it should return False. For
# example, ‘love’ and ‘evol’ should return True.

def equal_strings(str1,str2):
    ortak_eleman = []
    if len(str1) == len(str2):
        print("iki kelimenin uzunluğu aynıdır")
        for i in range(len(str1)):
            if str1[i] in str2:
                print("ortak eleman vardır.")
                ortak_eleman.append(str1[i])
                return True
            else:
                print("ortak eleman bulunmamaktadır.")
                return False
        print("ortak_elemanlar : ", ortak_eleman)

    else:
        print("iki kelimenin uzunluğu aynı değildir")
        return False



print(equal_strings("love", "evol"))