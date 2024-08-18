# List Varieties

# It is possible to create a nested list

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

c = [a, b]
print(c)

print(c[0][0] , c[1][2]) # 0th Element of 0th list, 2nd element of 1st list






# A list may be embedded in another list

x = [1, 2, 3, 4]; 
y = [10, 20, x, 30]; 

print(y)        # prints [10, 20, [1, 2, 3, 4], 30]







# It is possible to unpack a string or list within a list using the * operator

s = "Hello"
l = [*s]
print(l)    # prints ['H', 'e', 'l', 'l', 'o']

x = [1, 2, 3, 4]

y = [10, 20, 30]; 
y = [10, 20, *x, 30]; 

print(y)    # prints [10, 20, 1, 2, 3, 4, 30]