# Write a function called password_validator. The function
# asks the user to enter a password. A valid password should have
# at least one upper letter, one lower letter, and one
# number. It should not be less than 8 characters long. When
# the user enters a password, the function should check if the
# password is valid. If the password is valid, the function should
# return the valid password. If the password is not valid, the
# function should tell the users the errors in the password and
# prompt the user to enter another password. The code should
# only stop once the user enters a valid password. (use while loop).

def password_validator():
    errors = []
    while True:
        password = input('Enter your password: ')
        if not any(i.isupper() for i in password):
            errors.append("Please add at least one "
                          "capital letter to your password")
        elif not any(i.islower() for i in password):
            errors.append("Please add at least one "
                          "small letter to your password")
        elif not any(i.isdigit() for i in password):
            errors.append('Please add at least one '
                          'number to your password')
        elif len(password) < 8:
            errors.append("Your password is less "
                          "than 8 characters")
        if len(errors) > 0:
            print('Check the following errors:')
            print(str(errors))
            del errors[0:]
        else:
            return f'Your password is {password}'


print(password_validator())