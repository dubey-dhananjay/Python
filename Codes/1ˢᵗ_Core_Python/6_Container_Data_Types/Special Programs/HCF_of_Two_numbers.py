num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second Number: "))

if num1 < num2:
    smaller = num1
else:
    samller = num2

for i in range(1,smaller + 1):
    if ((num1 % i ==0) and (num2 % i == 0)):
        hcf = i
    
print(f"The HCF is {hcf}.")