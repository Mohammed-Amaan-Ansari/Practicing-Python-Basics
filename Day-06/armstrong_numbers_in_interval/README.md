# Armstrong Numbers in an Interval

## Problem
Print all Armstrong numbers within a given interval.

## Solution

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

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
 

## Sample Output

Input:
100
500

Output:
153
370
371
407
## Concepts Learned

- Nested loops
- while loop
- Range
- Armstrong number logic