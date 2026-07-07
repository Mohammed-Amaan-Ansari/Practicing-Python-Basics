# Sort Words in Alphabetical Order

## Problem

Sort the words of a sentence in alphabetical order.

## Solution

```python
text = input("Enter a sentence: ")

words = text.split()

words.sort()

for word in words:
    print(word)
```

## Sample Output

Input:

```text
python is easy to learn
```

Output:

```text
easy
is
learn
python
to
```

## Concepts Learned

- `split()` Method
- Lists
- `sort()` Method
- for Loop