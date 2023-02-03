# Write a function called sort_words that takes a string of words
# as an argument, removes the whitespaces, and returns a list of
# letters sorted in alphabetical order. Letters will be separated by
# commas. All letters should appear once in the list. This means
# that you sort and remove duplicates. For example ‘love life’
# should return as ['e,f,i,l,o,v']

def sort_words(str):
    str=str.replace(" ","")
    list_words=[]
    for i in str:
        if i not in list_words:
            list_words.append(i)
    list_words.sort()

    print(list_words)


str= "love life"
sort_words(str)