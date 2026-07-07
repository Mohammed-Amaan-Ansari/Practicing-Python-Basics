text = input("Enter a sentence: ")

words = text.split()

words.sort()

print("Words in Alphabetical Order:")

for word in words:
    print(word)