#Write a function called add_reverse. This function takes two
# lists as argument and adds each corresponding number, and
# reverses the outcome. For example, if you pass [10, 12, 34]
# and [12, 56, 78]. Your code should return [112, 22, 68]. If the
# two lists are not of equal lengths, the code should return a
# message that "the lists are not of equal lengths".

def add_reverse(list1,list2):
    list3=[]
    toplam=0
    if len(list1) != len(list2):
        print("the lists are not of equal lengths")
    else:
        for i in range(len(list1)):
            toplam=list1[i]+list2[i]
            list3.append(toplam)

    print(list3)




list1=[10, 12, 34]
list2=[12, 56, 78]
add_reverse(list1,list2)