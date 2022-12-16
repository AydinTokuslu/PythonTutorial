# Write a function called zeros_last. This function takes a list as
# argument. If a list has zeros (0), it will move them to the front of
# the list and maintain the order of the other numbers in the list.
# If there are no Zeros in the list, the function should return the
# original list sorted in ascending order. For example, if you pass
# [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
# 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
# your code should return [1, 2, 4, 6, 7].


numbers = [1, 4, 6, 0, 7,0,9]
def zeros_last(*nums):
    last_list = []
    count_zero = 0
    if 0 in nums:
        for i in nums:
            #last_list.append(i)
            if i == 0:
                count_zero +=1
            else:
                 last_list.append(i)
        for i in range(count_zero):
            last_list.append(0)
    else:
        for i in nums:
            last_list.append(i)
            last_list.sort()
    return last_list



#numbers = [1, 4, 6, 0, 7,0,9]
#numbers = [2, 1, 4, 7, 6]
print(zeros_last(*numbers))