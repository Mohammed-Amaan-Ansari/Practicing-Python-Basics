start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong Numbers:")

for num in range(start, end + 1):
    order = len(str(num))
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if sum == num:
        print(num)