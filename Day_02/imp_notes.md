# Reference Count in Python

## What is Reference Count?

**Reference Count** is the number of references (variables, containers, functions, etc.) that point to a Python object.

Python uses **reference counting** as its primary memory management technique. Every object in Python keeps track of how many references point to it.

- If the reference count becomes **0**, Python automatically deallocates the object.
- This process is part of Python's **memory management**.
- Python also uses a **Garbage Collector (GC)** to handle circular references.

---

# How Reference Counting Works

When an object is created, its reference count starts at **1**.

```python
a = 10
```

Memory Representation

```
a
|
v
10
```

Reference Count = **1**

---

## Example 1: Multiple References

```python
a = 10
b = a
c = a
```

Memory

```
      a
      |
      |
      v
     10
    /  \
   b    c
```

Reference Count

```
10 → 3 references
```

---

## Example 2: Deleting References

```python
a = 10
b = a

del a
```

Memory

```
b
|
v
10
```

Reference Count

```
2 → 1
```

---

## Example 3: Object Deallocation

```python
a = [1, 2, 3]
b = a

del a
del b
```

Reference Count

```
2 → 1 → 0
```

Since the reference count becomes **0**, Python automatically removes the object from memory.

---

# Checking Reference Count

The `sys` module provides the `getrefcount()` function.

```python
import sys

a = []

print(sys.getrefcount(a))
```

Output

```
2
```

### Why is the output 2?

One reference comes from the variable `a`.

Another temporary reference is created when the object is passed to `getrefcount()`.

---

## Example

```python
import sys

x = [10, 20]

print(sys.getrefcount(x))

y = x

print(sys.getrefcount(x))

z = x

print(sys.getrefcount(x))
```

Possible Output

```
2
3
4
```

---

# Reference Count with Functions

```python
def display(data):
    print(data)

a = [1, 2]

display(a)
```

Memory

```
a
|
v
[1,2]
 ^
 |
data
```

- During the function call, the reference count increases by **1**.
- After the function returns, the reference count decreases.

---

# Reference Count with Lists

```python
a = [10, 20]

b = a

c = [a]
```

Memory

```
a --------\
           \
            > [10,20]
           /
b --------/

c ---> [ reference ]
```

Reference Count = **3**

---

# Reference Count with Dictionaries

```python
d = {}

x = d

y = {"obj": d}
```

Memory

```
x ----\
       \
        > {}
       /
d ----/

y
|
v
{"obj": {}}
```

Reference count increases because the dictionary is also referenced inside another dictionary.

---

# Mutable vs Immutable Objects

Reference counting works for **all Python objects**.

## Immutable Objects

- int
- float
- bool
- str
- tuple

Example

```python
a = 100
b = a
```

Reference Count = **2**

---

## Mutable Objects

- list
- dictionary
- set
- class objects

Example

```python
a = []
b = a
```

Reference Count = **2**

---

# Assigning a New Object

```python
a = [1, 2]

b = a

a = [3, 4]
```

Initially

```
a ----\
       \
        > [1,2]
       /
b ----/
```

After Reassignment

```
a ----> [3,4]

b ----> [1,2]
```

Reference Count

Old List

```
2 → 1
```

New List

```
1
```

---

# Circular References

Reference counting alone cannot remove circular references.

Example

```python
a = []
b = []

a.append(b)
b.append(a)
```

Memory

```
a ----> [ b ]
^         |
|         |
|         v
[ a ] <--- b
```

Even after

```python
del a
del b
```

the objects still reference each other.

Therefore, Python uses the **Garbage Collector (GC)** to detect and remove circular references.

---

# Garbage Collector (GC)

Import the garbage collector module

```python
import gc
```

Force garbage collection

```python
gc.collect()
```

Check whether garbage collection is enabled

```python
import gc

print(gc.isenabled())
```

Output

```
True
```

---

# Advantages of Reference Counting

- Simple memory management.
- Immediate object deallocation.
- Prevents most memory leaks.
- Fast object destruction.
- Easy to implement.

---

# Disadvantages

- Cannot detect circular references.
- Small performance overhead because every assignment updates the reference count.
- Requires an additional garbage collector for cyclic objects.

---

# Reference Count Lifecycle

```
Create Object
      │
      ▼
Reference Count = 1
      │
      ▼
More References Added
      │
      ▼
Reference Count Increases
      │
      ▼
References Deleted
      │
      ▼
Reference Count Decreases
      │
      ▼
Reference Count = 0
      │
      ▼
Object Deallocated
```

---

# Common Functions

| Function | Description |
|----------|-------------|
| `sys.getrefcount(obj)` | Returns the reference count of an object |
| `del variable` | Removes a reference to an object |
| `gc.collect()` | Forces garbage collection |
| `gc.isenabled()` | Checks if the garbage collector is enabled |

---

# Interview Questions

### 1. What is reference counting?

Reference counting is a memory management technique in Python where each object stores the number of references pointing to it. When the count becomes zero, the object is deallocated.

---

### 2. Which module is used to check the reference count?

The `sys` module using:

```python
sys.getrefcount(obj)
```

---

### 3. Why does `getrefcount()` return one extra reference?

Because the object is temporarily referenced while being passed as an argument to the function.

---

### 4. Can reference counting handle circular references?

No. Python's **Garbage Collector (GC)** handles circular references.

---

### 5. What happens when the reference count becomes zero?

Python automatically deallocates the object and frees its memory.

---

# Key Points

- Every Python object has a **reference count**.
- Python primarily uses **reference counting** for memory management.
- `sys.getrefcount()` returns the current reference count.
- `del` removes a reference to an object.
- Objects are deallocated when their reference count reaches **0**.
- Circular references are handled by the **Garbage Collector (GC)**.
- The `gc` module provides functions such as `gc.collect()` and `gc.isenabled()`.

---