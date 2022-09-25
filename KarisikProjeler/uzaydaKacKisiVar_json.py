import requests
import json

gelen_cevap=requests.get("http://api.open-notify.org/astros.json")

uzaydaki_insan_sayisi=gelen_cevap.json()["number"]

print(f"şu anda uzayda {uzaydaki_insan_sayisi} insan var")

print("uzaydaki insanların isimleri")
print("----------------------------")

for kisi in gelen_cevap.json()["people"]:
    print(kisi["name"], "   -----> ", kisi["craft"])