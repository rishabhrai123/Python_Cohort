# ============================================
# PYTHON STRINGS
# File: string.py
# ============================================

# A String is a sequence of characters.
# Strings are enclosed in single (''),
# double ("") or triple quotes (''' ''' or """ """).

# Strings are:
# ✔ Ordered
# ✔ Immutable
# ✔ Iterable
# ✔ Supports Indexing and Slicing

# ============================================
# 1. Creating Strings
# ============================================

name = "Python"
language = 'Programming'

print(name)
print(language)

# Output:
# Python
# Programming


# ============================================
# 2. Multi-line Strings
# ============================================

text = """
Python
is
Awesome
"""

print(text)


# ============================================
# 3. String Data Type
# ============================================

name = "Python"

print(type(name))

# Output:
# <class 'str'>


# ============================================
# 4. String Length
# ============================================

name = "Python"

print(len(name))

# Output:
# 6


# ============================================
# 5. String Indexing
# ============================================

# Positive Indexing

text = "Python"

print(text[0])
print(text[1])
print(text[5])

# Output
# P
# y
# n


# Negative Indexing

print(text[-1])
print(text[-2])

# Output
# n
# o


# ============================================
# 6. String Slicing
# ============================================

text = "Programming"

print(text[0:6])
print(text[3:8])
print(text[:5])
print(text[5:])
print(text[-5:])
print(text[::2])

# Output
# Progra
# gramm
# Progr
# amming
# mming
# Pormig


# ============================================
# 7. Reverse a String
# ============================================

text = "Python"

print(text[::-1])

# Output
# nohtyP


# ============================================
# 8. String Concatenation
# ============================================

first = "Hello"
second = "World"

print(first + " " + second)

# Output
# Hello World


# ============================================
# 9. String Repetition
# ============================================

print("Hi " * 3)

# Output
# Hi Hi Hi


# ============================================
# 10. Membership Operators
# ============================================

text = "Python"

print("Py" in text)
print("Java" in text)
print("Java" not in text)

# Output
# True
# False
# True


# ============================================
# 11. String Comparison
# ============================================

print("abc" == "abc")
print("abc" != "ABC")
print("apple" < "banana")

# Output
# True
# True
# True


# ============================================
# 12. Escape Characters
# ============================================

print("Hello\nPython")
print("Hello\tPython")
print("He said \"Hello\"")
print('It\'s Python')

# Output:
# Hello
# Python
#
# Hello    Python
#
# He said "Hello"
# It's Python


# ============================================
# 13. String Formatting
# ============================================

name = "Rishabh"
age = 21

print("Name:", name, "Age:", age)

print(f"My name is {name} and I am {age} years old.")

print("My name is {}.".format(name))

# Output:
# Name: Rishabh Age: 21
# My name is Rishabh and I am 21 years old.
# My name is Rishabh.


# ============================================
# 14. Common String Methods
# ============================================

text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

# Output:
# PYTHON PROGRAMMING
# python programming
# Python Programming
# Python programming
# PYTHON PROGRAMMING


# ============================================
# 15. Searching Methods
# ============================================

text = "Python Programming"

print(text.find("Pro"))
print(text.index("Pro"))
print(text.count("m"))
print(text.startswith("Python"))
print(text.endswith("ing"))

# Output:
# 7
# 7
# 2
# True
# True


# ============================================
# 16. Replace Method
# ============================================

text = "I like Java"

print(text.replace("Java", "Python"))

# Output:
# I like Python


# ============================================
# 17. Split Method
# ============================================

text = "Python Java C++"

print(text.split())

# Output:
# ['Python', 'Java', 'C++']


# ============================================
# 18. Join Method
# ============================================

languages = ["Python", "Java", "C++"]

print(" | ".join(languages))

# Output:
# Python | Java | C++


# ============================================
# 19. Strip Methods
# ============================================

text = "   Python   "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Output:
# Python
# Python
#    Python


