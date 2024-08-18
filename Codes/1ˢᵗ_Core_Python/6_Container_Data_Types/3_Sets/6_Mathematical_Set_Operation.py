# Mathematical Set Operations
# Following union, intersection and difference operations can be carried out on sets:
# sets
engineers = {'Vijay', 'Sanjay', 'Ajay', 'Sujay', 'Dinesh'}
managers = {'Aditya', 'Sanjay'}
# union - all people in both categories
print(engineers | managers)
# intersection - who are engineers and managers
print(engineers & managers)
# difference - engineers who are not managers
print(engineers - managers)
# difference - managers who are not engineers
print(managers - engineers)
# symmetric difference - managers who are not engineers
# and engineers who are not managers
print(managers ^ engineers)


a = {1, 2, 3, 4, 5}




b = {2, 4, 5}
print(a >= b) # prints True as a is superset of b
print(a <= b) # prints False as a is not a subset of b






# Updating Set Operations
# Mathematical set operations can be extended to update an existing set.

a |= b # update a with the result of a | b
a &= b # update a with the result of a & b
a -= b # update a with the result of a - b
a ^= b # update a with the result of a ^ b

# Set Varieties
# Unlike a list and tuple, a set cannot contain a set embedded in it.

s = {'gate', 'fate', {10, 20, 30}, 'late'} # error, nested sets

# It is possible to unpack a set using the *operator.
x = {1, 2, 3, 4}
print(*x) # outputs 1, 2, 3, 4