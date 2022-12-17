# Extra Challenge: A Thousand Separator

# Your new company has a list of figures saved in a list. The issue
# is that these numbers have no separator. The numbers are
# saved in the following format:
# [1000000, 2356989, 2354672, 9878098].

# You have been asked to write a code that will convert each of the
# numbers in the list into a string. Your code should then add a
# comma on each number as a thousand separator for
# readability. When you run your code on the above list, your
# output should be:

# [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]

# Write a function called convert_numbers that will take one
# argument, a list of numbers above.



def convert_numbers(numbers):
    str_numbers_list = ""
    str_numbers_list_2 = []
    for i in range(len(numbers)):
        b = numbers[i] % 1000
        if b == 0:
            b = "000"
        elif b < 100:
             b = "0" + str(b)
        numbers[i] = numbers[i] // 1000
        c = numbers[i] % 1000
        if c == 0:
            c = "000"
        elif c < 100:
             c = "0" + str(c)
        numbers[i] = numbers[i] // 1000
        str_numbers_list = str(numbers[i])+"," + str(c) +","+ str(b)
        #print(str_numbers_list)
        str_numbers_list_2.append(str_numbers_list)
    print(str_numbers_list_2)


numbers = [1000000, 2356989, 2354672, 9878098, 3056470, 4550605]
convert_numbers(numbers)