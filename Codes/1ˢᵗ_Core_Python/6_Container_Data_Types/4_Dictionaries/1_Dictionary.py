# What are Dictionaries?
# Dictionary is a collection of key-value pairs.
# Dictionaries are also known as maps or associative arrays.
# A dictionary contains comma separated key : value pairs enclosed within { }.



d1 = { } # empty dictionary
d2 = {'A101' : 'Amol', 'A102' : 'Anil', 'B103' : 'Ravi'}

# Here, 'A101', 'A102', 'B103' are keys, whereas, 'Amol', 'Anil', 'Ravi' are values.

# Different keys may have same values.

d = {10 : 'A', 20 : 'A', 30 : 'Z'} # ok


# Keys must be unique. If keys are same, but values are different, latest key value pair getsstored.

d = {10 : 'A', 20 : 'B', 10 : 'Z'} # will store {10 : 'Z', 20 : 'B'}

# If key value pairs are repeated, then only one pair gets stored.

d = {10 : 'A', 20 : 'B', 10 : 'A'} # will store {10 : 'A', 20 : 'B'}







# Accessing Dictionary Elements
# Entire dictionary can be printed by just using the name of the dictionary.

d = {'A101' : 'Amol', 'A102' : 'Anil', 'B103' : 'Ravi'}
print(d)


# Unlike sets, dictionaries preserve insertion order. However, elements are not accessed using the position, but using the key.

d = {'A101' : 'Dinesh', 'A102' : 'Shrikant', 'B103' : 'Sudhir'}
print(d['A102']) # prints value for key 'A102'

# Thus, elements are not position indexed, but key indexed.
# Dictionaries cannot be sliced using [ ].