# ============================================
# 20. Checking Methods
# ============================================

print("Python".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print("HELLO".isupper())
print("hello".islower())
print("Python".istitle())
print(" ".isspace())

# Output:
# True
# True
# True
# True
# True
# True
# True


# ============================================
# 21. String Alignment
# ============================================

text = "Python"

print(text.center(20))
print(text.ljust(20))
print(text.rjust(20))

# Output:
#        Python
# Python
#              Python


# ============================================
# 22. Zero Fill
# ============================================

num = "25"

print(num.zfill(5))

# Output:
# 00025


# ============================================
# 23. Encoding & Decoding
# ============================================

text = "Python"

encoded = text.encode()

print(encoded)

print(encoded.decode())

# Output:
# b'Python'
# Python


# ============================================
# 24. String Immutability
# ============================================

name = "Python"

# Strings cannot be modified.

# name[0] = "J"   # TypeError

name = "Jython"

print(name)


# ============================================
# 25. Useful Built-in Functions
# ============================================

text = "Python"

print(len(text))
print(max(text))
print(min(text))
print(sorted(text))
print(reversed(text))

# Output:
# 6
# y
# P
# ['P','h','n','o','t','y']
# <reversed object>


# ============================================
# 26. Convert String
# ============================================

num = "100"

print(int(num))
print(float(num))

# Output:
# 100
# 100.0


# ============================================
# 27. ASCII Values
# ============================================

print(ord("A"))
print(chr(65))

# Output:
# 65
# A


# ============================================
# IMPORTANT STRING METHODS
# ============================================

# upper()
# lower()
# title()
# capitalize()
# swapcase()

# find()
# index()
# count()

# replace()

# split()
# join()

# strip()
# lstrip()
# rstrip()

# startswith()
# endswith()

# isalpha()
# isdigit()
# isalnum()
# isupper()
# islower()
# istitle()
# isspace()

# center()
# ljust()
# rjust()

# encode()
# decode()

# zfill()


# ============================================
# DIFFERENCE
# ============================================

# find()
# Returns -1 if not found.

# index()
# Raises ValueError if not found.

# strip()
# Removes spaces from both sides.

# split()
# Converts string into list.

# join()
# Converts list into string.

# replace()
# Replaces old value with new value.


# ============================================
# INTERVIEW QUESTIONS
# ============================================

# Q1. What is a String?
# -> A sequence of characters enclosed in quotes.

# Q2. Are strings mutable?
# -> No. Strings are immutable.

# Q3. Can strings be indexed?
# -> Yes.

# Q4. Difference between find() and index()?
# -> find() returns -1 if substring is absent.
# -> index() raises ValueError.

# Q5. Difference between split() and join()?
# -> split() converts a string into a list.
# -> join() converts a list into a string.

# Q6. Which method converts all characters to uppercase?
# -> upper()

# Q7. Which method removes spaces from both sides?
# -> strip()

# Q8. Which method replaces text?
# -> replace()

# Q9. How do you reverse a string?
# -> string[::-1]

# Q10. Which operator concatenates strings?
# -> +


# ============================================
# IMPORTANT POINTS
# ============================================

# 1. Strings are immutable.
# 2. Strings are ordered.
# 3. Strings support indexing and slicing.
# 4. Strings can contain letters, digits and symbols.
# 5. Index starts from 0.
# 6. Negative indexing starts from -1.
# 7. Slicing syntax -> string[start:end:step]
# 8. Strings are iterable.
# 9. Strings allow duplicate characters.
# 10. Strings support + and * operators.
# 11. Strings can be formatted using f-strings.
# 12. Strings are one of the most commonly used data types.
# 13. Use ord() to get ASCII/Unicode value.
# 14. Use chr() to convert ASCII code to character.
# 15. Strings are widely used in file handling, web development, APIs, and data processing.

# ============================================
# END OF FILE
# ============================================