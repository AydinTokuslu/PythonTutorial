# Verilen bir listenin içinde bulunan sözlük itemlarını sıralamak

employeeList = [
    {"name":"Ahmet", "age":40},
    {"name":"Ezgi", "age":28},
    {"name":"Elif", "age":30},
    {"name":"Mehmet", "age":50},
]
#yaşa göre sıralayalım
employeeList.sort(key=lambda item: item["age"])
#print(employeeList)


numbersList=[
    {"ONE": 1, "THREE": 3, "TWO": 2, "FIVE": 5, "FOUR": 4}
]# value'lara göre sözlük olarak küçükten büyüğe sıralayınız

# print(numbersList[0])  # {'ONE': 1}
# print(numbersList[0].keys())  # dict_keys(['ONE'])
# print(list(numbersList[0].keys()))  # ['ONE']
# print(list(numbersList[0]))  # ['ONE']
# print(list(numbersList[0])[0])  # ONE

#numbersList.sort(key=lambda item : item[list(item)[0]])
#print(numbersList)  #[{'ONE': 1}, {'TWO': 2}, {'THREE': 3}, {'FOUR': 4}, {'FIVE': 5}], keylere göre oldu

numbersDict = numbersList[0]
sortedNumbersDict = {k: v for k, v in sorted(numbersDict.items(), key=lambda item: item[1])}
print(sortedNumbersDict) # {'ONE': 1, 'TWO': 2, 'THREE': 3, 'FOUR': 4, 'FIVE': 5}

