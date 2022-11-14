#a = {"Ahmet": 100}
#print(a["Ahmet"])

#isim = input("Öğrenci ismi giriniz : ")
#print(a.get(isim, "aradığınız bulunamadı"))

a = {"Ahmet": {"Matematik"  : "90",
               "Fen"        : "80",
               "İngilizce"  : "75",
               "Türkçe"     : "80"},
    "Mehmet" : {"Matematik" : "80",
               "Fen"        : "85",
               "İngilizce"  : "89",
               "Türkçe"     : "80"}}
'''
isimler =a.keys()
while True:
    isim = input("Öğrenci ismi giriniz : ")
    if isim in isimler:
        flag = True
    else:
        flag = False

    if flag:
        ders = input("Ders ismi giriniz : ")
        print(a.get(isim, "aradığınız bulunamadı").get(ders, "Ders bulunamadı."))
    else:
        print("hatalı giriş")
'''


#isim = input("Öğrenci ismi giriniz : ")
#ders = input("Ders ismi giriniz : ")
#rint(a.get(isim, "aradığınız bulunamadı").get(ders, "Ders bulunamadı."))
#print(a["Ahmet"].items())

b = input("Öğrenci adını giriniz : ")

for i in a[b].items():
    print("""
    Öğrenci adı         : {}
    -------------------------
    {} Ders notu : {}
    """.format(b,i[0],i[1]))
