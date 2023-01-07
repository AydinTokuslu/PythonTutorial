# Write a function called capitalize. This function takes a string
# as an argument and capitalizes the first letter of each word. For
# example, ‘i like learning’ becomes ‘I Like Learning’.

def capitalize(str):
    new_str=""
    for i in str.split(" "):
        new_str+=i.capitalize()
        new_str+=" "
    return new_str


x="i like learning"
print(capitalize(x))