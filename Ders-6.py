def ogrenci_yazdir():
	bilgi=input("öğrencinin adını ve soyadını giriniz : ")

	vize = float(input("Vize notunuzu giriniz : "))
	final = float(input("Final notunuzu giriniz : "))

	sonuc = (vize * 0.4) + (final * 0.6)
	print("Toplam puanınız : ",sonuc)

	if sonuc >= 90:
		harf_notu="AA"

	elif sonuc >= 85:
		harf_notu="BA"

	elif sonuc >= 80:
		harf_notu="BB"

	elif sonuc >= 75:
		harf_notu="CB"

	elif sonuc >= 70:
		harf_notu="CC"

	elif sonuc >= 65:
		harf_notu="DC"

	elif sonuc >= 60:
		harf_notu="DD"

	else:
		harf_notu="FF"

	print("{} adlı ogrencinin, basari notu {}, bu derste elde ettigi harf notu {}".format(bilgi, sonuc, harf_notu))

	with open("notlar.txt","a", encoding="utf-8") as dosya:
		dosya.write("{} adli ogrencinin, basari notu {}, bu derste elde ettigi harf notu {}\n".format(bilgi, sonuc, harf_notu))

kac_ogrenci=int(input("kaç tane öğrenci kaydedeceksiniz? : "))
for i in range(kac_ogrenci):
	ogrenci_yazdir()