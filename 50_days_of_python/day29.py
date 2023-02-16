# Write a function called middle_figure that takes two
# parameters a, and b. The two parameters are strings. The
# function joins the two strings and finds the middle element.
# If the combined string has a middle element, the function should
# return the element, otherwise, return ‘no middle figure’. Use
# ‘make love’ as an argument for a and ‘not wars’ as an
# argument for b. Your function should return ‘e’ as the middle
# element. Whitespaces should be removed.

def middle_figure(a,b):
    join=""
    if len(a) > len(b):
        return a[-1]
    elif len(b) > len(a):
        return b[0]
    else:
        return "no middle figure"


a="make love"
b="not wars"
print(middle_figure(a,b))