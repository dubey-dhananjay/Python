num=int(input("Enter the Number: "))

if num>0 and num<=20:
    print(f"{num} is in Range of 0-20")

elif num>20 and num<=40:
    print(f"{num} is in Range of 21-40")

elif num>40 and num<=60:
    print(f"{num} is in Range of 41-60")

elif num>60 and num<=80:
    print(f"{num} is in Range of 61-80")

elif num>80 and num<=100:
    print(f"{num} is in Range of 81-100")

elif num>100 or num<0:
    print("In-Valid")

    