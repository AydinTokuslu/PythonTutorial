# Write a function called translate that takes the following
# words and translates them into pig Latin.
# a = 'i love python'
# Here are the rules:
# 1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the
# end. For example, ‘eat’ will become ‘eatyay’
# 2. If a word starts with anything other than a vowel, move
# the first letter to the end and add ‘ay’ to the end. For
# example, ‘day’ will become ‘ayday’.
# Your code should return:
# iyay ovelay ythonpay

def translate(a):
    a=a.split()
    vowels = ["a","e","i","o","u"]
    letter = ""
    for i in a:
        if i[0] in vowels:
            i+="yay"
            letter+= i + " "
        else:
            #pass
            i=i[1::]+i[0]
            i+="ay"
            letter+= i + " "
    print(letter)


a = "i love python"
#a = "i ove opython"
translate(a)

# def pig_latin(a):
#     output = []
#     for i, word in enumerate(a.split()):
#         if word[0] in 'aeiou':
#             output.append(word[i] + 'yay')
#         else:
#             output.append(word[1:] + word[0] + 'ay')
#     return ' '.join(output)

# print(pig_latin('i love python')