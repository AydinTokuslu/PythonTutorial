# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
# groceries = zip(fruits, quantities, prices)
# print(list(groceries))
# [('Apples', 5, 1.5), ('Oranges', 3, 2.25), ('Bananas', 4, 0.89)]

# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
# output=[]
# fruit_tuple_0 = (fruits[0], quantities[0], prices[0])
# output.append(output)
# fruit_tuple_1 = (fruits[1], quantities[1], prices[1])
# output.append(output)
# fruit_tuple_2 = (fruits[2], quantities[2], prices[2])
# output.append(output)
# print(fruit_tuple_0, fruit_tuple_1, fruit_tuple_2)
# # ('Apples', 5, 1.5) ('Oranges', 3, 2.25) ('Bananas', 4, 0.89)

# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
# i = 0
# output = []
# for fruit in fruits:
#      temp_qty = quantities[i]
#      temp_price = prices[i]
#      output.append((fruit, temp_qty, temp_price))
#      i += 1
# print(output)
# # [('Apples', 5, 1.5), ('Oranges', 3, 2.25), ('Bananas', 4, 0.89)]

# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
# i = 0
# output = []
# for fruit in fruits:
#       for qty in quantities:
#           for price in prices:
#                output.append((fruit, qty, price))
#       i += 1
# print(output)
# [('Apples', 5, 1.5), ('Apples', 5, 2.25), ('Apples', 5, 0.89), ('Apples', 3, 1.5), ('Apples', 3, 2.25), ('Apples', 3, 0.89), ('Apples', 4, 1.5), ('Apples', 4, 2.25), ('Apples', 4, 0.89), ('Oranges', 5, 1.5), ('Oranges', 5, 2.25), ('Oranges', 5, 0.89), ('Oranges', 3, 1.5), ('Oranges', 3, 2.25), ('Oranges', 3, 0.89), ('Oranges', 4, 1.5), ('Oranges', 4, 2.25), ('Oranges', 4, 0.89), ('Bananas', 5, 1.5), ('Bananas', 5, 2.25), ('Bananas', 5, 0.89), ('Bananas', 3, 1.5), ('Bananas', 3, 2.25), ('Bananas', 3, 0.89), ('Bananas', 4, 1.5), ('Bananas', 4, 2.25), ('Bananas', 4, 0.89)]

# a=[1,2,3,4]
# b=[sum(a[0:x+1]) for x in range(0,len(a))]
# print(b)

# L1 = []
# L1.append([1, [2, 3], 4])
# L1.extend([7, 8, 9])
# print(L1)
# print(L1[0][1][1] + L1[2])
# 11

# T = (1, 2, 3, 4, 5, 6, 7, 8)
# print(T[T.index(5)], end = " ")
# print(T[T[T[6]-3]-6])
# # 5 8

# D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}
# D['1'] = 2
# print(D[D[D[str(D[1])]]])
# # 3

# set1 = {1, 2, 3}
# set2 = set1.copy()
# set2.add(4)
# print(set1)
# # {1, 2, 3}













