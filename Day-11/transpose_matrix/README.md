# Transpose of a Matrix

## Problem

Find the transpose of a matrix.

## Solution

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)

for row in transpose:
    print(row)
```

## Sample Output

```text
[1, 4]
[2, 5]
[3, 6]
```

## Concepts Learned

- Nested Lists
- Nested Loops
- Matrix Transpose
- Indexing