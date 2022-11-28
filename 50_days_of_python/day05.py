# Create a function called my_discount. The function takes no
# arguments but asks the user to input the price and the
# discount (percentage) of the product. Once the user inputs the
# price and discount, it calculates the price after the discount.
# The function should return the price after the discount. For
# example, if the user enters 150 as price and 15% as the discount,
# your function should return 127.5.

def my_discount():
    price = int(input("Please enter the price : "))
    discount = int(input("Please enter the discount : "))/100
    last_price = price - (price * discount)
    return f"last_price that you should pay is : {last_price}"

print(my_discount())