# Create a simple calculator. The calculator should be able to perform
# basic math operations, add, subtract, divide and multiply. The
# calculator should take input from users. The calculator should be
# able to handle ZeroDivisionError, NameError, and ValueError.

def calculator():
    print("""
    1-add
    2-subtract
    3-divide
    4-multiply

    """)
    islem=input("Please select a basic math operation: ")
    num1=int(input("enter first number : "))
    num2=int(input("enter second number : "))
    while True:
        if islem=="1":
            try:
                total=num1+num2

            except ValueError:
                print("please ")
        elif islem=="3":
            if num1 != 0 or num2 != 0:
                try:
                    total=num1/num2
                except ZeroDivisionError:
                    print("numbers can't be zero, please enter a number ")


    return total

print(calculator())





