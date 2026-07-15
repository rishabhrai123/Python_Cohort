# Python Object Types / Data Types

Python is a **dynamically typed** and **object-oriented** programming language. Every value in Python is an object, and every object belongs to a particular data type (class).

---

# 1. Numbers

Numbers are used to store numeric values.

## Types of Numbers

- Integer (`int`)
- Floating Point (`float`)
- Complex (`complex`)
- Binary (`0b`)
- Decimal (`Decimal`)
- Fraction (`Fraction`)

## Examples

```python
a = 1234          # Integer
b = 3.14          # Float
c = 3 + 4j        # Complex
d = 0b111         # Binary (7)

from decimal import Decimal
x = Decimal("10.55")

from fractions import Fraction
y = Fraction(3, 4)
```

## Common Operations

```python
10 + 5
10 - 5
10 * 5
10 / 5
10 // 3
10 % 3
2 ** 5
```

---

# 2. Strings

A string is a sequence of Unicode characters.

## Declaration

```python
s1 = 'spam'
s2 = "Bob's"
s3 = """Multi-line
String"""
```

## Byte String

```python
b = b'a\x01c'
```

## Unicode String

```python
u = u'spam'
```

## String Operations

```python
len(s)
s.upper()
s.lower()
s.replace()
s.split()
s.strip()
```

## Example

```python
name = "Python"

print(name[0])
print(name[-1])
print(name[0:3])
```

---

# 3. Lists

Lists are ordered, mutable collections.

## Creating Lists

```python
a = [1, 2, 3]
b = [1, [2, "three"], 4.5]
c = list(range(10))
```

## List Methods

```python
append()
insert()
remove()
pop()
sort()
reverse()
extend()
```

## Example

```python
nums = [10,20,30]

nums.append(40)
nums.remove(20)

print(nums)
```

---

# 4. Tuples

Tuples are ordered but immutable collections.

## Creating Tuples

```python
t = (1, "spam", 4, "U")
```

```python
tuple("spam")
```

Output

```
('s','p','a','m')
```

## Named Tuple

```python
from collections import namedtuple

Student = namedtuple("Student",["name","age"])

s = Student("Rahul",20)

print(s.name)
```

### Advantages

- Faster than list
- Immutable
- Can be dictionary keys

---

# 5. Dictionary

Dictionary stores data in key-value pairs.

## Creating Dictionary

```python
d = {
    "food":"spam",
    "taste":"yum"
}
```

or

```python
d = dict(hours=10)
```

## Operations

```python
d.keys()
d.values()
d.items()
d.get()
d.update()
d.pop()
```

## Example

```python
student = {
    "name":"Ravi",
    "age":20
}

print(student["name"])
```

---

# 6. Set

Sets store unique elements.

## Creating Set

```python
set("abc")
```

```python
{'a','b','c'}
```

## Operations

```python
add()
remove()
union()
intersection()
difference()
```

## Example

```python
A = {1,2,3}
B = {3,4,5}

print(A | B)
print(A & B)
```

---

# 7. Files

Python supports file handling using `open()`.

## Open File

```python
open("eggs.txt")
```

Windows Example

```python
open(r"C:\ham.bin","wb")
```

## Modes

| Mode | Meaning |
|------|----------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| b | Binary |
| t | Text |

## Example

```python
file = open("data.txt","w")

file.write("Hello")

file.close()
```

---

# 8. Boolean

Boolean stores logical values.

```python
True
False
```

## Example

```python
5 > 3

True
```

```python
10 < 5

False
```

Used in

- if
- while
- comparisons
- logical expressions

---

# 9. None

Represents absence of value.

```python
x = None
```

Example

```python
def fun():
    pass

print(fun())
```

Output

```
None
```

---

# 10. Functions

Functions are reusable blocks of code.

## Example

```python
def add(a,b):
    return a+b

print(add(5,3))
```

### Types

- Built-in
- User-defined
- Lambda
- Recursive

---

# 11. Modules

A module is a Python file containing functions and variables.

Example

```python
import math

print(math.sqrt(25))
```

Popular Modules

- math
- random
- os
- sys
- datetime

---

# 12. Classes (OOP)

Class is a blueprint for creating objects.

## Example

```python
class Student:

    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

s = Student("Rahul")

s.show()
```

---

# Advanced Python Concepts

---

# 13. Decorators

A decorator modifies the behavior of a function without changing its code.

## Syntax

```python
def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper

@decorator
def hello():
    print("Hello")

hello()
```

Output

```
Before
Hello
After
```

### Uses

- Logging
- Authentication
- Timing
- Access Control

---

# 14. Generators

Generators generate values one by one using `yield`.

## Example

```python
def numbers():

    yield 1
    yield 2
    yield 3

for i in numbers():
    print(i)
```

### Advantages

- Memory efficient
- Lazy evaluation
- Faster for large datasets

---

# 15. Iterators

Iterator is an object that can be traversed one element at a time.

## Example

```python
nums = [10,20,30]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
```

Output

```
10
20
30
```

---

# 16. Comprehensions

A concise way of creating collections.

## List Comprehension

```python
square = [x*x for x in range(6)]
```

## Dictionary Comprehension

```python
square = {x:x*x for x in range(5)}
```

## Set Comprehension

```python
cube = {x*x*x for x in range(5)}
```

---

# 17. Context Managers

Automatically manage resources like files.

## Example

```python
with open("file.txt","r") as f:

    data = f.read()

print(data)
```

### Advantages

- Automatically closes file
- Cleaner code
- Handles exceptions

---

# 18. Metaprogramming

Writing code that manipulates or generates other code.

Examples

- `type()`
- `getattr()`
- `setattr()`
- `hasattr()`
- `eval()`
- `exec()`
- Metaclasses

## Example

```python
class Student:
    pass

print(type(Student))
```

Output

```
<class 'type'>
```

---

# Summary Table

| Data Type | Mutable | Ordered | Example |
|------------|----------|----------|---------|
| int | No | N/A | 10 |
| float | No | N/A | 3.14 |
| complex | No | N/A | 3+4j |
| string | No | Yes | "Python" |
| list | Yes | Yes | [1,2,3] |
| tuple | No | Yes | (1,2,3) |
| dictionary | Yes | Yes | {"a":1} |
| set | Yes | No | {1,2,3} |
| boolean | No | N/A | True |
| None | No | N/A | None |
| file | Depends | Sequential | open("a.txt") |
| function | N/A | N/A | def fun() |
| module | N/A | N/A | import math |
| class | N/A | N/A | class Student |

---

# Important Interview / Exam Points

- Everything in Python is an object.
- List is mutable, Tuple is immutable.
- Dictionary stores key-value pairs.
- Set stores unique values.
- String is immutable.
- Generator uses `yield`.
- Iterator uses `iter()` and `next()`.
- Decorators modify functions without changing their source code.
- Context Managers use `with`.
- Comprehensions create collections in a single line.
- Metaprogramming allows programs to inspect or modify themselves.