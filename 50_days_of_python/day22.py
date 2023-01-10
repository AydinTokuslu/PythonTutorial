# Create three functions. The first called add_hash takes a string and
# adds a hash # between the words. The second function called
# add_underscore removes the hash (#) and replaces it with an
# underscore "_" The third function called remove_underscore,
# removes the underscore and replaces it with nothing. if you pass
# ‘Python’ as an argument for the three functions, and you call them at
# the same time like:
# print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.

# def add_hash(str):
#     new_str=""
#     for i in str:
#         new_str+=i
#         new_str+="#"
#     return new_str
#
# def add_underscore(str):
#     new_str=""
#     for i in str:
#         if i == "#":
#             continue
#         else:
#             new_str+=i
#             new_str+="_"
#     return new_str
#
# def remove_underscore(str):
#     new_str = ""
#     for i in str:
#         if i == "_":
#             continue
#         else:
#             new_str += i
#     return new_str
#
# print(remove_underscore(add_underscore(add_hash("Python"))))

def add_hash(a: str):
 return "#".join(a)
def add_underscore(a: str):
 return str(a).replace("#", "_")
def remove_underscore(a: str):
 return str(a).replace("_", "")
print(remove_underscore(add_underscore(add_hash('Python'))))



