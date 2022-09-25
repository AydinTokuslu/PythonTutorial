from gtts import gTTS
import os

"""


konusma = gTTS(text= "merhaba nasılsınız, iyi misiniz", lang='tr', slow=False) # lang='tr' turkish

konusma.save("deneme.mp3")
os.system("deneme.mp3")
"""

dosya = open("deneme.txt","r").read()

konusma = gTTS(text= dosya, lang='en', slow=False) # lang='en' english

konusma.save("deneme.mp3")
os.system("deneme.mp3")
