# Convert Decimal to Binary, Octal, and Hexadecimal Using Recursion

## Problem

Convert a decimal number into Binary, Octal, and Hexadecimal using recursion.

## Solution

def convert(num, base):
    digits = "0123456789ABCDEF"

    if num < base:
        return digits[num]
    return convert(num // base, base) + digits[num % base]

number = int(input("Enter a decimal number: "))

print(convert(number, 2))
print(convert(number, 8))
print(convert(number, 16))


## Sample Output

Input:
25

Output:

```text
Binary      : 11001
Octal       : 31
Hexadecimal : 19
```

## Concepts Learned

- Recursion
- Number System Conversion
- String Indexing
- Functions