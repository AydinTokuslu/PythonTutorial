import turtle
import random
from playsound import playsound

pencere = turtle.Screen()
pencere.screensize(600,600)
pencere.title("Kaplumbagaları Yakala")
pencere.bgcolor("blue")
#pencere.bgpic('underwater.gif') #arkafona resim ekliyoruz.
pencere.tracer(2)#pencere hareketleri çok yavaş olduğu için hızlandırıyoruz.

oyuncu = turtle.Turtle()
oyuncu.color("white")
oyuncu.shape("triangle")
oyuncu.shapesize(3)
oyuncu.penup() #çizim yapmayacak, hareket edecek demek

score = 0 #puan belirliyoruz.

yaziPuan = turtle.Turtle()
yaziPuan.speed(0)#hızı yok
yaziPuan.shape("square")
yaziPuan.color("white")
yaziPuan.penup()
yaziPuan.hideturtle()#görünümünü, şeklini gizliyor.
yaziPuan.goto(-200,200)#x ve y koordinatlarında konumunu belirliyoruz.
yaziPuan.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))#üzerine yazı yazıyoruz. align=sağa sola kaydırma, font=yazı tipi ve büyüklüğü

speed = 1

hizPuan = turtle.Turtle()
hizPuan.speed(0)#hızı yok
hizPuan.shape("square")
hizPuan.color("white")
hizPuan.penup()
hizPuan.hideturtle()
hizPuan.goto(200,200)
hizPuan.write("Hız: {}".format(speed), align="center", font=("Courier", 24, "normal"))

def solaDon():
    oyuncu.left(30) #klavyeden sola basınca, sola dön
def sagaDon():
    oyuncu.right(30) #klavyeden sağa basınca, sağa dön

def hiziArtir():
    global speed
    speed = speed + 1
    hizPuan.clear() #önce mevcut hızı sıfırlamamız gerekiyor.
    hizPuan.write("Hız: {}".format(speed), align="center", font=("Courier", 24, "normal")) 

def hiziAzalt():
    global speed
    speed = speed - 1
    hizPuan.clear()#önce mevcut hızı sıfırlamamız gerekiyor.
    hizPuan.write("Hız: {}".format(speed), align="center", font=("Courier", 24, "normal")) 

#klavye sağ, sol, yukarı,aşağı komutları tanıtıyoruz.
pencere.listen() #klavye kontrolü için; pencereyi dinlicez, pencere üzerindeki klavye hareketleri takip edebileceğiz.
pencere.onkey(solaDon,"Left")#klavyeden yapılacak her hareketi kontrol edebileceğiz.
pencere.onkey(sagaDon,"Right")#klavyeden yapılacak her hareketi kontrol edebileceğiz.
pencere.onkey(hiziArtir, "Up")
pencere.onkey(hiziAzalt, "Down")

maxHedef = 5
hedefler = []
for i in range(maxHedef):#hedef burda 1 tane, hedefleri çoğaltıcaz.
    hedefler.append(turtle.Turtle())
    hedefler[i].penup()#çizim yapmayacak, hareket edecek demek
    hedefler[i].color("yellow")
    hedefler[i].shape("turtle")
    hedefler[i].speed(0)
    hedefler[i].setposition(random.randint(-300,300),random.randint(-300,300))#ekrandaki x,y konumunu belirtir.



while True:
    oyuncu.forward(speed) #oyuncu sürekli hareket ediyor.

    #oyuncu pencere dışına çıkınca geri dönsün.
    # orta noktadan sağa ve sola 300, aşağı ve yukarı 300
    if oyuncu.xcor() > 300 or oyuncu.xcor() < -300:
        oyuncu.right(180)
    if oyuncu.ycor() > 300 or oyuncu.ycor() < -300:
        oyuncu.right(180)

    #hedefte oyuncu gibi hareket etsin.Tüm hedeflerin hareket etmesi için döngü oluşturucaz.
    for i in range(maxHedef):
        hedefler[i].forward(1)
        if hedefler[i].xcor() > 500 or hedefler[i].xcor() < -500:#hedefler x düzlem pencereden çıkmadan geri dönsün
            hedefler[i].right(random.randint(150,250))
        if hedefler[i].ycor() > 500 or hedefler[i].ycor() < -500:#hedefler y düzlem pencereden çıkmadan geri dönsün
            hedefler[i].right(random.randint(150,250))
        #oyuncunun hedefi yemesi, yani çarpışması
        if oyuncu.distance(hedefler[i]) < 40:#aralarındaki mesafe 40 pikselden az ise çarpışma olmuştur.
            hedefler[i].setposition(random.randint(-300, 300), random.randint(-300, 300))  # hedefi tekrar oluştururuz.
            #çarpışma olduktan sonra açıları da değişsin
            hedefler[i].right(random.randint(0, 360))

            #çarpışma anında ses çıkması için ses dosyası yüklüyoruz.
            #playsound("ses dosyasının ismini yazıyoruz, uzantısı wav olacak", False) #sesin hızlı bir şekilde oynaması için False yazıyoruz.

            #çarpışma anında puanımız değişecek, puanımız artacak
            score = score + 1
            yaziPuan.clear()  # öncekini silip yeni puanı ekliyoruz.
            yaziPuan.write("Puan: {}".format(score), align="center", font=("Courier", 24, "normal"))
            


