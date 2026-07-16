# ============================================
# PYTHON SHIFT OPERATORS
# File: shift_operators.py
# ============================================

# Shift operators are Bitwise Operators.
# They work on the binary (bits) representation of integers.

# Types of Shift Operators:
# 1. Left Shift  (<<)
# 2. Right Shift (>>)

# ============================================
# 1. Left Shift Operator (<<)
# ============================================

# Syntax:
# number << n

# It shifts all bits to the left by n positions.
# Each left shift multiplies the number by 2.

a = 5

print(a << 1)

# Output:
# 10

# Binary Representation
#
# 5  = 00000101
#
# Shift Left by 1
#
# 00001010
#
# = 10

print(a << 2)

# Output:
# 20

# Binary
#
# 00000101
#      <<
#
# 00010100
#
# = 20


# ============================================
# More Left Shift Examples
# ============================================

print(3 << 1)

# Output
# 6

# 3 = 00000011
# <<
# 00000110

print(7 << 2)

# Output
# 28

# 7 × 2² = 28


# ============================================
# Formula
# ============================================

# number << n
#
# = number × (2 ** n)

print(10 << 3)

# 10 × 8 = 80

# Output
# 80


# ============================================
# 2. Right Shift Operator (>>)
# ============================================

# Syntax
#
# number >> n

# It shifts bits to the right by n positions.
# Each right shift divides the number by 2.

a = 20

print(a >> 1)

# Output
# 10

# Binary
#
# 20 = 00010100
#
# >>
#
# 00001010
#
# =10

print(a >> 2)

# Output
# 5

# Binary
#
# 00010100
#
# >>
#
# 00000101
#
# =5


# ============================================
# More Right Shift Examples
# ============================================

print(16 >> 1)

# Output
# 8

print(32 >> 2)

# Output
# 8

print(64 >> 3)

# Output
# 8


# ============================================
# Formula
# ============================================

# number >> n
#
# = number // (2 ** n)

print(80 >> 3)

# 80 // 8 = 10

# Output
# 10


# ============================================
# Binary Conversion
# ============================================

num = 10

print(bin(num))

# Output
# 0b1010


# ============================================
# Example
# ============================================

num = 10

print(num << 1)
print(num << 2)
print(num >> 1)
print(num >> 2)

# Output
#
# 20
# 40
# 5
# 2


# ============================================
# Positive Numbers
# ============================================

print(8 << 1)

# Output
# 16

print(8 >> 1)

# Output
# 4


# ============================================
# Negative Numbers
# ============================================

print(-8 << 1)

# Output
# -16

print(-8 >> 1)

# Output
# -4


# ============================================
# Practical Example
# ============================================

salary = 1000

# Multiply by 2
salary = salary << 1

print(salary)

# Output
# 2000


marks = 80

# Divide by 4

print(marks >> 2)

# Output
# 20


# ============================================
# Difference
# ============================================

# <<  Left Shift
#
# Moves bits to left
#
# Multiply by 2ⁿ

# >> Right Shift
#
# Moves bits to right
#
# Divide by 2ⁿ


# ============================================
# Interview Questions
# ============================================

# Q1 What is Left Shift?
#
# Left Shift moves bits toward the left.
#
# Formula:
#
# number << n
#
# number × 2ⁿ


# Q2 What is Right Shift?
#
# Right Shift moves bits toward the right.
#
# Formula:
#
# number >> n
#
# number // 2ⁿ


# Q3 Output

print(5 << 2)

# Output
# 20


print(20 >> 2)

# Output
# 5


# ============================================
# Important Points
# ============================================

# <<  means Left Shift
#
# >> means Right Shift
#
# Left Shift multiplies by powers of 2.
#
# Right Shift divides by powers of 2.
#
# Shift operators work only on integers.
#
# They are faster than multiplication or division by powers of 2 in many low-level operations.
#
# bin() converts a decimal number to its binary representation.


# ============================================
# Quick Revision
# ============================================

# 5 << 1 = 10
# 5 << 2 = 20
# 5 << 3 = 40

# 20 >> 1 = 10
# 20 >> 2 = 5
# 20 >> 3 = 2

# Formula:
#
# Left Shift  : n << x = n × (2 ** x)
#
# Right Shift : n >> x = n // (2 ** x)
# ============================================