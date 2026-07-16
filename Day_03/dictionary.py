# ==========================================================
#              PYTHON DICTIONARY COMPLETE NOTES
#                    File: dictionaries.py
# ==========================================================


"""
DICTIONARY IN PYTHON
====================

A dictionary is a collection of data stored in
key-value pairs.

Syntax:

dictionary = {
    key : value
}

Example:

student = {
    "name": "Rishabh",
    "age": 21,
    "branch": "CSE"
}


IMPORTANT POINTS:
-----------------

✔ Dictionaries are mutable.
✔ Dictionaries store data in key-value pairs.
✔ Keys must be unique.
✔ Keys must be immutable.
✔ Values can be any data type.
✔ Dictionaries are ordered (Python 3.7+).
✔ Dictionaries are dynamic.
✔ Access time is very fast (average O(1)).

"""



# ==========================================================
# CREATING DICTIONARIES
# ==========================================================


# Empty dictionary

empty = {}

print(empty)


# Dictionary with values

student = {
    "name": "Rishabh",
    "age": 21,
    "course": "B.Tech CSE"
}

print(student)



# Mixed data types

data = {
    1: "Python",
    "marks": 90,
    "passed": True,
    "list": [1,2,3]
}

print(data)



# Nested Dictionary

student = {

    "name":"Rishabh",

    "marks":{
        "Python":90,
        "DSA":85
    }
}

print(student)



# ==========================================================
# ACCESSING DICTIONARY VALUES
# ==========================================================


student = {
    "name":"Rishabh",
    "age":21
}


# Using key

print(student["name"])



# Using get()

"""
get() returns None if key does not exist.
"""

print(student.get("age"))

print(student.get("phone"))



# ==========================================================
# ADDING ELEMENTS
# ==========================================================


student = {
    "name":"Rishabh"
}


student["age"] = 21

student["branch"] = "CSE"


print(student)



# ==========================================================
# MODIFYING VALUES
# ==========================================================


student = {
    "name":"Rishabh",
    "age":20
}


student["age"] = 21


print(student)



# ==========================================================
# REMOVING ELEMENTS
# ==========================================================


student = {
    "name":"Rishabh",
    "age":21,
    "branch":"CSE"
}


# pop()

age = student.pop("age")

print(age)

print(student)



# popitem()

"""
Removes last inserted key-value pair.
"""

student.popitem()

print(student)



# del keyword

del student["branch"]

print(student)



# clear()

student.clear()

print(student)



# ==========================================================
# DICTIONARY METHODS
# ==========================================================


student = {

"name":"Rishabh",
"age":21,
"branch":"CSE"

}



# keys()

"""
Returns all keys.
"""

print(student.keys())



# values()

"""
Returns all values.
"""

print(student.values())



# items()

"""
Returns key-value pairs.
"""

print(student.items())



# ==========================================================
# LOOPING THROUGH DICTIONARY
# ==========================================================


student = {

"name":"Rishabh",
"age":21,
"branch":"CSE"

}


# Keys

for key in student:
    print(key)



# Values

for value in student.values():
    print(value)



# Key and Value

for key,value in student.items():

    print(key,value)



# ==========================================================
# CHECKING KEY EXISTENCE
# ==========================================================


student = {
    "name":"Rishabh"
}


print("name" in student)

print("age" not in student)



# ==========================================================
# UPDATE DICTIONARY
# ==========================================================


student = {

"name":"Rishabh",
"age":21

}


student.update(
    {
        "age":22,
        "branch":"CSE"
    }
)


print(student)



# ==========================================================
# COPY DICTIONARY
# ==========================================================


a = {

"name":"Rishabh"

}


b = a.copy()


b["name"]="Rahul"


print(a)

print(b)



# ==========================================================
# DICTIONARY FROM LISTS
# ==========================================================


keys = ["name","age","branch"]

values = ["Rishabh",21,"CSE"]


student = dict(zip(keys,values))


print(student)



# ==========================================================
# DICTIONARY COMPREHENSION
# ==========================================================


"""
Short way to create dictionaries.

Syntax:

{key:value for item in iterable}

"""


square = {

x:x*x

for x in range(1,6)

}


print(square)



# With condition

even = {

x:x*x

for x in range(10)

if x%2==0

}


print(even)



# ==========================================================
# NESTED DICTIONARY
# ==========================================================


college = {


"student1":

{

"name":"Rishabh",
"marks":90

},


"student2":

{

"name":"Aman",
"marks":85

}

}


print(college["student1"]["marks"])



# ==========================================================
# MERGING DICTIONARIES
# ==========================================================


a = {

"name":"Rishabh"

}


b = {

"age":21

}


# Using update()

a.update(b)

print(a)



# Using | operator (Python 3.9+)


c = a | b

print(c)



# ==========================================================
# DEFAULT VALUES
# ==========================================================


"""
setdefault()

Adds key only if it does not exist.
"""


student = {

"name":"Rishabh"

}


student.setdefault(
    "age",
    21
)


print(student)



# ==========================================================
# DICTIONARY FUNCTIONS
# ==========================================================


student = {

"a":10,
"b":20,
"c":30

}


print(len(student))


print(max(student))


print(min(student))



# ==========================================================
# DICTIONARY KEYS RULES
# ==========================================================


"""
Valid keys:

✔ int
✔ float
✔ string
✔ tuple


Invalid keys:

❌ list
❌ dictionary
❌ set


Because keys must be hashable.
"""


# Valid

d = {

(1,2):"tuple key"

}


print(d)



# Invalid

# d = {[1,2]:"list"}
# TypeError



# ==========================================================
# DICTIONARY VS LIST
# ==========================================================


"""
LIST:

- Stores values only
- Access using index
- Ordered
- Allows duplicates


DICTIONARY:

- Stores key-value pairs
- Access using keys
- Fast searching
- Keys are unique

"""



# ==========================================================
# DICTIONARY VS SET
# ==========================================================


"""
Dictionary:

{
key:value
}


Set:

{
value1,
value2
}


Dictionary stores mapping.
Set stores unique values.

"""



# ==========================================================
# TIME COMPLEXITY
# ==========================================================


"""
Access by key          O(1)

Insert                 O(1)

Update                 O(1)

Delete                 O(1)

Search key             O(1)

Loop                   O(n)

Copy                   O(n)

"""



# ==========================================================
# IMPORTANT INTERVIEW POINTS
# ==========================================================


"""
1. Dictionary stores key-value pairs.

2. Dictionary keys must be unique.

3. Dictionary keys must be immutable.

4. Values can be mutable.

5. Dictionaries are mutable.

6. Dictionary maintains insertion order.

7. Dictionary uses hashing internally.

8. Accessing by key is faster than list searching.

9. get() avoids KeyError.

10. items() returns key-value pairs.

11. keys() returns all keys.

12. values() returns all values.

13. update() merges dictionaries.

14. pop() removes specific key.

15. popitem() removes last item.

16. Dictionary comprehension creates dictionaries quickly.

17. Nested dictionaries represent complex data.

18. JSON data is similar to Python dictionaries.

19. Dictionary is used heavily in APIs and databases.

20. Average dictionary operation complexity is O(1).

"""


# ==========================================================
# END OF DICTIONARY NOTES
# ==========================================================