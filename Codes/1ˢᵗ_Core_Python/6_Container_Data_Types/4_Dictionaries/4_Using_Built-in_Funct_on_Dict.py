# Using Built-in Functions on Dictionaries
# Many built-in functions can be used with dictionaries.

d = { 'CS101' : 'CPP', 'CS102' : 'DS', 'CS201' : 'OOP'}

len(d) # return number of key-value pairs
max(d) # return maximum key in dictionary d
min(d) # return minimum key in dictionary d
sorted(d) # return sorted list of keys
sum(d) # return sum of all keys if keys are numbers
any(d) # return True if any key of dictionary d is True
all(d) # return True if all keys of dictionary d are True
reversed(d) # can be used for reversing dict/keys/values


courses = { 'CS101' : 'CPP', 'CS102' : 'DS', 'CS201' : 'OOP'}

for k, v in reversed(courses.items( )) :
    print(k, v)