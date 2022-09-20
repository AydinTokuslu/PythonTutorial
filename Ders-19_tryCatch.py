while True:
    try:
        boy=float(input("lütfen boyunuzu metre cinsinden giriniz (ÖRNEK: 1.85): "))
        break
    except:
        print("Lütfen sayıyı doğru giriniz.")

while True:
    try:
        kütle=float(input("lütfen kilonuzu kg cinsinden giriniz (ÖRNEK: 55): "))
        break
    except:
        print("Lütfen sayıyı doğru giriniz.")

print(kütle / boy ** 2)