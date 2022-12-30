# Write a function called your_age. This function asks a student
# to enter their , and then it returns their age. For example, if
# a user enters Peter as their name, your function should return,
#  "Hi, Peter, you are 27 years old." This function reads data
# from the database (dictionary below). If the name is not in the
# dictionary, your code should tell the user that their name is not
# in the dictionary, and ask them for their age. Your code should
# then add the name and age to the dictionary of names_age
# below. Once added your code should return to the user ‘Hi,
# (added name), you are (added age) years old’. Remember
# to convert the input from user to lowercase letters
# names_age = {"jane": 23, "kerry": 45, "tim": 34, “peter": 27}


names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}

def your_age():
    name=input("please enter your name : ")
    if name in names_age.keys():
        age = names_age[name]
    else:
        age=int(input("please enter your age : "))
        names_age[name]=age
    return f"Hi, {name}, you are {age} years old."

print(your_age())
