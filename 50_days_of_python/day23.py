# Create a simple calculator. The calculator should be able to perform
# basic math operations, add, subtract, divide and multiply. The
# calculator should take input from users. The calculator should be
# able to handle ZeroDivisionError, NameError, and ValueError.

import operator
def calculator():
    try:
        num1 = int(input("Enter number: "))
        # asking the user to pick an operator
        opt = input("Pick operator(+,-,*,/) : ")
        num2 = int(input('Enter another number: '))
        if opt not in ['+', '-', '*', '/'] or len(opt) > 1:
            print('Please enter a valid operator')
    except ValueError:
        print('Please enter a valid number')
    except ZeroDivisionError:
         print('You cannot divide a number by zero.Try again')
    else:
        if opt == '+':
            return f'ans is: {operator.add(num1, num2)}'
        elif opt == '-':
            return f'ans is: {operator.sub(num1, num2)}'
        elif opt == '*':
            return f'ans is: {operator.mul(num1, num2)}'
        elif opt == '/':
            return f' ans is: {operator.truediv(num1, num2)}'
    return 'Try again'

print(calculator())






