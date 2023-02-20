# Write a function called count that takes one argument a string,
# and returns a dictionary of how many times each element
# appears in the string. For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count(s):
    s_dict={}
    for i in s:
        if i not in s_dict.keys():
            s_dict[i]=1
        else:
            s_dict[i]+=1
    print(s_dict)


s="hello"
count(s)