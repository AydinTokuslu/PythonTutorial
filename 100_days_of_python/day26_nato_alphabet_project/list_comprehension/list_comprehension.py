# numbers = [1, 2, 3]
# new_numbers = [n +1 for n in numbers]
# print(new_numbers)  # [2, 3, 4]
# name = "angela"
# letters_list = [letter for letter in name]
# num = [n*2 for n in range(1, 5)]
# print(num)  # [2, 4, 6, 8]
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)  # ['Alex', 'Beth', 'Dave']
# print(upper_names)  # ['CAROLINE', 'ELEANOR', 'FREDDIE']

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]