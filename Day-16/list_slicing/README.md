# List Slicing

## Problem

Access different portions of a list using slicing.

## Solution

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[:3])
print(numbers[-3:])
print(numbers[2:5])
print(numbers[::2])
print(numbers[::-1])
```

## Sample Output

```text
[10, 20, 30]
[50, 60, 70]
[30, 40, 50]
[10, 30, 50, 70]
[70, 60, 50, 40, 30, 20, 10]
```

## Concepts Learned

- List Slicing
- Slice Notation (`start:end:step`)
- Negative Indexing
- Reversing a List