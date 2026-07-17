import os

# Parent directory
parent_dir = "Projects"

# Nested directory
nested_dir = "Python/Day14"

# Create the complete directory structure
path = os.path.join(parent_dir, nested_dir)

os.makedirs(path, exist_ok=True)

print("Nested directory created successfully!")
print("Path:", path)