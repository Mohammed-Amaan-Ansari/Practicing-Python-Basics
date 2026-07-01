# Find GCD (Greatest Common Divisor)

## Problem

Find the Greatest Common Divisor (GCD) of two numbers.

## Solution

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2

print(num1)
 

## Sample Output

Input:
48
18

Output:

6

## Concepts Learned

- Euclidean Algorithm
- while Loop
- Modulus Operator
- Multiple Assignment