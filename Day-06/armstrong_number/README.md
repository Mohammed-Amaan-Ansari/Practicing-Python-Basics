# Armstrong Number

## Problem
Check whether a given number is an Armstrong number.

## Solution

 
num = int(input("Enter a number: "))

order = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
 

## Sample Output

Input:
 153
 

Output:
Armstrong Number
 

## Concepts Learned

- while loop
- Modulus operator
- Integer division
- Exponent operator (`**`)
- Conditional statements