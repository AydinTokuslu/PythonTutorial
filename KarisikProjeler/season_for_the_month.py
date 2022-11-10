
# Write a Python program that reads two integers representing a month and day and
# prints the season for that month and day.
# December 21 - March 19 winter.
# March 20 - June 19 spring.
# June 20 - September 20 summer.
# September 21 - December 20 autumn.

# Expected Output:
# Input the month (e.g. January, February etc.): july
# Input the day: 31
# Season is autumn

month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if (month == "December" and day >=21) or (month == "March" and day <= 19) or month == "January" or month == "February":
    print("Season is winter")
elif (month == "March" and day >=20) or (month == "June" and day <= 19) or month == "April" or month == "May":
    print("Season is spring")
elif (month == "June" and day >=20) or (month == "September" and day <= 20) or month == "July" or month == "August":
    print("Season is summer")
elif (month == "September" and day >=21) or (month == "December" and day <= 20) or month == "October" or month == "November":
    print("Season is autumn")
else:
    print("Yanlış değer girdiniz")
