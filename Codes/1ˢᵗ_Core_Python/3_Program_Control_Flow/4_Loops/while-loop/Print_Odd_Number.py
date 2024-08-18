#Odd Numbers
def main():
    i = int(input("Enter the Initial Value: "))
    f = int(input("Enter the Final Value: "))
    
    while i <= f:
        if i % 2 == 1:
            print("Odd Number:",i)
            #print(i, end=" ")
            #print(i)
        i += 1

main()
