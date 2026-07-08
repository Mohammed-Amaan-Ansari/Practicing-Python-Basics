# Count the Number of Each Vowel

## Problem

Count the occurrences of each vowel (a, e, i, o, u) in a given string.

## Solution

```python
text = input("Enter a string: ").lower()

vowels = "aeiou"

count = {}

for vowel in vowels:
    count[vowel] = text.count(vowel)

for vowel, total in count.items():
    print(f"{vowel}: {total}")
```

## Sample Output

Input:

```text
Hello World
```

Output:

```text
a: 0
e: 1
i: 0
o: 2
u: 0
```

## Concepts Learned

- Strings
- Dictionaries
- `count()` Method
- for Loop
- String Manipulation