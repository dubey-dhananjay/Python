# Looping in Sets

# Like strings, lists and tuples, sets too can be iterated over using a for loop.

s = {12, 15, 13, 23, 22, 16, 17}

for ele in s :
    print(ele)

# OUTPUT:
# 16
# 17
# 22
# 23
# 12
# 13
# 15





# Note that unlike a string, list or tuple, a while loop should not be used to access the set elements. This is because we cannot access a set element using an index, as in s[i].

# Built-in function enumerate( ) can be used with a set. The enumeration is done on access order, not insertion order.