# Create a function called generate_password that generates any
# length of password for the user. The password should have a
# random mix of upper letters, lower letters, numbers, and
# punctuation symbols. The function should ask the user how
# strong they want the password to be. The user should pick from -
# weak, strong, and very strong. If the user picks weak, the
# function should generate a 5-character long password. If the user
# picks strong, generate an 8-character password and if they pick
# very strong, generate a 12-character password.
import string
import random
def password_generator():
    # string module constants
    a = string.ascii_letters + \
    string.digits + string.punctuation
    password1 =[]
    length = input("Pick your password length "
    "a,b or c: \na. weak \nb.strong \nc."
    "Very strong...: ")
    if length == 'a':
        length = 5
    elif length == 'b':
        length = 8
    elif length == 'c':
        length = 12
    for i in range(length):
        password = str(random.choice(a))
        password1.append(password)
    return 'You password is', ''.join(password1)
print(password_generator())