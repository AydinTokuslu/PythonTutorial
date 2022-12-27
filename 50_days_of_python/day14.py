# Write a function called flat_list that takes one argument, a
# nested list. The function converts the nested list into a one-dimension list.
# For example [[2,4,5,6]] should return
# [2,4,5,6].

def flat_list(list):
    new_list=[]
    for i in list:
        for j in i:
            #print(j)
            new_list.append(j)
    print(new_list)


x=[[2,4,5,6]]
flat_list(x)