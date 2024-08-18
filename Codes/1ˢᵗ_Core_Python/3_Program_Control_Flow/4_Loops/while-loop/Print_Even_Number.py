#Even Numbers
def main():
    i=int(input("Enter the Initial Value: "))
    f=int(input("Enter the Final Value: "))
    
    while i <= f:
        if i % 2 == 0:
            #print(i, end=" ")
            print("Even Number is:",i)
        i += 1

main()

