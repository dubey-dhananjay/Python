# Set Methods
# Any set is an object of type set. Its methods can be accessed using the syntax s.method( ). Usage of commonly used set methods is shown below:

s = {12, 15, 13, 23, 22, 16, 17}
t = {'A', 'B', 'C'}

u = set ( ) # empty set
s.add('Hello') # adds 'Hello' to s
s.update(t) # adds elements of t to s






u = s.copy( ) # performs deep copy (cloning)
s.remove(15) # deletes 15 from s
s.remove(101) # would raise error, as 101 is not a member of s
s.discard(12) # removes 12 from s
s.discard(101) # won't raise an error, though 101 is not in s
s.clear( ) # removes all elements
# Following methods can be used on 2 sets to check the relationship between them:

s = {12, 15, 13, 23, 22, 16, 17}
t = {13, 15, 22}

print(s.issuperset(t)) # prints True
print(s.issubset(t)) # prints False
print(s.isdisjoint(t)) # prints False