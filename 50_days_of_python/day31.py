# Write a function that has one parameter and takes a list of words
# as an argument. The function returns the longest word from the
# list. Name the function longest_word. The function should
# return the longest word and the number of letters in that word.
# For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your
# function should return
# [10, JavaScript] as the longest word.

def longest_word(list1):
    max=0
    max_word=""
    for i in list1:
        if len(i)>max:
            max=len(i)
            max_word=i
    print(f"[{max}, {max_word}]")



list1=["Java", "JavaScript", "Python"]
longest_word(list1)