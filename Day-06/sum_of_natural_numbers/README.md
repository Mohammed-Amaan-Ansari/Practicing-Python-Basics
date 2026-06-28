# Sum of Natural Numbers

## Problem
Find the sum of the first **n** natural numbers.

## Solution

n = int(input("Enter a positive integer: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)

## Sample Output

Input:
10

Output:
55

## Concepts Learned

- for loop
- range()
- Accumulator pattern
- Arithmetic operations