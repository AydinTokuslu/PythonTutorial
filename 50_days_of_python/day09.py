# Create a function called biggest_odd that takes a string of
# numbers and returns the biggest odd number in the list. For
# example, if you pass ‘23569’ as an argument, your function
# should return 9. Use list comprehension.

def biggest_odd(num):
    list_nums = []
    list_nums_int = []
    for i in range(len(num)):
        list_nums.append(num[i])
    print(list_nums)
    for i in range(len(list_nums)):
        list_nums_int.append(int(list_nums[i]))
    print(max(list_nums_int))


num = "23569"

biggest_odd(num)