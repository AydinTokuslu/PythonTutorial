import turtle
import time
import random

hiz = 0.15

pencere = turtle.Screen()
pencere.setup(width=600, height=600)
pencere.title("Yilan Oyunu2")
pencere.bgcolor("red")
pencere.tracer(0)

yilan = turtle.Turtle()
yilan.shape("circle")
yilan.color("yellow")
yilan.penup()
yilan.speed(0)
yilan.goto(0,100)
yilan.direction = "stop"

yemek = turtle.Turtle()
yemek.shape("square")
yemek.color("blue")
yemek.penup()
yemek.speed(0)
yemek.goto(0,0)
yemek.shapesize(0.80, 0.80)

kuyruklar = []
puan = 0

yazPuan = turtle.Turtle()
yazPuan.shape("square")
yazPuan.color("white")
yazPuan.penup()
yazPuan.speed(0)
yazPuan.goto(0,260)
yazPuan.shapesize(0.80, 0.80)
yazPuan.hideturtle()
yazPuan.write("Puan : {}".format(puan), align="center", font=("Courier", 24, "normal"))

def move():
    if yilan.direction == "up":
        y = yilan.ycor()
        yilan.sety(y + 20)
    if yilan.direction == "down":
        y = yilan.ycor()
        yilan.sety(y - 20)
    if yilan.direction == "right":
        x = yilan.xcor()
        yilan.setx(x + 20)
    if yilan.direction == "left":
        x = yilan.xcor()
        yilan.setx(x - 20)

def goUp():
    if yilan.direction != "down":
        yilan.direction = "up"
def goDown():
    if yilan.direction != "up":
        yilan.direction = "down"
def goRight():
    if yilan.direction != "left":
        yilan.direction = "right"
def goLeft():
    if yilan.direction != "right":
        yilan.direction = "left"

pencere.listen()
pencere.onkey(goUp,"Up")
pencere.onkey(goDown,"Down")
pencere.onkey(goRight,"Right")
pencere.onkey(goLeft,"Left")


while True:
    pencere.update()
    if yilan.xcor() > 300 or yilan.xcor() < -300 or yilan.ycor() > 300 or yilan.ycor() < -300:
        yilan.goto(0,0)
        yilan.direction = "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)

            kuyruklar = []
            puan = 0
            yazPuan.clear()
            yazPuan.write("Puan : {}".format(puan), align="center", font=("Courier", 24, "normal"))

            hiz = 0.15

    if yilan.distance(yemek) < 20 :
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        yemek.goto(x, y)

        puan = puan + 10
        yazPuan.clear()
        yazPuan.write("Puan : {}".format(puan), align="center", font=("Courier", 24, "normal"))
        hiz = hiz - 0.001

        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.shape("square")
        yeniKuyruk.color("white")
        yeniKuyruk.penup()
        yeniKuyruk.speed(0)
        kuyruklar.append(yeniKuyruk)
    for i in range(len(kuyruklar)-1, 0, -1):
        x = kuyruklar[i-1].xcor()
        y = kuyruklar[i-1].ycor()
        kuyruklar[i].goto(x,y)
    if len(kuyruklar) > 0:
        x = yilan.xcor()
        y = yilan.ycor()
        kuyruklar[0].goto(x,y)

    move()
    time.sleep(hiz)