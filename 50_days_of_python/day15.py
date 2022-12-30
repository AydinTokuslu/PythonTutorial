# Write a function called same_in_reverse that takes a string
# and checks if the string reads the same in reverse. If it is the
# same, the code should return True if not, it should return False.
# For example, ‘dad’ should return True, because it reads the
# same in reverse.

def same_in_reverse(str):
    reverse=""
    for i in str[::-1]:
        reverse+=i
    print(reverse)
    if str == reverse:
        return True
    else:
        return False



strr="dadad"
print(same_in_reverse(strr))
