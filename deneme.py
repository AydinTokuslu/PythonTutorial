#my_list = []
#for i in range(10,0,-1):
 #   my_list.append(i)
#my_list.sort()
#print(my_list)
#my_list.reverse()
#print(my_list)

#my_list1 = [4, 5, 2, 1]
#my_list1.sort()
#print(my_list1)

grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
#print(grocer[2][2:5:2])
#print(grocer)
print(grocer[1][1][1:6:2])
grocer2=[]
for i in grocer:
    for y in i:
        for z in y:
            #print(z)
            grocer2.append(z)
#print(grocer2)
#print (z for i in grocer for y in i for z in y)
#text = "My two favorite flowers are tulip and rose, two favorite colors are blue and green."
flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
text = f"My two favorite flowers are {flowers[0][2]} and {flowers[0][1][1]}, two favorite colors are {colors[1][0]} and {colors[1][1][1]}."
text = "My two favorite flowers are {} and {}, two favorite colors are {} and {}.".format(flowers[0][2], flowers[0][1][1], colors[1][0], colors[1][1][1])
#print(text)

escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]

#sentence = "I am 40 years old. I have two children. Data Science is my IT domain."
#sentence = "I am 40 years old. {}I have two children. {}Data Science is my IT domain.".format("\n\t","\n\t\t")
sentence = "I am 40 years old. {}I have two children. {}Data Science is my IT domain.".format(escapes[0],escapes[2][1])

print(sentence)
#print(123_456_789+987_654_321)
two_digit_number = input("Type a two digit number: ")

first_digit=int(two_digit_number[0])
second_digit=int(two_digit_number[1])
print(first_digit)
print(second_digit)
print("total : "+ str(first_digit + second_digit ) )