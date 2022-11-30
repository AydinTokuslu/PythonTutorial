from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# for _ in range(50):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.left(90)         #kesik çizgiler çizdirmek

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):    # üçgen, dörtgen, beşgen, altıgen, yedigen ... vb çizdirmek
#     angle = 360 / num_sides  # kenar köşe sayısına göre açıyı buluyoruz.
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#
# for shape_sides_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_sides_n)












screen = Screen()
screen.exitonclick()