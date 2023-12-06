# Write a function called word_index that takes one argument,
# a list of strings and returns the index of the longest word in the
# list. If there is no longest word (if all the strings are of the same
# length), the function should return zero (0). For example, the list
# below should return 2.
# words1 = ["Hate", "remorse", "vengeance"]
#  And this list below, should return zero (0)
# words2 = ["Love", "Hate"]

def word_index(list):
    max = 0
    for i in list:
        if len(i) > max:
            max = len(i)
    return list.index(i)


words1 = ["Hate", "remorse", "vengeance","elvedaistanbul"]
words2 = ["Love", "Hate"]
print(word_index(words1))
print(word_index(words2))