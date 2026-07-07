# Remove Punctuation from a String

## Problem

Remove all punctuation characters from a given string.

## Solution

```python
import string

text = input("Enter a string: ")

result = ""

for char in text:
    if char not in string.punctuation:
        result += char

print(result)
```

## Sample Output

Input:

```text
Hello, World! Welcome to Python.
```

Output:

```text
Hello World Welcome to Python
```

## Concepts Learned

- String Iteration
- `string.punctuation`
- Conditional Statements
- String Concatenation