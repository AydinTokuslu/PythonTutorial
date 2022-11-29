from turtle import Turtle, Screen
import random


screen = Screen()
is_race_on = False
screen.setup(width=500, height=500)
screen.title("Turtle Race")
#screen.bgcolor("yellow")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? : ")
print(user_bet)
colors = ["blue", "yellow", "red", "black", "purple", "green", "orange"]
all_turtles = []
y_positions = [-100, -60, -20, 20, 60, 100, 140]

for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()