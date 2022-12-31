# Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
# Write a code that generates a list of the following numbers from
# the nested list above – 34, 67, 78. Your output should be another
# list:
# [34, 67, 78]. The list output should not have duplicates.



def dublicate_element(list):
    dublicate_list=[]
    for i in list:
        for j in i:
            if j not in dublicate_list:
                dublicate_list.append(j)
            else:
                continue
    return dublicate_list


nested_list = [[12, 34, 56, 67, 78], [12, 67, 34, 68, 78]]
print(dublicate_element(nested_list))