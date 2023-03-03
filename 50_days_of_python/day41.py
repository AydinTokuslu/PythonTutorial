# Create a function called words_with_vowels, this function
# takes a string of words and returns a list of only words that
# have vowels in them. For example, ‘You have no rhythm’ should
# return [‘You’,’have’, ‘no’].

def words_with_vowels(a):
    vowels = ["a","e","i","o","u"]
    new_list=[]
    a=a.split()
    for i in a:
        for j in vowels:
                if j in i:
                    if i not in new_list:
                        new_list.append(i)
    print(new_list)


a="You have no rhythm"
words_with_vowels(a)