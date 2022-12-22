# Write a function called swap_values. This function takes a list
# of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4,67, 7] as a parameter, your
# function should return
# [7, 4, 67, 2].

def swap_values(list):
    temp = list[0]
    last = list[-1]
    new_list=[]
    new_list.append(last)
    for i in range(len(list)-1):
        list[i] = list[i+1]
        new_list.append(list[i])
    new_list[-1] = temp

    print(new_list)

x = [2, 4,67, 7,5]
swap_values(x)