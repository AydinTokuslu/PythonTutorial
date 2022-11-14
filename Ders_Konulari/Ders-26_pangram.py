def pangram_checker(sentence):
    lsentence=sentence.lower()

    letters=['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']

    for letter in lsentence:
        if letter in letters:
            try:
                letters.remove(letter)
            except:
                pass

    if len(letters) == 0:
        return True
    else:
        return False


#print(pangram_checker("adana bugün çok sıcak.")) False
print(pangram_checker("Pijamalı hasta yağız şoföre çabucak güvendi"))