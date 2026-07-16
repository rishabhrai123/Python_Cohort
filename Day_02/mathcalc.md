# Mathematical Calculations in Python

Python provides powerful mathematical operations through **operators**, **built-in functions**, and the **math**, **cmath**, **random**, **statistics**, and **decimal** modules.

---

# 1. Arithmetic Operators

Arithmetic operators perform basic mathematical calculations.

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `10 / 4` | `2.5` |
| `//` | Floor Division | `10 // 4` | `2` |
| `%` | Modulus (Remainder) | `10 % 4` | `2` |
| `**` | Exponent (Power) | `2 ** 3` | `8` |

## Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 2. Assignment Operators

| Operator | Meaning |
|----------|---------|
| `=` | Assignment |
| `+=` | Add and assign |
| `-=` | Subtract and assign |
| `*=` | Multiply and assign |
| `/=` | Divide and assign |
| `%=` | Modulus and assign |
| `//=` | Floor divide and assign |
| `**=` | Power and assign |

Example

```python
x = 10

x += 5
x *= 2

print(x)
```

---

# 3. Comparison Operators

Used in mathematical comparisons.

| Operator | Example |
|----------|---------|
| `==` | 5 == 5 |
| `!=` | 5 != 4 |
| `>` | 8 > 5 |
| `<` | 5 < 7 |
| `>=` | 8 >= 8 |
| `<=` | 4 <= 9 |

---

# 4. Built-in Mathematical Functions

## abs()

Returns absolute value.

```python
abs(-25)
```

Output

```
25
```

---

## round()

Rounds a number.

```python
round(3.567,2)
```

Output

```
3.57
```

---

## pow()

Power function.

```python
pow(2,5)
```

Output

```
32
```

---

## divmod()

Returns quotient and remainder.

```python
divmod(17,5)
```

Output

```
(3,2)
```

---

## max()

Largest number.

```python
max(10,20,30)
```

---

## min()

Smallest number.

```python
min(10,20,30)
```

---

## sum()

Sum of elements.

```python
sum([10,20,30])
```

Output

```
60
```

---

## len()

Length of collection.

```python
len([1,2,3])
```

---

# 5. Type Conversion

```python
int(3.9)

float(5)

complex(5)

str(100)
```

---

# 6. math Module

```python
import math
```

---

## Square Root

```python
math.sqrt(25)
```

Output

```
5.0
```

---

## Factorial

```python
math.factorial(5)
```

Output

```
120
```

---

## Power

```python
math.pow(2,4)
```

---

## Ceiling

Rounds upward.

```python
math.ceil(5.2)
```

Output

```
6
```

---

## Floor

Rounds downward.

```python
math.floor(5.9)
```

Output

```
5
```

---

## Truncate

```python
math.trunc(8.99)
```

Output

```
8
```

---

## Absolute Value

```python
math.fabs(-12)
```

---

## GCD

Greatest Common Divisor

```python
math.gcd(20,30)
```

Output

```
10
```

---

## LCM

Least Common Multiple

```python
math.lcm(10,15)
```

Output

```
30
```

---

## Logarithm

```python
math.log(100)
```

Natural logarithm

```python
math.log10(100)
```

Base-10 logarithm

---

## Exponential

```python
math.exp(2)
```

---

## Constants

```python
math.pi

math.e

math.tau

math.inf

math.nan
```

---

# 7. Trigonometric Functions

```python
import math
```

| Function | Description |
|----------|-------------|
| `math.sin(x)` | Sine |
| `math.cos(x)` | Cosine |
| `math.tan(x)` | Tangent |
| `math.asin(x)` | Inverse Sine |
| `math.acos(x)` | Inverse Cosine |
| `math.atan(x)` | Inverse Tangent |

Example

```python
math.sin(math.pi/2)
```

Output

```
1.0
```

---

# 8. Angle Conversion

Degrees to Radians

```python
math.radians(180)
```

Radians to Degrees

```python
math.degrees(math.pi)
```

---

# 9. Random Mathematical Functions

```python
import random
```

Random Integer

```python
random.randint(1,100)
```

Random Float

```python
random.random()
```

Random Choice

```python
random.choice([10,20,30])
```

