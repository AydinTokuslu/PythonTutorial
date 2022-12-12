#  Odd and Even
# Write a function called odd_even that has one parameter and
# takes a list of numbers as an argument. The function returns the
# difference between the largest even number in the list and the
# smallest odd number in the list. For example, if you pass
# [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(list):
    max = 0
    min = 1000
    for i in list:
        if i % 2 == 0:
            if i > max:
                max = i
        else:
            if i < min:
                min = i
    return max - min


list2 = [1,2,4,6,7,42,88]
print(odd_even(list2))