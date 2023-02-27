# list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
#  18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
# Write a function called missing_numbers that takes a list of
# sequence of numbers and finds the missing numbers in the
# sequence. The list above should return:
# [4, 8, 10, 13, 16, 29, 30]

def missing_numbers(list):
    missed_numbers=[]
    for i in range(1,32):
        if i not in list:
            missed_numbers.append(i)
    print(missed_numbers)


list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
missing_numbers(list)