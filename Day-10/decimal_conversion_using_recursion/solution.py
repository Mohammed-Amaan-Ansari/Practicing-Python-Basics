def convert(num, base):
    digits = "0123456789ABCDEF"

    if num < base:
        return digits[num]
    else:
        return convert(num // base, base) + digits[num % base]


number = int(input("Enter a decimal number: "))

print("Binary      :", convert(number, 2))
print("Octal       :", convert(number, 8))
print("Hexadecimal :", convert(number, 16))