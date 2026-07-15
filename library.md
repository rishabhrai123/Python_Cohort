# Python Libraries – Complete Notes

Python libraries are collections of pre-written code (modules and packages) that provide reusable functionality. They help developers perform tasks such as mathematics, data analysis, web development, machine learning, automation, networking, and more.

---

# What is a Library?

A **library** is a collection of modules containing functions, classes, and variables that can be imported into a Python program.

## Syntax

```python
import library_name
```

Example

```python
import math

print(math.sqrt(25))
```

Output

```
5.0
```

---

# Types of Python Libraries

1. Standard Library (Built-in)
2. Third-Party Library
3. User-Defined Library

---

# 1. Standard Library

The Python Standard Library comes pre-installed with Python.

Examples

- math
- random
- os
- sys
- datetime
- time
- statistics
- decimal
- fractions
- json
- csv
- pathlib
- shutil
- itertools
- collections

---

# 2. Third-Party Libraries

These libraries must be installed using **pip**.

Installation

```bash
pip install library_name
```

Example

```bash
pip install numpy
```

Popular Third-Party Libraries

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow
- PyTorch
- Flask
- Django
- OpenCV
- BeautifulSoup
- Requests

---

# 3. User-Defined Library

You can create your own module.

Example

Create file

```python
# calculator.py

def add(a,b):
    return a+b
```

Use it

```python
import calculator

print(calculator.add(10,20))
```

---

# Import Statements

Import Entire Library

```python
import math
```

Import Specific Function

```python
from math import sqrt
```

Import Multiple Functions

```python
from math import sqrt,factorial
```

Import with Alias

```python
import numpy as np
```

Import Everything

```python
from math import *
```

---

# Common Python Libraries

---

# math Library

Provides mathematical functions.

Import

```python
import math
```

Functions

```python
math.sqrt(25)

math.factorial(5)

math.pow(2,5)

math.ceil(4.2)

math.floor(4.8)

math.gcd(20,30)

math.lcm(12,18)

math.log(100)

math.log10(100)

math.exp(2)
```

Constants

```python
math.pi

math.e

math.tau

math.inf

math.nan
```

---

# random Library

Generates random values.

Import

```python
import random
```

Functions

```python
random.random()

random.randint(1,100)

random.uniform(1,10)

random.choice(["A","B","C"])

random.shuffle(list1)

random.sample(range(100),5)
```

---

# os Library

Provides operating system functions.

Import

```python
import os
```

Functions

```python
os.getcwd()

os.chdir()

os.mkdir()

os.rmdir()

os.listdir()

os.remove()

os.rename()
```

Example

```python
import os

print(os.getcwd())
```

---

# sys Library

Interacts with the Python interpreter.

Import

```python
import sys
```

Functions

```python
sys.version

sys.platform

sys.exit()

sys.argv
```

---

# datetime Library

Works with dates and times.

Import

```python
import datetime
```

Example

```python
today = datetime.datetime.now()

print(today)
```

Functions

```python
datetime.date.today()

datetime.datetime.now()

datetime.timedelta(days=5)
```

---

# time Library

Provides time-related functions.

Import

```python
import time
```

Functions

```python
time.time()

time.sleep(5)

time.localtime()

time.ctime()
```

---

# statistics Library

Performs statistical calculations.

Import

```python
import statistics
```

Functions

```python
statistics.mean(data)

statistics.median(data)

statistics.mode(data)

statistics.stdev(data)

statistics.variance(data)
```

---

# decimal Library

Provides high precision decimal arithmetic.

Import

```python
from decimal import Decimal
```

Example

```python
a = Decimal("0.1")

b = Decimal("0.2")

print(a+b)
```

---

# fractions Library

Works with rational numbers.

Import

```python
from fractions import Fraction
```

Example

```python
Fraction(3,4)

Fraction(1,2)+Fraction(1,3)
```

---

# collections Library

Provides advanced container data types.

Import

```python
from collections import *
```

Popular Classes

- Counter
- deque
- namedtuple
- OrderedDict
- defaultdict

Example

```python
from collections import Counter

Counter("python")
```

---

# itertools Library

Provides efficient looping tools.

Import

```python
import itertools
```

Functions

```python
count()

cycle()

repeat()

product()

permutations()

combinations()
```

Example

```python
from itertools import combinations

print(list(combinations([1,2,3],2)))
```

---

# pathlib Library

Object-oriented file system paths.

Import

```python
from pathlib import Path
```

Example

```python
p = Path("notes.txt")

print(p.exists())
```

---

# shutil Library

Performs high-level file operations.

Import

```python
import shutil
```

Functions

```python
copy()

move()

rmtree()

copytree()
```

---

# json Library

Works with JSON data.

Import

```python
import json
```

Convert Dictionary to JSON

```python
json.dumps(data)
```

Convert JSON to Dictionary

```python
json.loads(data)
```

