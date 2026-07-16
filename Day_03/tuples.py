# ==========================================================
#              PYTHON TUPLE COMPLETE NOTES
#                    File: tuple.py
# ==========================================================


"""
TUPLE IN PYTHON
===============

A tuple is an ordered collection of elements stored in
a single variable.

Syntax:

tuple_name = (value1, value2, value3)


Example:

numbers = (10,20,30)


IMPORTANT POINTS:
-----------------

✔ Tuples are immutable (cannot be changed).
✔ Tuples are ordered.
✔ Tuples support indexing.
✔ Tuples support slicing.
✔ Tuples allow duplicate values.
✔ Tuples can store different data types.
✔ Tuples are faster than lists.
✔ Tuples use less memory compared to lists.
✔ Tuples can be used as dictionary keys.
✔ Tuples can contain mutable objects.

"""


# ==========================================================
# CREATING TUPLES
# ==========================================================


# Empty tuple

empty_tuple = ()

print(empty_tuple)



# Tuple with values

numbers = (10,20,30)

print(numbers)



# Tuple with different data types

data = (
    10,
    "Python",
    3.14,
    True
)

print(data)



# Nested tuple

nested = (
    (1,2,3),
    (4,5,6)
)

print(nested)



# ==========================================================
# SINGLE ELEMENT TUPLE
# ==========================================================


"""
Important:

A single value without comma is NOT a tuple.

"""



# Wrong

a = (10)

print(type(a))


# Output:
# <class 'int'>



# Correct

b = (10,)

print(type(b))


# Output:
# <class 'tuple'>



# ==========================================================
# TUPLE INDEXING
# ==========================================================


"""
Index starts from 0

Example:

(10,20,30,40)

Index:
 0  1  2  3


Negative Index:

-4 -3 -2 -1

"""


numbers = (10,20,30,40)


print(numbers[0])

print(numbers[2])

print(numbers[-1])

print(numbers[-2])



# ==========================================================
# TUPLE SLICING
# ==========================================================


"""
Syntax:

tuple[start:stop:step]

"""


numbers = (10,20,30,40,50,60)


print(numbers[0:3])


print(numbers[:4])


print(numbers[3:])


print(numbers[::-1])


print(numbers[::2])



# ==========================================================
# TUPLE IMMUTABILITY
# ==========================================================


"""
Tuples cannot be modified after creation.

"""

numbers = (10,20,30)


# Wrong:

# numbers[0] = 100

# TypeError



# Correct way:

numbers = (100,20,30)

print(numbers)



# ==========================================================
# ACCESSING TUPLE ELEMENTS
# ==========================================================


student = (
    "Rishabh",
    21,
    "CSE"
)


print(student[0])

print(student[1])

print(student[2])



# ==========================================================
# TUPLE OPERATORS
# ==========================================================


# Concatenation (+)


a = (1,2,3)

b = (4,5,6)


print(a+b)



# Repetition (*)


print((1,2)*3)



# Membership operators


print(2 in (1,2,3))


print(5 not in (1,2,3))



# ==========================================================
# LOOP THROUGH TUPLE
# ==========================================================


numbers = (10,20,30)


for item in numbers:

    print(item)



# Using index

for i in range(len(numbers)):

    print(numbers[i])



# ==========================================================
# TUPLE METHODS
# ==========================================================


"""
Tuple has only two built-in methods:

1. count()
2. index()

Because tuples are immutable.
"""


# ==========================================================
# count()
# ==========================================================


"""
Returns number of occurrences.
"""


numbers = (1,2,2,3,2)


print(numbers.count(2))


# Output:
# 3



# ==========================================================
# index()
# ==========================================================


"""
Returns first occurrence index.
"""


numbers = (10,20,30,20)


print(numbers.index(20))


# Output:
# 1



# ==========================================================
# BUILT-IN FUNCTIONS WITH TUPLES
# ==========================================================


numbers = (10,20,30,40)


print(len(numbers))


print(max(numbers))


print(min(numbers))


print(sum(numbers))


print(sorted(numbers))



# ==========================================================
# TUPLE PACKING
# ==========================================================


"""
Packing means storing multiple values
into a tuple.
"""


student = "Rishabh",21,"CSE"


print(student)



# ==========================================================
# TUPLE UNPACKING
# ==========================================================


"""
Extract tuple values into variables.
"""


student = (
    "Rishabh",
    21,
    "CSE"
)


name, age, branch = student


print(name)

print(age)

print(branch)



# ==========================================================
# SWAPPING USING TUPLE
# ==========================================================


a = 10

b = 20


a,b = b,a


print(a,b)



# ==========================================================
# NESTED TUPLE
# ==========================================================


matrix = (

    (1,2,3),

    (4,5,6),

    (7,8,9)

)


print(matrix[0])


print(matrix[1][2])



# ==========================================================
# CONVERTING DATA TYPES
# ==========================================================


# List to tuple


numbers = [1,2,3]


t = tuple(numbers)


print(t)



# Tuple to list


t = (1,2,3)


lst = list(t)


print(lst)



# String to tuple


text = "Python"


print(tuple(text))



# ==========================================================
# TUPLE WITH MUTABLE OBJECTS
# ==========================================================


"""
Tuple is immutable,
but objects inside tuple can change.

"""


data = (

    [1,2,3],

    "Python"

)


data[0].append(4)


print(data)



# ==========================================================
# TUPLE AS DICTIONARY KEY
# ==========================================================


"""
Tuple can be dictionary key
because it is immutable.
"""


location = {

    (28.61,77.20):"Delhi"

}


print(location)



# ==========================================================
# TUPLE VS LIST
# ==========================================================


"""
LIST:

✔ Mutable
✔ Uses []
✔ More memory
✔ More methods
✔ Slower


TUPLE:

✔ Immutable
✔ Uses ()
✔ Less memory
✔ Faster
✔ Secure data
"""


# ==========================================================
# TUPLE VS SET
# ==========================================================


"""
TUPLE:

(1,2,3)

- Ordered
- Allows duplicates
- Indexed


SET:

{1,2,3}

- Unordered
- No duplicates
- No indexing

"""



# ==========================================================
# WHY USE TUPLES?
# ==========================================================


"""
1. Data should not change.

Example:
- Days of week
- Coordinates
- Database records


2. Faster data access.

3. Less memory usage.

4. Can be dictionary keys.

5. Protects data from modification.

"""



# ==========================================================
# TIME COMPLEXITY
# ==========================================================


"""
Access by index       O(1)

Search                O(n)

count()               O(n)

index()               O(n)

Iteration             O(n)

Conversion            O(n)

"""



# ==========================================================
# IMPORTANT INTERVIEW POINTS
# ==========================================================


"""
1. Tuple is immutable.

2. Tuple uses parentheses ().

3. Single element tuple requires comma.

4. Tuple supports indexing and slicing.

5. Tuple allows duplicate elements.

6. Tuple can contain different data types.

7. Tuple is faster than list.

8. Tuple uses less memory.

9. Tuple has only two methods:
   count() and index()

10. Tuple can be dictionary key.

11. Tuple unpacking is widely used.

12. Tuples support concatenation.

13. Tuples support repetition.

14. Tuples are hashable if all elements are hashable.

15. Tuple values cannot be changed directly.

16. Tuple can contain mutable objects.

17. sorted(tuple) returns a list.

18. tuple() converts iterable into tuple.

19. Tuples are commonly used for fixed data.

20. Named tuples provide readable tuple structures.

"""


# ==========================================================
# END OF TUPLE NOTES
# ==========================================================