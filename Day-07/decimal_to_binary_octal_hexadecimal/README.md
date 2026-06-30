# Convert Decimal to Binary, Octal, and Hexadecimal

## Problem

Convert a decimal number to binary, octal, and hexadecimal.

## Solution

```python
num = int(input("Enter a decimal number: "))

print("Binary      :", bin(num))
print("Octal       :", oct(num))
print("Hexadecimal :", hex(num))
```

## Sample Output

Input:
25

Output:
Binary      : 0b11001
Octal       : 0o31
Hexadecimal : 0x19

## Concepts Learned

- Number System Conversion
- Built-in Functions (`bin()`, `oct()`, `hex()`)
- User Input