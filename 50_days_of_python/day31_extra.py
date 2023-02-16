# Write a function called create_user. This function asks the
# user to enter their name, age, and password. The function
# saves this information in a dictionary. For example, if the use
# enters name as Peter, age - 18 and password - love. The
# function should save the information as: {'name': 'Peter',
# 'age': 18, 'password': 'love'}
# Once the information is saved. The function should print to the
# user that - "User saved. Please login"
# The function should then ask the user to re-enter their name
# and password. If the name and password match with what is
# saved in the dictionary, the function should return "Logged in
# successfully". If the name and password do not match with
# what is saved in the dictionary, the function should print
# ('Wrong password or user name. Please try again'. The
# function should keep running until the user enters correct
# logging details.

def create_user():
    name=input("please enter your name: ")
    age=input("please enter your age: ")
    password=input("please enter your password: ")
    user_list={}
    user_list["name"]=name
    user_list["age"]=age
    user_list["password"]=password
    print("User saved. Please login")
    while True:
        name_2=input("please re-enter your name : ")
        password_2=input("please re-enter your password : ")
        if name_2 in user_list.values() and password_2 in user_list.values():
            print("Logged in successfully")
            break
        else:
            print("Wrong password or user name. Please try again")

create_user()