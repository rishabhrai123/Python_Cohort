# ============================================
# PYTHON SETS
# File: sets.py
# ============================================

# A Set is an unordered collection of unique elements.
# Sets are mutable but do not allow duplicate values.

# ============================================
# 1. Creating a Set
# ============================================

fruits = {"apple", "banana", "mango"}

print(fruits)
print(type(fruits))

# Output:
# {'apple', 'banana', 'mango'}
# <class 'set'>


# ============================================
# 2. Empty Set
# ============================================

empty_set = set()

print(empty_set)
print(type(empty_set))

# Output:
# set()
# <class 'set'>


# ============================================
# 3. Duplicate Values
# ============================================

numbers = {10, 20, 30, 10, 20}

print(numbers)

# Output:
# {10, 20, 30}


# ============================================
# 4. Mixed Data Types
# ============================================

data = {10, 3.14, "Python", True}

print(data)


# ============================================
# 5. Length of Set
# ============================================

fruits = {"apple", "banana", "mango"}

print(len(fruits))

# Output:
# 3


# ============================================
# 6. Membership Operators
# ============================================

print("apple" in fruits)
print("grapes" in fruits)
print("banana" not in fruits)

# Output:
# True
# False
# False


# ============================================
# 7. Accessing Set Elements
# ============================================

# Sets do not support indexing.

for item in fruits:
    print(item)


# ============================================
# 8. Add One Item
# ============================================

fruits.add("orange")

print(fruits)


# ============================================
# 9. Add Multiple Items
# ============================================

fruits.update(["grapes", "kiwi"])

print(fruits)


# ============================================
# 10. Remove Item
# ============================================

fruits.remove("banana")

print(fruits)

# remove() raises KeyError if item does not exist.


# ============================================
# 11. discard()
# ============================================

fruits.discard("watermelon")

print(fruits)

# discard() does not raise an error.


# ============================================
# 12. pop()
# ============================================

item = fruits.pop()

print(item)
print(fruits)

# Removes a random item.


# ============================================
# 13. clear()
# ============================================

colors = {"Red", "Blue", "Green"}

colors.clear()

print(colors)

# Output:
# set()


# ============================================
# 14. Copy a Set
# ============================================

A = {1, 2, 3}

B = A.copy()

print(B)


# ============================================
# 15. Union
# ============================================

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A | B)

# Output:
# {1,2,3,4,5}


# ============================================
# 16. Intersection
# ============================================

A = {1, 2, 3}
B = {2, 3, 4}

print(A.intersection(B))
print(A & B)

# Output:
# {2,3}


# ============================================
# 17. Difference
# ============================================

A = {1, 2, 3}
B = {2, 3, 4}

print(A.difference(B))
print(A - B)

# Output:
# {1}


# ============================================
# 18. Symmetric Difference
# ============================================

A = {1, 2, 3}
B = {2, 3, 4}

print(A.symmetric_difference(B))
print(A ^ B)

# Output:
# {1,4}


# ============================================
# 19. Update Set
# ============================================

A = {1, 2}
B = {3, 4}

A.update(B)

print(A)

# Output:
# {1,2,3,4}


# ============================================
# 20. issubset()
# ============================================

A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))

# Output:
# True


# ============================================
# 21. issuperset()
# ============================================

A = {1, 2, 3}
B = {1, 2}

print(A.issuperset(B))

# Output:
# True


# ============================================
# 22. isdisjoint()
# ============================================

A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))

# Output:
# True


# ============================================
# 23. Frozen Set
# ============================================

numbers = frozenset([1, 2, 3])

print(numbers)

# frozenset is immutable.


# ============================================
# 24. Set Comprehension
# ============================================

squares = {x * x for x in range(1, 6)}

print(squares)

# Output:
# {1,4,9,16,25}


# ============================================
# 25. Built-in Functions
# ============================================

numbers = {10, 20, 30, 40}

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

# Output:
# 4
# 40
# 10
# 100
# [10,20,30,40]


# ============================================
# 26. Convert List to Set
# ============================================

numbers = [1, 2, 2, 3, 3, 4]

unique = set(numbers)

print(unique)

# Output:
# {1,2,3,4}


# ============================================
# 27. Convert Set to List
# ============================================

numbers = {10, 20, 30}

lst = list(numbers)

print(lst)


# ============================================
# IMPORTANT POINTS
# ============================================

# 1. Sets store unique values.
# 2. Duplicate values are removed automatically.
# 3. Sets are unordered.
# 4. Sets do not support indexing or slicing.
# 5. Sets are mutable.
# 6. Set elements must be immutable (hashable).
# 7. Empty set -> set()
# 8. Empty {} creates a dictionary.
# 9. Membership testing (in) is very fast.
# 10. Frozen sets are immutable.


# ============================================
# IMPORTANT METHODS
# ============================================

# add()
# update()
# remove()
# discard()
# pop()
# clear()
# copy()

# union()
# intersection()
# difference()
# symmetric_difference()

# issubset()
# issuperset()
# isdisjoint()


# ============================================
# INTERVIEW QUESTIONS
# ============================================

# Q1. What is a set?
# -> An unordered collection of unique elements.

# Q2. Can sets contain duplicate values?
# -> No.

# Q3. Can we use indexing with sets?
# -> No.

# Q4. Difference between remove() and discard()?
# -> remove() raises KeyError if the item is missing.
# -> discard() does not raise an error.

# Q5. Difference between union() and intersection()?
# -> union() returns all unique elements.
# -> intersection() returns only common elements.

# Q6. What is a frozenset?
# -> An immutable version of a set.

# ============================================
# END OF FILE
# ============================================