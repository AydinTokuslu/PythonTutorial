# Create a function called all_the_same that takes one
# argument, a string, a list, or a tuple and checks if all the
# elements are the same. If the elements are the same, the function
# should return True. If not, it should return False. For example,
# [‘Mary’, ‘Mary’, ‘Mary’] should return True

def all_the_same(s):
    for i in range(0,len(s)):
        if s[i] == s[i+1]:
            #print(s[i])
            return True
        else:
            return False




ssl=["Mary", "Mary", "Many"]
print(all_the_same(ssl))