# str1 = "the love is real"
# Write a function called read_backwards that takes a string as
# an argument and reverses it. For example, the string above
# should return: "real is love the"

def read_backwards(s):
    new_str=s.split()
    for i in reversed(new_str):
        print(i, end=" ")

s = "the love is real"
read_backwards(s)