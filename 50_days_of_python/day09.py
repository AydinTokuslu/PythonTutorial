# Create a function called biggest_odd that takes a string of
# numbers and returns the biggest odd number in the list. For
# example, if you pass ‘23569’ as an argument, your function
# should return 9. Use list comprehension.

def biggest_odd(num):
    list_nums = []
    for i in range(len(num)):
        x = int(num) % 10
        list.append(x)
        y = int(num) / 10
        num = y

    print(list_nums)


num = "23569"
biggest_odd(num)