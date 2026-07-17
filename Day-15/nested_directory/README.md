# Create a Nested Directory

## Problem

Create a nested directory structure using Python.

## Solution

```python
import os

parent_dir = "Projects"
nested_dir = "Python/Day14"

path = os.path.join(parent_dir, nested_dir)

os.makedirs(path, exist_ok=True)

print("Nested directory created successfully!")
```

## Sample Output

```text
Nested directory created successfully!
Path: Projects/Python/Day14
```

## Concepts Learned

- `os` Module
- `os.makedirs()`
- Directory Creation
- File System Operations