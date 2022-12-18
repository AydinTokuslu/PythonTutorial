# Verilen bir listenin içinde bulunan sözlük itemlarını sıralamak

employeeList = [
    {"name":"Ahmet", "age":40},
    {"name":"Ezgi", "age":28},
    {"name":"Elif", "age":30},
    {"name":"Mehmet", "age":50},
]
employeeList.sort(key=lambda item: item["age"])
print(employeeList)