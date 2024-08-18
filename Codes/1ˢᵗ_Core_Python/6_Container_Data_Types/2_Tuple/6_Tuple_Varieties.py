# It is possible to create a tuple of tuples.


# Example 1:
a = (1, 3, 5, 7, 9)
b = (2, 4, 6, 8, 10)

c = (a, b)
print(c)    # prints ((1, 3, 5, 7, 9), (2, 4, 6, 8, 10))

print(c[0][0], c[1][2]) # 0th element of 0th tuple, 2nd ele of 1st tuple

# OUTPUT: 1 6






# Example 2:
records = (
            ('Priyanka', 24, 3455.50), ('Shailesh', 25, 4555.50),
            ('Subhash', 25, 4505.50), ('Sugandh', 27, 4455.55)
          )

print(records[0][0], records[0][1], records[0][2])      # prints Priyanka 24 3455.5
print(records[1][0], records[1][1], records[1][2])      # prints Shailesh 25 4555.5

for n, a, s in records:
    print(n,a,s)


# OUTPUT: 

# Priyanka 24 3455.5
# Shailesh 25 4555.5
# Subhash 25 4505.5
# Sugandh 27 4455.55








# A tuple may be embedded in another tuple.

x = (1, 2, 3, 4)
y = (10, 20, x, 30)

print(y)    # outputs (10, 20, (1, 2, 3, 4), 30)



# It is possible to unpack a tuple within a tuple using the * operator.

x = (1, 2, 3, 4)
y = (10, 20, *x, 30)

print(y) # outputs (10, 20, 1, 2, 3, 4, 30)



# Tuple Unpacking:

my_tuple = (1, 2, 3)

a, b, c = my_tuple

print(a)  
print(b) 
print(c)  

# Output: 1
# Output: 2
# Output: 3