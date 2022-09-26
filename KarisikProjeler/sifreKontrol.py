import tkinter as tk

arayuz = tk.Tk()
arayuz.title("Sifre")
arayuz.geometry("300x200")

a1="elif"
a2="12345"

kullanici = tk.Label(text="KULLANICI ADI: ")
kullanici.place(x=10, y=10)

y = tk.StringVar()
kullanici_girisi = tk.Entry(textvariable=y)
kullanici_girisi.place(x=100, y=10)

kullanici = tk.Label(text="ŞİFRE GİRİŞİ: ")
kullanici.place(x=29, y=35)

x = tk.StringVar()
kullanici_girisi = tk.Entry(textvariable=x)
kullanici_girisi.place(x=100, y=35)

dogru_yanlis = tk.Label(font="Verdana 30 bold")
dogru_yanlis.place(x=100, y=95)


def giris_komut():
    kullan = y.get()
    sif = x.get()
    print(kullan,"\n",sif)
    if kullan == a1 and sif == a2:
        print("doğru")
        dogru_yanlis.config(text="DOĞRU", fg="green")
    else:
        print("yanlış")
        dogru_yanlis.config(text="YANLIŞ", fg="red")

giris= tk.Button(text="GİRİS", command=giris_komut)
giris.place(x=186, y=55)

arayuz.mainloop()