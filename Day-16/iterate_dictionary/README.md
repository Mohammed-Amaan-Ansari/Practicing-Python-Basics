# Iterate Over a Dictionary

## Problem

Iterate through all key-value pairs in a dictionary.

## Solution

```python
student = {
    "Name": "Amaan",
    "Age": 21,
    "Course": "CSE",
    "CGPA": 8.93
}

for key, value in student.items():
    print(f"{key}: {value}")
```

## Sample Output

```text
Name: Amaan
Age: 21
Course: CSE
CGPA: 8.93
```

## Concepts Learned

- Dictionaries
- `items()` Method
- `for` Loop
- Key-Value Pairs