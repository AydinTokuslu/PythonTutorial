from PyPDF2 import PdfFileMerger

birlestirici = PdfFileMerger()

'''
birlestirici.append("C:/Users/aydin/Desktop/Deep Learning-Based Formula.pdf")
birlestirici.append("C:/Users/aydin/Desktop/İngilizce Hikayeler derece 2  Fono 164s.pdf")

birlestirici.write("birlesen.pdf")
'''

deeplearning = open("C:/Users/aydin/Desktop/Deep Learning-Based Formula.pdf","rb")
ingilicehikayeler = open("C:/Users/aydin/Desktop/İngilizce Hikayeler derece 2  Fono 164s.pdf","rb")

"""
birlestirici.append(deeplearning)
birlestirici.append(ingilicehikayeler)
birlestirici.write("birlesendpf.pdf")
"""

birlestirici.append(deeplearning)
birlestirici.merge(0, ingilicehikayeler)
# 0ncı sayfaya ingilizce hikayeler gelsin, farklı sayfalara da koyabiliriz (3,5,7,10 vb)
birlestirici.write("tekrarbirlesen.pdf")