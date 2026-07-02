# Fibonacci Series Using Recursion

## Problem

Print the Fibonacci sequence using recursion.

## Solution

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")


## Sample Output

Input:
8

Output:
0 1 1 2 3 5 8 13

## Concepts Learned

- Recursion
- Functions
- Base Case
- Recursive Calls
- for Loop