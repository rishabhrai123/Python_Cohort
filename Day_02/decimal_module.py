# ============================================
# Floating Point Precision in Python
# File: decimal_module.py
# ============================================

# Sometimes floating-point calculations produce
# unexpected results.

print(0.1 + 0.1 + 0.1)

# Output:
# 0.30000000000000004


print(0.1 + 0.1 + 0.1 - 0.3)

# Output:
# 5.551115123125783e-17

# We expect:
# 0.0

# But Python gives a very small number instead.

# ============================================
# Why Does This Happen?
# ============================================

# Computers store decimal numbers in binary.
# Numbers like 0.1 cannot be represented exactly
# in binary floating-point format.

# Therefore,
# 0.1 is stored as an approximation.

# Actual stored value is close to:
# 0.10000000000000000555...

# So,

# 0.1 + 0.1 + 0.1
#
# becomes
#
# 0.30000000000000004

# Hence,

# 0.30000000000000004 - 0.3
#
# =
#
# 5.551115123125783e-17

# This is called Floating Point Precision Error.


# ============================================
# Solution : Decimal Module
# ============================================

# Python provides the decimal module for
# high-precision decimal arithmetic.

from decimal import Decimal


# Wrong way

print(Decimal(0.1))

# Output
# 0.100000000000000005551115123125...


# Correct way

print(Decimal("0.1"))

# Output
# 0.1

# Always pass numbers as strings to Decimal.


# ============================================
# Accurate Calculation
# ============================================

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.1")
c = Decimal("0.1")
d = Decimal("0.3")

print(a + b + c)

# Output
# 0.3

print(a + b + c - d)

# Output
# 0.0


# ============================================
# Another Example
# ============================================

from decimal import Decimal

price = Decimal("19.99")
tax = Decimal("5.01")

print(price + tax)

# Output
# 25.00


# ============================================
# Float vs Decimal
# ============================================

# Float

print(0.1 + 0.2)

# Output
# 0.30000000000000004


# Decimal

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))

# Output
# 0.3


# ============================================
# Why Use Decimal?
# ============================================

# Decimal is mainly used in:

# Banking Software
# Financial Applications
# Accounting
# Currency Calculations
# Billing Systems
# Scientific Calculations


# ============================================
# Important Points
# ============================================

# 1. Float numbers are stored in binary.
# 2. Some decimal values cannot be represented exactly.
# 3. This causes floating-point precision errors.
# 4. Decimal provides exact decimal arithmetic.
# 5. Always create Decimal objects using strings.
#
# Correct:
# Decimal("0.1")
#
# Incorrect:
# Decimal(0.1)


# ============================================
# Interview Questions
# ============================================

# Q1. Why does 0.1 + 0.1 + 0.1 - 0.3 not return 0?

# Because floating-point numbers are stored as
# binary approximations, causing small precision
# errors.

# --------------------------------------------

# Q2. Which module solves floating-point errors?

# decimal

# --------------------------------------------

# Q3. Which class is used from the decimal module?

# Decimal

# --------------------------------------------

# Q4. How should Decimal objects be created?

# Correct
Decimal("0.1")

# Incorrect
# Decimal(0.1)

# --------------------------------------------

# Q5. What is the output?

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))

# Output
# 0.3