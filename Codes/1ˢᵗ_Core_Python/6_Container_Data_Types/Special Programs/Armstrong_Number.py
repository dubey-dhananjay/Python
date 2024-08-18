# Write a program to check whether a given 3-digit number is an Armstrong number or not.

# What is an Armstrong number?

# Definition of the Armstrong Number
# An n-digit Armstrong number is a special number which is equal to the sum of its own digits, each raised to the power of n.

# An 3-digit Armstrong number is a special number which is equal to the sum of its own digits, each raised to the power of 3.

num = int(input("Enter a 3-digit Number: "))
sum = 0
temp = num

while temp>0:
    digit = temp % 10
    sum += digit**3
    temp //= 10

if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")