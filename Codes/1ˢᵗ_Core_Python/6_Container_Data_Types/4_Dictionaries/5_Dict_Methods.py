# Dictionary Methods

# There are many dictionary methods. Many of the operations performed by them can also be performed using built-in functions.
# The useful dictionary methods are shown below:

c = { 'CS101' : 'CPP', 'CS102' : 'DS', 'CS201' : 'OOP'}
d = { 'ME126' : 'HPE', 'ME102' : 'TOM', 'ME234' : 'AEM'}

print(c.get('CS102', 'Absent')) # prints DS
print(c.get('EE102', 'Absent')) # prints Absent
print(c['EE102']) # raises keyerror
c.update(d) # updates c with items in d
print(c.popitem( )) # removes and returnsitem in LIFO order
print(c.pop('CS102')) # removes key and returns its value

c.clear( ) # clears all dictionary entries




animals = {'Tiger' : 141, 'Lion' : 152, 'Leopard' : 110}

birds = {'Eagle' : 38, 'Crow': 3, 'Parrot' : 2}

combined = {** animals, ** birds }



lst = [12, 13, 14, 15, 16]
d = dict.fromkeys(lst, 25) # keys - list items, all values set to 25

print(d)

# prints {12: 25, 13: 25, 14: 25, 15: 25, 16: 25}