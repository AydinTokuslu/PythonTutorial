sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split(" ")
#print(sentence)
result = { word : len(word) for word in sentence}
print(result)  # {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}