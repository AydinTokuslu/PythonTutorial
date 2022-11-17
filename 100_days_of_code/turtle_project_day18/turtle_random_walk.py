import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():  # rengi random seçmesi için
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

#colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(15)
tim.speed("fastest")

directions = [tim.forward(100), tim.right(90), tim.left(90), tim.back(100)]
directions = [0, 90, 180, 270]

for _ in range(200):
    #tim.color(random.choice(colours))  # rengi biz belirliyoruz, listeye göre
    tim.color(random_color())  # rengi random seçmesi için
    tim.forward(30)
    tim.setheading(random.choice(directions))
