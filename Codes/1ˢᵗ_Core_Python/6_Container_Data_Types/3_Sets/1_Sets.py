# Sets

# Sets are like lists, with an exception that they do not contain duplicate entries. 

a = {} # This way of representing empty set is wrong
a = set()   # empty set, use () instead of {}

b = {20}    # set with one item
c = {"Sanjay", 25, 34555.505}    # set with multiple items

d = {10, 10, 10, 10, 10}
print(d)    # prints {10}


# Note: While storing element in a set, its hash value is computed using a hashing technique to determine where it should be stored in the set. 


s = {12, 23, 45, 16, 52}
t = {16, 52, 12, 23, 45}
u = {52, 12, 16, 45, 23}

print(s)    # prints {16, 52, 23, 12, 45}
print(t)    # prints {16, 52, 23, 12, 45}
print(u)    # prints {16, 52, 23, 12, 45}




# It is possible to create a set of strings and tuples, but not a set of lists

s1 = {"Morning", "Evening"}     # works because strings are immutable
s2 = {(12, 23), (15, 25), (17, 34)}     # works because tuples are immutable
s3 = {[12, 23], [15, 25], [17, 34]} # error because list are mutable


# Since strings and tuples are immutable, their hash value remains same at all times. Hence a set of strings or tuples is permitted. However, a list may change, so its hash value may change, hence a set of lists is not permitted.






# Accessing Set Elements
# Entire set can be printed by just using the name of the set. Set is an unordered collection. Hence order of insertion is not same as the order of access.

s = {15, 25, 35, 45, 55}
print(s)    # prints {35, 45, 15, 55, 25}





# Being an unordered collection, items in a set cannot be accessed using indices.

# Sets cannot be sliced using [ ].