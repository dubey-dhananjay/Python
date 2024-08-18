per=int(input("Enter your Percentage: "));

if per>100 or per<=0:
    print("In-Valid Percentage")

elif per<=100 and per>=90:
    print("You have secured 'O' Grade")

elif per<90 and per>=80:
    print("You have secured 'A' Grade")

elif per<80 and per>=70:
    print("You have secured 'B' Grade")

elif per<70 and per>=60:
    print("You have secured 'C' Grade")

elif per<60 and per>=50:
    print("You have secured 'D' Grade")

elif per<50 and per>=35:
    print("You have secured 'P' Grade")

else:
    print("You have Failed")


