# Write a function called string_range that takes a single
# number and returns a string of its range. The string characters
# should be separated by dots(.) For example, if you pass 6 as
# an argument, your function should return ‘0.1.2.3.4.5’.

def string_range():
    number = input("please enter a number : ")
    for i in range(0, int(number)):
        if i == int(number)-1:
            print("{}".format(i), end="")
        else:
            print("{}.".format(i), end="")

string_range()