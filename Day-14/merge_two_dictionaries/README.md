# Merge Two Dictionaries

## Problem

Merge two dictionaries into a single dictionary.

## Solution

```python
dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3,
    "d": 4
}

merged_dict = {**dict1, **dict2}

print(merged_dict)
```

## Sample Output

```text
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## Concepts Learned

- Dictionaries
- Dictionary Unpacking (`**`)
- Dictionary Operations