# Write a function called analyse_string that returns the number of
# special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
# and, total characters (all letters and special characters minus
# whitespaces) in a string. Return everything in a dictionary format:

# {“special character”: “number”, “words”: “number”, “total
# characters”: “number”}

# Use the string below as an argument:

# “Python has a string format operator %. This functions
# analogously to printf format strings in C, e.g. "spam=%s
# eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".

def analyse_string(string):
    special_characters = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    special_count = 0
    word_count = 0
    total_char_count = 0

    for char in string:
        if char in special_characters:
            special_count += 1

    words = string.split()
    word_count = len(words)

    for word in words:
        total_char_count += len(word)

    result = {
        "special characters": special_count,
        "words": word_count,
        "total characters": total_char_count
    }

    return result

string = "Python has a string format operator %. This functions analogously to printf format strings in C, e.g. 'spam=%s eggs=%d' % ('blah', 2) evaluates to 'spam=blah eggs=2'."
analysis_result = analyse_string(string)
print(analysis_result)