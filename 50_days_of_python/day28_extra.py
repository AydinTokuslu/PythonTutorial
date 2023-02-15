# Write a function called largest_number that takes a list of
# integers and re-arrange the individual digits to create the largest
# number possible. For example, if you pass the following as an
# argument: list1 = [3, 67, 87, 9, 2]. Your code should return the
# number in this exact format: 9,877,632 as the largest number.

def largest_number(list1):
    number = ""
    max = 0
    num_list = []
    for i in list1:
        # print(sorted(list1))
        if i % 2 == 0 or i % 2 == 1:
            sayi1 = i // 10
            sayi2 = i % 10
            num_list.append(sayi1)
            num_list.append(sayi2)
        else:
            num_list.append(i)
    num_list = sorted(num_list)
    for i in num_list[::-1]:
        if i != 0:
            number += str(i)

    print(number)


list1 = [3, 67, 87, 9, 2]
largest_number(list1)