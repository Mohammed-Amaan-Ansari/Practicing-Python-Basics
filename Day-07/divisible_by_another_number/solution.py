num = int(input("Enter the first number: "))
divisor = int(input("Enter the second number: "))

if divisor == 0:
    print("Division by zero is not allowed.")
elif num % divisor == 0:
    print(f"{num} is divisible by {divisor}")
else:
    print(f"{num} is not divisible by {divisor}")