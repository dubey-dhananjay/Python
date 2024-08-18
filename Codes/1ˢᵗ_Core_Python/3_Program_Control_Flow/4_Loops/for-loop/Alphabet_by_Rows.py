alpha=ord('A')

k=1

for i in range(1,6):
    for j in range (1,i+1):
        print(chr(alpha+i-1),end=" ")
        k+=1
    print()



'''
OUTPUT:
A 
B B 
C C C 
D D D D 
E E E E E 
'''
