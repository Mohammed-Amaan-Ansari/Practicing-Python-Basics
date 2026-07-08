text = input("Enter a string: ").lower()

vowels = "aeiou"

count = {}

for vowel in vowels:
    count[vowel] = text.count(vowel)

print("Vowel Counts:")

for vowel, total in count.items():
    print(f"{vowel}: {total}")