# Write a function called check_pangram that takes a string
# and checks if it is a pangram. A pangram is a sentence that
# contains all the letters of the alphabet. If it is a pangram,
# the function should return True, otherwise, return False. The
# following sentence is a pangram so it should return True:
# 'the quick brown fox jumps over a lazy dog'

def check_pangram(a):
    a = a.replace(" ", "")
    list_a = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

    for i in a:
        if i not in list_a:
            list_a.append(i)
    list_a.sort()
    print(list_a)
    if list_a == letters:
        return True
    else:
        return False


# a="the quick brown fox jumps over a lazy dog"
a = "the quick brown fox jumps over a lazy"
print(check_pangram(a))