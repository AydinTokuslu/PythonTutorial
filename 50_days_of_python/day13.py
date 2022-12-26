# Write a function called your_vat. The function takes no
# parameter. The function asks the user to input the price of an
# item and VAT (vat should be a percentage). The function should
# return the price of the item plus VAT. If the price is 220 and,
# VAT is 15% your code should return a vat inclusive price of 253.
# Make sure that your code can handle ValueError. Ensure the
# code runs until valid numbers are entered. (hint: Your code
# should include a while loop)

def your_vat():
    while True:
        try:
            item_price=int(input("please enter the price of the item: "))
            vat=int(input("please enter the vat percentage: "))
            payment=item_price + (item_price*vat/100)
            print(f"You will pay including vat is : {payment}")
            break
        except ValueError:
            print("please enter a valid integer regarding item_price and vat")

your_vat()