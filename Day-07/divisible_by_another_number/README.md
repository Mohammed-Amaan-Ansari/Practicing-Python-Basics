# Check Divisibility

## Problem

Check whether one number is divisible by another.

## Solution

```python
num = int(input("Enter the first number: "))
divisor = int(input("Enter the second number: "))

if divisor == 0:
    print("Division by zero is not allowed.")
elif num % divisor == 0:
    print("Divisible")
else:
    print("Not Divisible")
```

## Sample Output

Input:
20
5


Output:
Divisible


## Concepts Learned

- Modulus Operator (%)
- Conditional Statements
- User Input