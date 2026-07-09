# Find Size of an Image

## Problem

Find the width and height of an image.

## Prerequisites

Install the Pillow library:

```bash
pip install pillow
```

## Solution

```python
from PIL import Image

image = Image.open("sample.jpg")

width, height = image.size

print("Width :", width)
print("Height:", height)
```

## Sample Output

```text
Width : 1920
Height: 1080
```

## Concepts Learned

- Pillow Library
- Opening Images
- Image Dimensions
- Tuple Unpacking