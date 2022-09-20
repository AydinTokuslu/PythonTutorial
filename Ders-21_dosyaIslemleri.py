dosya=open("planlar.txt","r",encoding="utf-8")

print(dosya.read(14))
print(dosya.readline())
print(dosya.readlines())
print(dosya.tell())#imlecin index olarak yerini söyler
print(dosya.seek(0))#seek, imlecin nerede olacağını ayarlar
print(dosya.read(14))
print(dosya.seek(50))#seek, imlecin nerede olacağını ayarlar
print(dosya.readline())

dosya.close()