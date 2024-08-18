num = int(input("Enter any number to find Factorial: "))

fact = 1
for i in range(1,num+1):
    fact = fact*i

print(f"Factorial of {num} is: {fact}")