# ==========================================================
#              PYTHON LIST COMPLETE NOTES
#                    File: list.py
# ==========================================================


"""
LIST IN PYTHON
==============

A list is a collection of multiple values stored in a single variable.

Lists are:
✔ Ordered
✔ Mutable (can be changed)
✔ Indexed
✔ Allow duplicate values
✔ Allow different data types
✔ Dynamic in size

Syntax:

list_name = [value1, value2, value3]

Example:
"""

numbers = [1, 2, 3, 4]

print(numbers)



# ==========================================================
# CREATING LISTS
# ==========================================================


# Empty list

empty_list = []

print(empty_list)


# List with values

students = ["Rishabh", "Aman", "Rahul"]

print(students)


# Mixed data types

data = [10, "Python", 3.14, True]

print(data)


# Nested list

nested = [[1,2],[3,4]]

print(nested)



# ==========================================================
# LIST INDEXING
# ==========================================================

"""
Index starts from 0

Example:

Python List:

[10,20,30,40]

Index:
 0  1  2  3

Negative Index:

[-4,-3,-2,-1]

"""

numbers = [10,20,30,40]

print(numbers[0])
print(numbers[2])
print(numbers[-1])



# ==========================================================
# LIST SLICING
# ==========================================================

"""
Syntax:

list[start:stop:step]

"""

numbers = [10,20,30,40,50,60]


print(numbers[0:3])

print(numbers[:4])

print(numbers[3:])

print(numbers[::-1])

print(numbers[::2])



# ==========================================================
# LIST MUTABILITY
# ==========================================================

"""
Lists can be modified after creation.
"""

numbers = [10,20,30]

numbers[0] = 100

print(numbers)

# Output:
# [100,20,30]



# ==========================================================
# LIST OPERATORS
# ==========================================================


# Concatenation

a = [1,2,3]
b = [4,5,6]

print(a+b)



# Repetition

print([1,2]*3)



# Membership

print(2 in [1,2,3])

print(5 not in [1,2,3])



# ==========================================================
# ADDING ELEMENTS TO LIST
# ==========================================================


# append()

"""
Adds element at end.
"""

numbers = [1,2,3]

numbers.append(4)

print(numbers)



# extend()

"""
Adds multiple elements.
"""

numbers = [1,2,3]

numbers.extend([4,5,6])

print(numbers)



# insert()

"""
Adds element at specific index.

Syntax:
insert(index,value)
"""

numbers = [1,2,3]

numbers.insert(1,100)

print(numbers)



# ==========================================================
# REMOVING ELEMENTS FROM LIST
# ==========================================================


# remove()

"""
Removes first matching value.
"""

numbers = [10,20,30,20]

numbers.remove(20)

print(numbers)



# pop()

"""
Removes element by index.
Returns removed value.
"""

numbers = [10,20,30]

x = numbers.pop()

print(x)
print(numbers)



# pop(index)

numbers = [10,20,30]

numbers.pop(1)

print(numbers)



# del keyword

numbers = [10,20,30]

del numbers[0]

print(numbers)



# clear()

"""
Removes all elements.
"""

numbers = [1,2,3]

numbers.clear()

print(numbers)



# ==========================================================
# LIST METHODS
# ==========================================================


# index()

numbers = [10,20,30]

print(numbers.index(20))



# count()

numbers = [1,2,2,3]

print(numbers.count(2))



# sort()

"""
Sorts list permanently.
"""

numbers = [5,1,3,2]

numbers.sort()

print(numbers)



# Reverse sorting

numbers.sort(reverse=True)

print(numbers)



# reverse()

"""
Reverse list order.
"""

numbers = [1,2,3]

numbers.reverse()

print(numbers)



# copy()

"""
Creates shallow copy.
"""

a = [1,2,3]

b = a.copy()

print(b)



# ==========================================================
# BUILT-IN FUNCTIONS WITH LIST
# ==========================================================


numbers = [10,20,30,40]


print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sum(numbers))

print(sorted(numbers))



# ==========================================================
# LOOP THROUGH LIST
# ==========================================================


numbers = [10,20,30]

for value in numbers:
    print(value)



# Using index

for i in range(len(numbers)):
    print(numbers[i])



# ==========================================================
# LIST COMPREHENSION
# ==========================================================

"""
Short way to create lists.

Syntax:

[expression for item in iterable]
"""


squares = [x*x for x in range(1,6)]

print(squares)



# With condition

even = [x for x in range(10) if x%2==0]

print(even)



# ==========================================================
# NESTED LIST
# ==========================================================


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print(matrix[0])

print(matrix[1][2])



# ==========================================================
# COPYING LIST
# ==========================================================


"""
Assignment creates reference.

"""

a = [1,2,3]

b = a

b.append(4)

print(a)
# [1,2,3,4]


# Correct copying

a = [1,2,3]

b = a.copy()

b.append(4)

print(a)



# ==========================================================
# LIST UNPACKING
# ==========================================================


numbers = [10,20,30]

a,b,c = numbers

print(a)
print(b)
print(c)



# ==========================================================
# CONVERTING LIST
# ==========================================================


# List to string

chars = ['P','y','t','h','o','n']

text = "".join(chars)

print(text)



# String to list

text = "Python"

chars = list(text)

print(chars)



# Tuple to list

t = (1,2,3)

print(list(t))



# ==========================================================
# IMPORTANT DIFFERENCE
# ==========================================================


"""
LIST VS TUPLE

List:
✔ Mutable
✔ Uses []
✔ More memory
✔ Slower

Tuple:
✔ Immutable
✔ Uses ()
✔ Less memory
✔ Faster
"""



# ==========================================================
# TIME COMPLEXITY OF LIST OPERATIONS
# ==========================================================


"""
Access by index       O(1)

Search                O(n)

Append                O(1)

Insert                O(n)

Delete                O(n)

Pop last              O(1)

Pop middle            O(n)

Sort                  O(n log n)

Reverse               O(n)

Copy                  O(n)

"""



# ==========================================================
# INTERVIEW POINTS
# ==========================================================


"""
1. Lists are mutable.
2. Lists maintain insertion order.
3. Lists allow duplicate values.
4. Lists can store different data types.
5. Lists are dynamic arrays.
6. Indexing starts from 0.
7. Negative indexing starts from -1.
8. append() adds one element.
9. extend() adds multiple elements.
10. insert() adds element at specific position.
11. remove() removes value.
12. pop() removes index and returns value.
13. sort() modifies original list.
14. sorted() creates new sorted list.
15. copy() creates shallow copy.
16. List comprehension creates lists quickly.
17. Lists can contain other lists.
18. Lists are passed by reference.
19. Nested lists are used for matrices.
20. Lists use dynamic memory allocation.

"""


# ==========================================================
# END OF LIST NOTES
# ==========================================================