# ==========================================================
#        PYTHON STRING <-> LIST CONVERSION NOTES
#                 File: conversion.py
# ==========================================================


"""
STRING TO LIST CONVERSION
=========================

A string can be converted into a list using:
1. list()
2. split()
3. List comprehension

"""


# ==========================================================
# 1. Using list() Method
# ==========================================================

"""
list() converts every character of a string
into separate list elements.

Syntax:
    list(string)
"""

text = "Python"

char_list = list(text)

print(char_list)

# Output:
# ['P', 'y', 't', 'h', 'o', 'n']



# ==========================================================
# 2. Using split() Method
# ==========================================================

"""
split() divides a string into a list.

Syntax:
    string.split(separator, maxsplit)

Default separator = space
"""

text = "Python Java C++"

language_list = text.split()

print(language_list)

# Output:
# ['Python', 'Java', 'C++']



# ==========================================================
# 3. Split Using Custom Separator
# ==========================================================

text = "apple,banana,mango"

fruit_list = text.split(",")

print(fruit_list)

# Output:
# ['apple', 'banana', 'mango']



# ==========================================================
# 4. String of Numbers to List
# ==========================================================

"""
By default split() creates a list of strings.

Use map() to convert into integers.
"""

numbers = "10 20 30 40"

num_list = list(map(int, numbers.split()))

print(num_list)

# Output:
# [10,20,30,40]



# ==========================================================
# 5. Using List Comprehension
# ==========================================================

text = "Python"

char_list = [ch for ch in text]

print(char_list)

# Output:
# ['P','y','t','h','o','n']



# ==========================================================
# LIST TO STRING CONVERSION
# ==========================================================


"""
A list can be converted into a string using:

join()

Syntax:
    separator.join(list)

Important:
All list elements must be strings.
"""



# ==========================================================
# 1. Characters List to String
# ==========================================================

char_list = ['P','y','t','h','o','n']

text = "".join(char_list)

print(text)

# Output:
# Python



# ==========================================================
# 2. Join Words into String
# ==========================================================

words = ["Python","is","easy"]

sentence = " ".join(words)

print(sentence)

# Output:
# Python is easy



# ==========================================================
# 3. Join Using Different Separator
# ==========================================================

items = ["A","B","C"]

result = "-".join(items)

print(result)

# Output:
# A-B-C



# ==========================================================
# 4. Integer List to String
# ==========================================================

"""
join() does not work directly with integers.

Convert integers to string first.
"""

numbers = [1,2,3,4]

text = "".join(map(str,numbers))

print(text)

# Output:
# 1234



# ==========================================================
# STRING <-> LIST SUMMARY
# ==========================================================


"""
STRING TO LIST:

1. list()
   - Converts characters into list elements.

Example:
list("Python")

Output:
['P','y','t','h','o','n']


2. split()
   - Converts words/items into list.

Example:
"Python Java".split()

Output:
['Python','Java']



LIST TO STRING:

join()

Example:

"-".join(['A','B','C'])

Output:
A-B-C

"""



# ==========================================================
# IMPORTANT INTERVIEW POINTS
# ==========================================================

"""
1. Strings are immutable.
2. Lists are mutable.
3. list() separates every character.
4. split() separates based on delimiter.
5. join() combines list elements into string.
6. join() requires all elements to be strings.
7. Use map(str,list) for integer lists.
8. split() returns a list.
9. join() returns a string.
10. Conversion time complexity is O(n).
"""


# ==========================================================
# TIME COMPLEXITY
# ==========================================================

"""
list(string)          -> O(n)
string.split()        -> O(n)
separator.join(list)  -> O(n)
map conversion        -> O(n)
"""