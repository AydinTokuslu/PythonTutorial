# names = [ "Peter", "Jon", "Andrew"]
# Write a function called sort_length that takes a list of strings
# as an argument, and sorts the strings in ascending order
# according to their length. For example, the list above should
# return:
# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions

def sort_length(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if len(list[i]) > len(list[j]):
                list[i], list[j] = list[j], list[i]
    return list


names = [ "Peter", "Jon", "Andrew"]
print(sort_length(names))