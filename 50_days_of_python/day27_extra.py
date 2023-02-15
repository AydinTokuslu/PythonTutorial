# Write a function called difference that takes two lists as
# arguments. This function should return all the elements that are
# in list a but not in list b and all the elements in list b not in list
# a. For example:
# list1 = [1, 2, 4, 5, 6]
# list2 = [1, 2, 5, 7, 9]
# should return:
# [4, 6, 7, 9]
# Use list comprehension in your function.

def difference(list1,list2):
    unique_numbers=[]
    for i in list1:
        if i not in list2:
            unique_numbers.append(i)
    for i in list2:
        if i not in list1:
            unique_numbers.append(i)

    print(unique_numbers)




list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
difference(list1,list2)