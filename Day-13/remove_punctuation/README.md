# Illustrate Different Set Operations

## Problem

Perform different set operations such as Union, Intersection, Difference, and Symmetric Difference.

## Solution

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
```

## Sample Output

```text
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
Symmetric Difference: {1, 2, 5, 6}
```

## Concepts Learned

- Sets
- Union (`|`)
- Intersection (`&`)
- Difference (`-`)
- Symmetric Difference (`^`)