alpha=ord('A')

k=1

for i in range(1,6):
    for j in range (1,i+1):
        print(chr(alpha+k-1),end=" ")
        k+=1
    print()



'''
OUTPUT: 

A 
B C 
D E F 
G H I J 
K L M N O 
'''