---

# csv Library

Reads and writes CSV files.

Import

```python
import csv
```

Read CSV

```python
with open("data.csv") as file:
    reader = csv.reader(file)
```

Write CSV

```python
writer.writerow(["Name","Age"])
```

---

# re Library

Regular Expressions.

Import

```python
import re
```

Functions

```python
re.search()

re.findall()

re.match()

re.sub()

re.split()
```

Example

```python
re.findall(r"\d+","Age 21")
```

---

# requests Library

Used for HTTP requests.

Install

```bash
pip install requests
```

Example

```python
import requests

response = requests.get("https://example.com")

print(response.status_code)
```

---

# NumPy Library

Numerical computing.

Install

```bash
pip install numpy
```

Import

```python
import numpy as np
```

Example

```python
arr = np.array([1,2,3])

print(arr.mean())
```

Uses

- Arrays
- Matrix Operations
- Linear Algebra
- Scientific Computing

---

# Pandas Library

Data analysis.

Install

```bash
pip install pandas
```

Import

```python
import pandas as pd
```

Example

```python
df = pd.read_csv("students.csv")

print(df.head())
```

Uses

- Data Cleaning
- Data Analysis
- CSV Handling
- Excel Processing

---

# Matplotlib Library

Data visualization.

Install

```bash
pip install matplotlib
```

Example

```python
import matplotlib.pyplot as plt

plt.plot([1,2,3],[2,4,6])

plt.show()
```

---

# Seaborn Library

Advanced statistical visualization.

Install

```bash
pip install seaborn
```

Example

```python
import seaborn as sns
```

---

# OpenCV Library

Computer Vision.

Install

```bash
pip install opencv-python
```

Import

```python
import cv2
```

Uses

- Image Processing
- Face Detection
- Object Detection
- Video Processing

---

# Flask Library

Python Web Framework.

Install

```bash
pip install flask
```

Example

```python
from flask import Flask

app = Flask(__name__)
```

Uses

- REST APIs
- Web Applications

---

# Django Library

Full Stack Python Framework.

Install

```bash
pip install django
```

Create Project

```bash
django-admin startproject myproject
```

Uses

- Websites
- Admin Panel
- Authentication
- Database Management

---

# TensorFlow Library

Machine Learning and Deep Learning.

Install

```bash
pip install tensorflow
```

Import

```python
import tensorflow as tf
```

Uses

- AI
- Neural Networks
- Image Recognition

---

# PyTorch Library

Deep Learning Library.

Install

```bash
pip install torch
```

Import

```python
import torch
```

Uses

- AI
- Machine Learning
- Research

---

# BeautifulSoup Library

Web Scraping.

Install

```bash
pip install beautifulsoup4
```

Import

```python
from bs4 import BeautifulSoup
```

Uses

- HTML Parsing
- Web Data Extraction

---

# Library vs Module vs Package

| Feature | Module | Package | Library |
|---------|--------|---------|---------|
| Definition | Single Python file | Collection of modules | Collection of packages/modules |
| Example | math.py | numpy | TensorFlow |
| Extension | .py | Folder | Large project |

---

# pip Commands

Install Library

```bash
pip install numpy
```

Upgrade Library

```bash
pip install --upgrade numpy
```

Uninstall Library

```bash
pip uninstall numpy
```

List Installed Libraries

```bash
pip list
```

Show Library Information

```bash
pip show numpy
```

Freeze Installed Packages

```bash
pip freeze
```

---

# Summary Table

| Library | Purpose |
|----------|---------|
| math | Mathematical functions |
| random | Random numbers |
| os | Operating system operations |
| sys | Python interpreter information |
| datetime | Date and time handling |
| time | Time-related functions |
| statistics | Statistical calculations |
| decimal | High-precision decimal arithmetic |
| fractions | Rational number operations |
| collections | Specialized container types |
| itertools | Efficient iterators |
| pathlib | File and path handling |
| shutil | File copying and moving |
| json | JSON processing |
| csv | CSV file handling |
| re | Regular expressions |
| requests | HTTP requests |
| NumPy | Numerical computing |
| Pandas | Data analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| OpenCV | Computer vision |
| Flask | Lightweight web framework |
| Django | Full-stack web framework |
| TensorFlow | Machine learning |
| PyTorch | Deep learning |
| BeautifulSoup | Web scraping |

---

# Exam & Interview Points

- **Standard libraries** come pre-installed with Python.
- **Third-party libraries** must be installed using `pip`.
- Use `import library_name` to import an entire library.
- Use `from library import function` to import specific functions.
- `math` is used for mathematical operations.
- `random` generates random values.
- `os` and `pathlib` are used for file and directory management.
- `json` is used for JSON data exchange.
- `requests` is commonly used to interact with web APIs.
- `NumPy` and `Pandas` are essential libraries for data science.
- `Flask` and `Django` are popular Python web frameworks.