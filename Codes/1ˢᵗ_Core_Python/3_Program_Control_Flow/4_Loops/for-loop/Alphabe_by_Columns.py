alpha=ord('A')

k=1

for i in range(1,6):
    for j in range (1,i+1):
        print(chr(alpha+j-1),end=" ")
        k+=1
    print()



'''
OUTPUT:
A 
A B 
A B C 
A B C D 
A B C D E
'''
