# Find Factors of a Number

## Problem

Print all the factors of a given number.

## Solution
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)


## Sample Output

Input:
12


Output:
1
2
3
4
6
12


## Concepts Learned

- for Loop
- Modulus Operator
- Conditional Statements