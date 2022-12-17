# Write a function called hide_password that takes no
# parameters. The function takes an input (a password) from a
# user and returns a hidden password. For example, if the user
# enters ‘hello’ as a password the function should return ‘****’ as
# a password and tell the user that the password is 4 characters
# long.


def hide_password(str):

    hide_str = ""
    for i in range(len(str)):
        hide_str += "*"
    print(hide_str)
    return f"The password is {len(str)} characters long\nYour password is {hide_str}"

password=input("please enter a password : ")
print(hide_password(password))