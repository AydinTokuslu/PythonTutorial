import random

yaziGelen=0
turaGelen=0

paraYuzeyi=["Tura","Yazi"]

atilacakPara=int(input("kaç kere para atmak istiyorsunuz? : "))

while atilacakPara>0:
    paraUstu=random.choice(paraYuzeyi)
    if paraUstu=="Tura":
        turaGelen+=1
        print("Tura geldi!")
    else:
        yaziGelen+=1
        print("Yazi geldi!")

    atilacakPara-=1

print("Tura sayısı : {}\nYazi sayisi : {}".format(yaziGelen,turaGelen))