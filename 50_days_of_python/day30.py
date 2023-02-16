# Write a function called repeated_name that finds the most
# repeated name in the following list.
# name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]

def repeated_name(name):
    repeated={}
    for i in name:
        if not i in repeated:
            repeated[i]=1
        else:
            repeated[i]+=1
    print(repeated)
    print(f"Most repeated name is : {max(repeated)} and repeat number is : {max(repeated.values())}")



name = ["John", "Peter", "John", "Peter", "Jones", "Peter", "James", "James"]
repeated_name(name)