Random Shuffle

```python
random.shuffle(list1)
```

Random Sample

```python
random.sample(range(100),5)
```

---

# 10. Statistics Module

```python
import statistics
```

Mean

```python
statistics.mean(data)
```

Median

```python
statistics.median(data)
```

Mode

```python
statistics.mode(data)
```

Variance

```python
statistics.variance(data)
```

Standard Deviation

```python
statistics.stdev(data)
```

---

# 11. Decimal Module

Provides high precision calculations.

```python
from decimal import Decimal

a = Decimal("0.1")

b = Decimal("0.2")

print(a+b)
```

Output

```
0.3
```

---

# 12. Fraction Module

```python
from fractions import Fraction

Fraction(5,8)
```

Addition

```python
Fraction(1,2)+Fraction(1,3)
```

Output

```
5/6
```

---

# 13. Complex Numbers

```python
a = 3+4j
```

Real Part

```python
a.real
```

Imaginary Part

```python
a.imag
```

Magnitude

```python
abs(a)
```

---

# 14. Bitwise Mathematical Operators

| Operator | Meaning |
|----------|---------|
| `&` | AND |
| `|` | OR |
| `^` | XOR |
| `~` | NOT |
| `<<` | Left Shift |
| `>>` | Right Shift |

Example

```python
5 & 3

5 | 3

5 ^ 3

5 << 2

20 >> 2
```

---

# 15. Operator Precedence

Highest to Lowest

```
()
**
+x -x
* / // %
+ -
<< >>
&
^
|
Comparison
not
and
or
```

Example

```python
5 + 2 * 3
```

Output

```
11
```

---

# 16. Common Mathematical Programs

## Swap Two Numbers

```python
a,b = 10,20

a,b = b,a

print(a,b)
```

---

## Even or Odd

```python
num = 15

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Largest Number

```python
a = 20
b = 50

print(max(a,b))
```

---

## Area of Circle

```python
import math

r = 5

area = math.pi*r*r

print(area)
```

---

## Simple Interest

```python
P = 1000

R = 5

T = 2

SI = (P*R*T)/100

print(SI)
```

---

## Compound Interest

```python
P = 1000

R = 5

T = 2

A = P*(1+R/100)**T

CI = A-P

print(CI)
```

---

## Factorial

```python
import math

print(math.factorial(5))
```

---

## Prime Number

```python
num = 17

prime = True

for i in range(2,num):
    if num%i==0:
        prime=False
        break

print(prime)
```

---

## Fibonacci Series

```python
a,b = 0,1

for i in range(10):
    print(a)
    a,b = b,a+b
```

---

## Sum of First N Numbers

```python
n = 10

print(n*(n+1)//2)
```

---

# Summary Table

| Category | Functions/Operators |
|-----------|---------------------|
| Arithmetic | `+ - * / // % **` |
| Built-in | `abs()`, `round()`, `pow()`, `sum()`, `max()`, `min()`, `divmod()` |
| math Module | `sqrt()`, `factorial()`, `pow()`, `ceil()`, `floor()`, `gcd()`, `lcm()`, `log()`, `exp()` |
| Trigonometry | `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()` |
| Statistics | `mean()`, `median()`, `mode()`, `variance()`, `stdev()` |
| Random | `randint()`, `random()`, `choice()`, `shuffle()`, `sample()` |
| Decimal | `Decimal()` |
| Fraction | `Fraction()` |
| Complex | `.real`, `.imag`, `abs()` |
| Bitwise | `&`, `|`, `^`, `~`, `<<`, `>>` |

---

# Exam & Interview Points

- `/` always returns a **float**, while `//` performs **floor division**.
- `%` returns the **remainder** after division.
- `**` is used for exponentiation (power).
- `math.sqrt()` computes the square root of a number.
- `math.pi` and `math.e` are predefined mathematical constants.
- `statistics.mean()` returns the arithmetic mean.
- `random.randint(a, b)` returns a random integer between `a` and `b` (inclusive).
- `Decimal` provides precise decimal arithmetic, avoiding floating-point precision issues.
- `Fraction` represents numbers as exact rational values.
- `abs()` returns the absolute value of a number, including the magnitude of complex numbers.