# You are given a list of names, and you are asked to write a code
# that returns all the names that start with ‘S’. Your code should
# return a dictionary of all the names that start with S and how
# many times they appear in the dictionary. Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly",
#  "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
# Your code should return: {"Sasha": 1, "Sera": 2}

names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

s_list = []
for i in names:
    if i.startswith("S"):
        s_list.append(i)
print(s_list)

def convert(s_list):
    count = 0

    res_dict = {s_list[i]: count for i in range(0, len(s_list))}

    for j in res_dict.items():
        if j in res_dict.keys():
            count += 1
            res_dict = {s_list[i]: count for i in range(0, len(s_list), 2)}
        else:
            count = 0
            res_dict = {s_list[i]: count for i in range(0, len(s_list), 2)}
    return res_dict
print(convert(s_list))

# def number_of_keys(res_dict):
#     count = 0
#     for value in res_dict.items():
#         count+= 1
#     return count
# print(number_of_keys(res_dict))

# s_dict = {}
# count = 0
# for i in s_list:
#     s_dict[0]=i
#     s_dict[1]=len(s_dict.values())
#     # if i in s_dict.keys():
#     #     count +=1
#     #     s_dict[count] = count
#     # else:
#     #     s_dict[i]=i
#     #     s_dict[count] = count
# print(s_dict)
