# Prime Numbers in an Interval

## Problem
Print all prime numbers within a given interval.

## Solution

```python
start = 1
end = 50

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

### Concepts Learned
Nested Loops
Prime Number Logic
break Statement
for-else Loop