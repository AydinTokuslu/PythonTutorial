# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
import math

def prime_check(x):
    is_prime = True

    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
            continue
    return is_prime

sayi = 600851475143
biggest_prime = 1
for i in range(2,int(math.sqrt(sayi))):
    if sayi % i == 0 and prime_check(i):
       biggest_prime = i
print(biggest_prime)
