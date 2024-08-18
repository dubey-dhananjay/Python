# Basic Dictionary Operations
# Dictionaries are mutable. So we can perform add/delete/modify operations on a dictionary.

courses = { 'CS101' : 'CPP', 'CS102' : 'DS', 'CS201' : 'OOP', 'CS226' : 'DAA', 'CS601' : 'Crypt', 'CS442' : 'Web'}

# add, modify, delete

courses['CS444'] = 'Web Services' # add new key-value pair

courses['CS201'] = 'OOP Using java' # modify value for a key
del(courses['CS102']) # delete a key-value pair
del(courses) # delete dictionary object


# Note that any new addition will take place at the end of the existing dictionary, since dictionary preserves the insertion order.

# Dictionary keys cannot be changed in place.
# Given below are the operations that work on lists and tuples. These operations are discussed in detail in Chapter 8. Try these operations on dictionaries as an exercise.

# Concatenation - doesn't work Merging - doesn't work
# Conversion - works Aliasing - works
# Cloning - works Searching - works
# Identity - works Comparison - doesn't work
# Emptiness - works
# Two dictionaries cannot be concatenated using +.
# Two dictionaries cannot be merged using the form z = s + t.
# Two dictionary objects cannot be compared using <, >.