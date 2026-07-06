# Matrix Multiplication

## Problem

Multiply two matrices.

## Solution

```python
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0],
    [0, 0]
]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    print(row)
```

## Sample Output

```text
[19, 22]
[43, 50]
```

## Concepts Learned

- Nested Loops
- Matrix Multiplication
- Indexing
- List Representation of Matrices