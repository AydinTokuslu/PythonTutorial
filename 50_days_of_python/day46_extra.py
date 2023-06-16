# Create a code that extracts data from a website. You will extract a
# table from the website. And from that table you will extract columns
# about the data types in Python and their mutability. You will extract
# information from the following website:

# https://en.wikipedia.org/wiki/Python_(programming_language)

# The following table (next page) is what you will extract from the website.

import pandas as pd
# Accessing the website (pip3 install lxml)
web = pd.read_html("https://en.wikipedia.org/wiki/Python_(programming_language)")
# Using slicing to get table number 1
table = web[1]
print(table)
# getting the two columns from table.
# data_types = table[['Type', 'Mutability']]
# print(data_types)