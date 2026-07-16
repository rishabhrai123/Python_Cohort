# ============================================
# PYTHON NUMBERS NOTES
# File: number.py
# ============================================

# --------------------------------------------
# 1. Integer (int)
# Whole numbers (positive, negative, zero)
# --------------------------------------------

a = 10
b = -25
c = 0

print(a)
print(type(a))

# Output:
# 10
# <class 'int'>


# --------------------------------------------
# 2. Float
# Decimal numbers
# --------------------------------------------

pi = 3.14
price = 99.99

print(pi)
print(type(pi))

# Output:
# 3.14
# <class 'float'>


# --------------------------------------------
# 3. Complex Numbers
# Format: real + imaginary j
# --------------------------------------------

x = 3 + 4j

print(x)
print(type(x))
print(x.real)
print(x.imag)

# Output:
# (3+4j)
# <class 'complex'>
# 3.0
# 4.0


# --------------------------------------------
# 4. Type Conversion
# --------------------------------------------

a = 10

print(float(a))
print(complex(a))

b = 5.8
print(int(b))

# Output:
# 10.0
# (10+0j)
# 5


# --------------------------------------------
# 5. Arithmetic Operators
# --------------------------------------------

a = 10
b = 3

print(a + b)     # Addition
print(a - b)     # Subtraction
print(a * b)     # Multiplication
print(a / b)     # Division
print(a // b)    # Floor Division
print(a % b)     # Modulus
print(a ** b)    # Power


# --------------------------------------------
# 6. Comparison Operators
# --------------------------------------------

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)


# --------------------------------------------
# 7. Built-in Functions
# --------------------------------------------

print(abs(-25))
print(pow(2, 5))
print(round(5.67))
print(max(10, 20, 30))
print(min(10, 20, 30))
print(sum([10, 20, 30]))

# Output:
# 25
# 32
# 6
# 30
# 10
# 60


# --------------------------------------------
# 8. Math Module
# --------------------------------------------

import math

print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.9))
print(math.factorial(5))
print(math.gcd(12, 18))
print(math.pi)
print(math.e)
print(math.trunc(10.99))

# Output:
# 5.0
# 5
# 4
# 120
# 6
#10


# --------------------------------------------
# 9. Random Module
# --------------------------------------------

import random

print(random.randint(1, 10)) # Gives  random integer
print(random.random())
print(random.choice(["Red", "Blue", "Green"]))


# --------------------------------------------
# 10. Binary, Octal, Hexadecimal
# --------------------------------------------

a = 0b1010
b = 0o17
c = 0x1A

print(a)
print(b)
print(c)

# Output:
# 10
# 15
# 26


# --------------------------------------------
# 11. Convert Number Systems
# --------------------------------------------

num = 20

print(bin(num))
print(oct(num))
print(hex(num))

# Output:
# 0b10100
# 0o24
# 0x14


# --------------------------------------------
# 12. Number Formatting
# --------------------------------------------

num = 1234.56789

print(f"{num:.2f}")

money = 1000000

print(f"{money:,}")

# Output:
# 1234.57
# 1,000,000


# --------------------------------------------
# 13. Boolean as Numbers
# --------------------------------------------

print(True + True)
print(True + False)

# Output:
# 2
# 1


# --------------------------------------------
# 14. Decimal Module
# High Precision Arithmetic
# --------------------------------------------

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)

# Output:
# 0.3


# --------------------------------------------
# 15. Fraction Module
# --------------------------------------------

from fractions import Fraction

f = Fraction(2, 5)

print(f)

# Output:
# 2/5


# ============================================
# IMPORTANT POINTS
# ============================================

# int      -> Whole numbers
# float    -> Decimal numbers
# complex  -> Complex numbers

# /   -> Division
# //  -> Floor Division
# %   -> Modulus
# **  -> Power

# Useful Functions:
# abs()
# round()
# pow()
# max()
# min()
# sum()

# Modules:
# math
# random
# decimal
# fractions

# Number Conversions:
# int()
# float()
# complex()

# Number Systems:
# bin()
# oct()
# hex()


# Use  of repr 
repr('chai')

# Use of str
str('chai')

# Use of chai
print('chai')