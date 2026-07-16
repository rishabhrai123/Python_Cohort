# Python `repr()`, `str()`, and `print()` Notes

## Introduction

Python provides different ways to represent and display objects:

- `repr()` → Official representation (for developers)
- `str()` → Readable representation (for users)
- `print()` → Displays output on the screen

---

# 1. repr()

## Definition

The `repr()` function returns the **official string representation** of an object.

It is mainly used for:

- Debugging
- Logging
- Developers

### Syntax

```python
repr(object)
```

### Example

```python
name = "chai"

print(repr(name))
```

### Output

```
'chai'
```

Notice that the output includes **quotes**.

---

## Another Example

```python
text = "Hello\nPython"

print(repr(text))
```

### Output

```
'Hello\nPython'
```

The newline (`\n`) is shown as text instead of creating a new line.

---

# 2. str()

## Definition

The `str()` function returns the **human-readable string representation** of an object.

It is mainly used for displaying information to users.

### Syntax

```python
str(object)
```

### Example

```python
name = "chai"

print(str(name))
```

### Output

```
chai
```

No quotes are displayed.

---

## Another Example

```python
text = "Hello\nPython"

print(str(text))
```

### Output

```
Hello
Python
```

The `\n` is interpreted as a newline.

---

# 3. print()

## Definition

The `print()` function displays the given object on the console.

Internally, `print()` uses `str()` to convert the object into a readable format before displaying it.

### Syntax

```python
print(object)
```

### Example

```python
print("chai")
```

### Output

```
chai
```

---

# Comparison Example

```python
text = "Hello\nPython"

print(repr(text))
print(str(text))
print(text)
```

### Output

```
'Hello\nPython'
Hello
Python
Hello
Python
```

---

# Difference Table

| Feature | repr() | str() | print() |
|---------|---------|--------|----------|
| Purpose | Official representation | Readable representation | Display output |
| Used For | Developers, debugging | Users | Console output |
| Shows Quotes | Yes | No | No |
| Shows Escape Characters | Yes | No | No |
| Return Type | String | String | None |

---

# Example with List

```python
numbers = [10, 20, 30]

print(repr(numbers))
print(str(numbers))
```

### Output

```
[10, 20, 30]
[10, 20, 30]
```

For lists, both outputs look similar.

---

# Example with String

```python
name = "Python"

print(repr(name))
print(str(name))
```

### Output

```
'Python'
Python
```

---

# Example with Newline

```python
msg = "Hello\nWorld"

print(repr(msg))
print(str(msg))
```

### Output

```
'Hello\nWorld'
Hello
World
```

---

# Return Values

| Function | Returns |
|----------|----------|
| `repr()` | String |
| `str()` | String |
| `print()` | None |

Example

```python
x = print("Hello")

print(x)
```

Output

```
Hello
None
```

---

# Key Points

- `repr()` returns the official representation of an object.
- `str()` returns a user-friendly representation.
- `print()` displays output on the console.
- `repr()` is mainly used for debugging.
- `str()` is mainly used for user-friendly output.
- `print()` automatically calls `str()` on objects.
- `repr()` displays escape characters such as `\n` and `\t`.
- `str()` interprets escape characters.

---

# Interview Questions

### 1. What is `repr()`?

`repr()` returns the official string representation of an object.

---

### 2. What is `str()`?

`str()` returns the readable string representation of an object.

---

### 3. What is the difference between `repr()` and `str()`?

| repr() | str() |
|---------|--------|
| Official representation | Readable representation |
| Used for debugging | Used for users |
| Shows quotes | Does not show quotes |
| Shows escape characters | Interprets escape characters |

---

### 4. What does `print()` return?

`print()` returns **None**.

---

### 5. Which function is mainly used for debugging?

**Answer:** `repr()`

---

# Summary

- **`repr()`** → Developer-friendly representation (includes quotes and escape characters).
- **`str()`** → User-friendly representation (easy to read).
- **`print()`** → Displays the `str()` representation on the console.