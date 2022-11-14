with open("ornek_metin.txt", encoding="utf-8") as f:
    with open("gecenler.txt","w", encoding="utf-8") as g:
        with open("kalanlar.txt","w", encoding="utf-8") as k:
            icerik = f.readlines()
            m = 0
            for satir in icerik:
                if m == 0:
                    m += 1
                    continue
                satir = satir.replace("\n","")
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0