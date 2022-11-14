def repeat_character(text:str):
    emptyList=[]
    for c in text:
       if c not in emptyList:
           emptyList.append(c)
       else:
           return c

    return 0

print(repeat_character("ABCDEFGBCA"))