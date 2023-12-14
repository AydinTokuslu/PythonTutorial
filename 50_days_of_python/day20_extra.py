# str1= 'leArning is hard, bUt if You appLy youRself ' \
#  'you can achieVe success'

# You are given a string of words. Some of the words in the string
# contain uppercase letters. Write a code that will return all the
# words that have an uppercase letter. Your code should return a
# list of the words. Each word in the list should be reversed. Here
# is how your output should look:

# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']

def reversed_list(str):
    new_str=""
    for i in str.split(" "):
        if i.islower():
            continue
        else:
            new_str+=i
            new_str+=" "

    return new_str[::-1]

str1="leArning is hard, bUt if You appLy youRself you can achieVe success"

print(reversed_list(str1))