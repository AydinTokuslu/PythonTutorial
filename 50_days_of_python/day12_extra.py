# Write a function called age_in_minutes that tells a user how
# old they are in minutes. Your code should ask the user to
# enter their year of birth, and it should return their age in
# minutes (by subtracting their year of birth to the current year).
# Here are things to look out for:
# a. The user can only input a 4-digit year of birth. For
# example, 1930 is a valid year. However, entering any
# number longer or less than 4 digits long should render
# input invalid. Notify the user to input a four digits
# number.
# b. If a user enters a year before 1900, your code should
# tell the user that input is invalid. If the user enters the
# year after the current year, the code should tell the user,
# to input a valid year.
# The code should run until the user inputs a valid year.
# Your function should return the user's age in minutes. For
# example, if someone enters 1930, as their year of birth your
# function should return:
# You are 48,355,200 minutes old.
import datetime

today=datetime.date.today().year
#print(today)
def age_in_minutes():
    birth=True
    while birth:
        age=input("please enter 4-digit year of your birth : ")
        if len(age) == 4:
            if int(age) < 1900:
                print("the input is invalid, please enter a valid year after 1900")
                # birth = False
            elif int(age) > int(today):
                print("please enter a valid year, not passing this year")
            else:
                your_age=int(today)-int(age)
                your_age=your_age*12*30*24*60
                print(f"you are {your_age} minutes old.")
                birth = False
        else:
            print("please enter 4 digit year of birth")
            # birth=False

age_in_minutes()