#Write a function called Python_snakes that takes a number
# as an argument and creates the following shape, using the
# number’s range: (hint: Use the loops and emoji library. If you
# pass 7 as argument, your code should print the following: ⠦
#      ⠦
#     ⠦ ⠦
#    ⠦ ⠦ ⠦
#   ⠦ ⠦ ⠦ ⠦
#  ⠦ ⠦ ⠦ ⠦ ⠦
# ⠦ ⠦ ⠦ ⠦ ⠦ ⠦


#🐍

# snake=emoji.emoji_lis("snake")
# print(snake)
def Python_snakes():
    #argument=int(input("please enter argument : "))
    argument=7
    for i in range(1,argument):
        #print("🐍" * i)
        print((argument-i) * " " + "🐍" * i)


Python_snakes()