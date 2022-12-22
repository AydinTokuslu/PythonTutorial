# Write a function called equal_strings. The function takes two
# strings as arguments and compares them. If the strings are equal
# (if they have the same characters and have equal length), it
# should return True, if they are not, it should return False. For
# example, ‘love’ and ‘evol’ should return True.

def equal_strings(str1,str2):
    farkli_eleman = ""
    global random_list
    random_list = []
    if len(str1) == len(str2):
        print("iki kelimenin uzunluğu aynıdır")
        for i in range(len(str1)):
            if str1[i] not in str2:
                farkli_eleman += str1[i]
            elif str2[i] not in str1:
                farkli_eleman += str2[i]
    else:
        print("iki kelimenin uzunluğu aynı değildir")
        return False

    if len(farkli_eleman) == 0:
        print("iki kelime aynı harflere sahiptir.")
        return True
    else:
        print("iki kelime aynı harflere sahip değildir.")
        return False

print(equal_strings("love", "evol"))