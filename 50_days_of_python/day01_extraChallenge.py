# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary. For example, the following dictionary should return
# – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(dict):
    max = 0
    for i in dict:
        #print(dict[i])
        if len(dict[i]) > max:
            max = len(dict[i])
    return dict[i]

fruits = {'fruit': 'apple', 'color': 'greeen','shape': "circleee"}
print(longest_value(fruits))