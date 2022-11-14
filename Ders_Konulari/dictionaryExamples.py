
person1={"name":"linus", "age":21}
#print(person1)
person1["hobbies"]=["dancing","fishing"]  # yeni bir eleman ekliyoruz
#person1.pop("name")
#print(person1)
for key in person1:
    print(key)
    #print(person1[key])
for key in person1.keys():
    print(key)
for i in person1.items():
    print(i)
for i in person1.values():
    print(i)

synonyms={"mountain":"peak","forest":"jungle"}
#print("1.",synonyms["mountain"])
synonyms["terrain"]="land"  # yeni bir eleman ekliyoruz
#print("2.",synonyms)
synonyms.pop("forest")
#print("3.",synonyms)

my_dict = {'name': 'Jack', 'age': 26}
print(my_dict["name"])  # Jack
print(my_dict["age"])  # 26
print(my_dict.get("age"))  # 26
print(my_dict.get("address"))  #sonuç dictionary içinde yoksa, get ile çağırma none döndürür. normal çağırsaydık error verirdi.
# print(my_dict["address"])
my_dict["age"]=30
print(my_dict["age"]) # 30
print(my_dict.items())  # dict_items([('name', 'Jack'), ('age', 30)])
print(my_dict)  # {'name': 'Jack', 'age': 30}
my_dict["address"]="downtown"  # yeni bir eleman ekliyoruz
print(my_dict)  # {'name': 'Jack', 'age': 30, 'address': 'downtown'}
print(my_dict.items())  # dict_items([('name', 'Jack'), ('age', 30), ('address', 'downtown')])

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.keys())  # dict_keys([1, 2, 3, 4, 5])
print(squares.values())  # dict_values([1, 4, 9, 16, 25])
print(squares.items())  # dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
for i in squares.items():
    print(i[0],i[1])  # 1 1
    print(i[0])  # 1
print(squares.popitem())#sildiği sonuncu karakteri gösterir
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16}, sonucu silinmişti
#print(squares.clear())#tüm dictionary'inin içini siler
#print(squares)
#del squares #tüm dictionary'i siler, squares diye birşey kalmaz
#print(squares)

capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"}

for key in capitals:
    #print(key)
    print("Key = " + key + ", Value = " + capitals[key])  # Key = USA, Value = Washington D.C.

# Multi-dimensional Dictionary
d1={"name":"Steve","age":25, "marks":60}
d2={"name":"Anil","age":23, "marks":75}
d3={"name":"Asha", "age":20, "marks":70}

students={1:d1, 2:d2, 3:d3}
print(students)  # {1: {'name': 'Steve', 'age': 25, 'marks': 60}, 2: {'name': 'Anil', 'age': 23, 'marks': 75}, 3: {'name': 'Asha', 'age': 20, 'marks': 70}}
print(students[1]["age"])  # 25
print(students[3]["marks"])  # 70

person = {}
type(person)

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)  # {'fname': 'Joe', 'lname': 'Fonebone', 'age': 51, 'spouse': 'Edna', 'children': ['Ralph', 'Betty', 'Joey'], 'pets': {'dog': 'Fido', 'cat': 'Sox'}}
print(person["children"])  # ['Ralph', 'Betty', 'Joey']
print(person["children"][-1])  # Joey
print(person["pets"]["cat"])  # Sox