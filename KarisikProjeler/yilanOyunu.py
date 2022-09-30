import turtle
import time
import random

hiz = 0.15

pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("lightgreen")
pencere.setup(width=600, height=600)
pencere.tracer(0) #pencereyi güncellemeyi engelliyoruz.

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("black")
kafa.penup()#çizim yapmayacak, yazı yazmayacak sadece hareket edecek demek
kafa.goto(0,100)#0a 100 noktasına götürüyoruz.
kafa.direction = "stop" #kafa şu an duruyor.

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()#çizim yapmayacak, yazı yazmayacak sadece hareket edecek demek
yemek.goto(0,0)#0a 100 noktasına götürüyoruz.
yemek.shapesize(0.80,0.80)

kuyruklar = []
puan = 0

yazPuan = turtle.Turtle()
yazPuan.speed(0)
yazPuan.shape("square")
yazPuan.color("white")
yazPuan.penup()#çizim yapmayacak, yazı yazmayacak sadece hareket edecek demek
yazPuan.goto(0,260)#0a 100 noktasına götürüyoruz.
yazPuan.shapesize(0.80,0.80)
yazPuan.hideturtle()
yazPuan.write("Puan : {}".format(puan), align="center", font=("Courier", 24, "normal"))

#hareket sistemini oluşturucaz, fonksiyon oluşturuyoruz.
def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

def goUp():
    if kafa.direction != "down":
        kafa.direction = "up"

def goDown():
    if kafa.direction != "up":
        kafa.direction = "down"

def goRight():
    if kafa.direction != "left":
        kafa.direction = "right"

def goLeft():
    if kafa.direction != "right":
        kafa.direction = "left"

pencere.listen()
pencere.onkey(goUp, "Up")#pencerede yukarı tuşuna basılmışsa o işlemi yapsın diye
pencere.onkey(goDown, "Down")#pencerede aşağı tuşuna basılmışsa o işlemi yapsın diye
pencere.onkey(goRight, "Right")#pencerede sağ tuşuna basılmışsa o işlemi yapsın diye
pencere.onkey(goLeft, "Left")#pencerede sol tuşuna basılmışsa o işlemi yapsın diye



while True:
    pencere.update()

    #kafa duvarlara çarparsa, merkezde tekrar başlasın diye
    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0,0)
        kafa.direction = "stop"
    #kuyrukları ekrandan/pencereden dışarı taşıyoruz.
        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)
        #kenara çarpınca kuyruk ve puan sıfırlansın
        kuyruklar = []
        puan = 0
        yazPuan.clear()
        yazPuan.write("Puan : {}".format(puan), align="center", font=("Courier", 24, "normal"))

        hiz = 0.15


    if kafa.distance(yemek) < 20:#ikisinin arasındaki mesafe 20 pikselden az ise çarpışma var demektir.
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        yemek.goto(x,y)

        puan = puan + 10 #yedikçe 10 puan artsın
        yazPuan.clear()
        yazPuan.write("Puan : {}".format(puan), align="center", font=("Courier", 24, "normal"))

        hiz = hiz - 0.001

        yeniKuyruk=turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape("square")
        yeniKuyruk.color("white")
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

    for i in range(len(kuyruklar) - 1, 0 , -1):#kuyruklar birbirinin yerine geçiyor.
        x = kuyruklar[i-1].xcor()
        y = kuyruklar[i-1].ycor()
        kuyruklar[i].goto(x,y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()
    time.sleep(hiz)
