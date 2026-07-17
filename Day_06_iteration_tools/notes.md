# __next__() Method in Python

## Introduction

`__next__()` is a special (magic/dunder) method in Python used to define the behavior of an **iterator**.

It is called automatically when we use the built-in `next()` function on an iterator object.

The `__next__()` method returns the **next value** from the iterator sequence.

---

## Syntax

```python
object.__next__()