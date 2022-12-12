#  List of Prime Numbers
# Write a function called prime_numbers. This function asks a
# user to enter a number (integer) as an argument and returns a
# list of all the prime numbers within its range. For example, if user
# enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def prime_numbers(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

num = int(input("please enter a number : "))
prime_nums = []

for i in range(2, num):
    if prime_numbers(i):
        prime_nums.append(i)

print(prime_nums)


#
# for i in range(2,sayi+1):
#     if asal_mi(i):
#         asal_sayilar.append(i)
#
# print(asal_sayilar)