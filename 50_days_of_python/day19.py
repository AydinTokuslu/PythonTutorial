# Write two functions. The first function is called count_words
# which takes a string of words and counts how many words are in
# the string.

# The second function called count_elements takes a string of
# words and counts how many elements are in the string. Do not
# count the whitespaces. The first function will return the number
# of words in a string and the second one will return the number
# of elements (less whitespace). If you pass ‘I love learning’,
# the count_words function should return 3 words and
# count_elements should return 13 elements.

def count_words(str):
    count=0
    for i in str.split(" "):
        count+=1
    return f"{count} words"

def count_elements(str):
    count = 0
    for i in str.split(" "):
        count+=len(i)
    return f"{count} elements"

x="I love learning"
print(count_words(x))
print(count_elements(x))
