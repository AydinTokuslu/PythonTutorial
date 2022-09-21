import json

veriler={}

veriler["kullanicilar"]=[]
veriler["kullanicilar"].append({"kadi":"Mckarakule","sifre":"123456","mail":"mckarakule@hotmail.com"})
veriler["kullanicilar"].append({"kadi":"karabela42","sifre":"123456mm","mail":"karabela42@hotmail.com"})

print(veriler)

with open("veriler.json","w") as dosya:
    json.dump(veriler,dosya)


with open("veriler.json","r") as dosya:
    veriler=json.load(dosya)
    for kullanici in veriler["kullanicilar"]:
        if kullanici["kadi"] == "Mckarakule":
            print(kullanici["sifre"])

dosya.close()