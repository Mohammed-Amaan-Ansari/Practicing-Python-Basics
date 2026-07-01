# Simple Calculator

## Problem

Create a simple calculator that performs addition, subtraction, multiplication, and division.

## Solution

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operator.")


## Sample Output

Input:

10
*
5


Output:
50.0


## Concepts Learned

- if-elif-else
- Arithmetic Operators
- User Input
- Nested Conditions