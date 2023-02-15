# Write a function called index_position. This function takes a
# string as a parameter and returns the positions or indexes of all
# lower letters in the string. For example, ‘LovE’ should return
# [1,2].

def index_position(str):
    index_str=[]
    for i in str:
        print(i)
        if i.islower():
            #print(str.index(i))
            index_str.append(str.index(i))
    print(index_str)



str="LovE"
index_position(str)