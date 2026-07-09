from PIL import Image

image = Image.open("sample.jpg")

width, height = image.size

print("Width :", width)
print("Height:", height)