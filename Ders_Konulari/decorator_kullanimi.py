import time

def zaman_hesapla(fonk): # decorator fonksiyonu
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        fonk(*args, **kwargs)
        bitis = time.time()
        print(f"işlem {bitis - baslangic} saniye sürdü.")
    return wrapper

@zaman_hesapla  # decorator fonksiyonu
def kareleri_al(liste):
    for i in liste:
        print(i * i)

@zaman_hesapla  # decorator fonksiyonu
def kupleri_al(liste):
    for i in liste:
        print(i ** 3)

@zaman_hesapla  # decorator fonksiyonu
def topla(a, b):
    time.sleep(1)
    print(a + b)

#kareleri_al(range(10000))  # işlem 0.09776592254638672 saniye sürdü.
#kupleri_al(range(10000))  # işlem 0.06134605407714844 saniye sürdü.
topla(10,20)  # 30, işlem 1.0023348331451416 saniye sürdü.