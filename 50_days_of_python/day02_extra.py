# Write a function called check_duplicates that takes a list of
# strings as an argument. The function should check if the list has
# any duplicates. If there are duplicates, the function should return
# the duplicates. If there are no duplicates, the function should
# return "No duplicates". For example, the list of fruits below
# should return apple as a duplicate and list of names should
# return "no duplicates".
# fruits = ['apple', 'orange', 'banana', 'apple']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def check_duplicates(list):
    dublicate = []
    for i in list:
        #print(i)
        dublicate.append(i)
    if i in dublicate:
        return i
    else:
        return "no dublicates"

fruits = ['orange', 'apple', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(check_duplicates(names))