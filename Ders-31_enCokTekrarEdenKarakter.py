def maxc(text:str):
    emptyDict=dict()

    for c in text:
        if c not in emptyDict:
            emptyDict[c] = 1
        else:
            emptyDict[c] += 1

    #return emptyDict

    kaydedici=0
    karakter=""

    for c,n in emptyDict.items():
        if n > kaydedici:
            kaydedici = n
            karakter = c
    return "{}:{}".format(karakter,kaydedici)

print(maxc("mert mekatronik udemy dersleri"))