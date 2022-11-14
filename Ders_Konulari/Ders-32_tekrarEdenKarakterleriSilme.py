def clearList(liste:list):
    emptyList=[]

    for name in liste:
        if name not in emptyList:
            emptyList.append(name)
        else:
            pass
    return emptyList


print(clearList(["Mert","Tolga","Okan","Tolga","Kerem","Aslı","Melike","Mert","Melis","Melis","Şeyda","Burcu","Burcu","Melike"]))