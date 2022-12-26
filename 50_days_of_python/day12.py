# Write a function called count_dots. This function takes a
# string separated by dots as a parameter and counts how many
# dots are in the string. For example, ‘h.e.l.p.’ should return 4
# dots, and ‘he.lp.’ should return 2 dots.

def count_dots(str):
    count=0
    str_a=str.split(".")
    print(str_a)
    for i in range(len(str_a)-1):
        count+=1
    return count


a="h.e.l.p."
print(count_dots(a))