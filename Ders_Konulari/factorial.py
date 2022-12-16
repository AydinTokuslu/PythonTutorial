from math import factorial

integers = [1, 2, 3, 4, 5]

def calculate(*args):
    result = 0
    if args: # fonksiyon içinde args varsa
        for integer in args:
            result += factorial(integer) / integer
    return result  # result = 1 factorial/1, 2 factorial/2, 3 factorial/3...

print(calculate(*integers))  # 34