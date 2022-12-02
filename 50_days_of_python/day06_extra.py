# Write a function called zeroed code that takes a list of numbers
# as an argument. The code should zero (0) the first and the last
# number in the list. For example, if the input is [2, 5, 7, 8, 9],
# your code should return [0, 5, 7, 8, 0].

def zeroed(list):
    if list[0] % 2 == 0 or list[0] % 2 == 1:
        list[0] = 0
    if list[-1] %2 == 0 or list[-1] % 2 == 1:
        list[-1] = 0
    return list


number = [2, 5, 7, 8, 9]
print(zeroed(number))