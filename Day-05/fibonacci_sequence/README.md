# Fibonacci Sequence

## Problem
Print the Fibonacci sequence up to a specified number of terms.

## Solution

```python
n = int(input("Enter the number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

## Sample Output

Input:

```text
7
```

Output:

```text
0 1 1 2 3 5 8
```

## Concepts Learned

- Variables
- Multiple Assignment
- for loop
- Sequence Generation