# Task - 5'ler tablosu

# sayi=5
# for i in range(11):
#     print(f"{sayi} x {i} = {sayi * i}")

# number = int(input("enter a number between 1 and 10: "))
# for i in range(11):
#     print(f"{number,i}x{number * i}=")
#     #i += 1

# print(range(5))
# print(*range(5))  # * boşluklu yazdırıyor, 0 1 2 3 4
# print(*("seperate")) # * boşluklu yazdırıyor, s e p e r a t e
# print(*range(10,0,-2)) # * boşluklu yazdırıyor, 10 8 6 4 2
#
# numbers = [0,1,2,3,4,5]
# text = ["zero","one","two","three","four","five"]
#
# for x,y in zip(text, numbers): # index sırasıyla zipler, birleştirir
#     print(x, ":", y)  # zero : 0

# even = []
# odd = []
# for i in range(1,11):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# numbers = [11, 36, 33, 66, 89, 21, 32, 16, 10]
# even = []
# odd = []
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"The number of even numbers : {len(even)}")
# print(f"The number of odd numbers : {len(odd)}")

# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{i}"*j)

# for i in range(1, 10):
#     print(f"{i}" * i)

# names = ["susan", "tom", "edward"]
# mood = ["happy", "sad"]
#
# for i in names:
#     for k in mood:
#         print(f"{i} is {k}")

# for i in range(1,11):
#     for k in range(1,11):
#         print(f"{i} x {k} = {i*k}")
#        print("")

for i in range(1,7):
    for k in range(1,7):
        print((9-k) * " " + "*" * (i+1))
    print("")



# for i in range(10): # piramit
#     print ((9-i) * f" " + (2*i-1)* "*")


