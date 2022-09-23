import pyttsx3
import PyPDF2

hikaye = open("C:/Users/aydin/Desktop/Deep Learning-Based Formula.pdf","rb")
pdfOkuyucu = PyPDF2.PdfFileReader(hikaye)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id) #voices[0] = kadın sesi, [1]= erkek sesi

for sayfa_numarası in range(0,pdfOkuyucu.numPages):
    sayfa = pdfOkuyucu.getPage(sayfa_numarası)
    yazi = sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()