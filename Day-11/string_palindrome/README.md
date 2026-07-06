# String Palindrome

## Problem

Check whether a given string is a palindrome.

## Solution

```python
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

## Sample Output

Input:

```text
madam
```

Output:

```text
Palindrome
```

## Concepts Learned

- String Slicing
- Conditional Statements
- User Input
- String Comparison