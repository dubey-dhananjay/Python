# Looping in Dictionaries
# Like strings, lists, tuples and sets, dictionaries too can be iterated over using a for loop. There are three ways to do so:

courses = {'DAA' : 'CS', 'AOA' : 'ME', 'SVY' : 'CE' }
# iterate over key-value pairs

for k, v in courses.items( ) :
    print(k, v)

# iterate over keys

for k in courses.keys( ) :
    print(k)

# iterate over keys - shorter way
for k in courses :
    print(k)

# iterate over values
for v in courses.values( ) :
    print(v)


# While iterating through a dictionary using a for loop, if we wish to keep track of index of the key-value pairs that is being referred to, we can do so using the built-in enumerate( ) function.

courses = {'DAA' : 'CS', 'AOA' : 'ME', 'SVY' : 'CE' }

for i, (k, v) in enumerate(courses.items( )) :
    print(i,k)

# Note that ( ) around k, v are necessary.