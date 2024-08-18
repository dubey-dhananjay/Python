# Mutability - Unlike a list, a tuple is immutable, i.e. it cannot be modified.

msg = ("Fall", "In", "Line")

msg[0] = "FALL"     # error
msg[1:3] = ("Above", "Mark")    # error


# Since a tuple is immutable operations like .append(), .extend(), .insert(), .remove(), and .clear() don't have these methods.

# Additionally, tuples don’t support the del statement on items.

point = (7, 14, 21)

del point[2]    # error


# Though a tuple itself is immutable, it can contain mutable objects like lists.

# mutable lists, immutable string—all can belong to tuple

s = ([1, 2, 3, 4], [4, 5], 'Ocelot')

# If a tuple contains a list, the list can be modified since list is a mutable object. 

s = ([1, 2, 3, 4], [10, 20], "Onida")

s[1][1] = 45   # changes first item of list at index 1, i.e 20

print(s)    ([1, 2, 3, 4], [10, 45], 'Onida')

# one more way to change first item of first list

p = s[1]    # s[1] is [10, 20] so now p is another name of the list situated at s[1]

print(p)

p[1] = 100

print(s) # here due to aliasing list is mutable so list in tuple s is also modified

# OUTPUT: ([1, 2, 3, 4], [10, 100], 'Onida')







# Concatenation: One tuple can be concatenated at the end of another as shown below: 
# In this after concatenating another tuple object has been created

tpl = (3, 4, 5, 6)
print(id(tpl))      # prints 3183380673328

tpl += (1, 2, 3)

print(tpl)      # prints (3, 4, 5, 6, 1, 2, 3)
print(id(tpl))      # prints 3183375938848

# Since tuple is immutable after concatenating another tuple object has been created and another memory address is assigned






# Merging: Two tuple can be merged to create a new list

a = (10, 20, 30)
b = (100, 200, 300)

c = a + b

print(c)        # prints (10, 20, 30, 100, 200, 300)






# Conversion: A string/list/set can be converted into a tuple using the tuple() conversion function. 

# string:
l = tuple("Africa")

print(l)       # prints ('A', 'f', 'r', 'i', 'c', 'a')





# list:
l = [10, "Hello", True, 23.12]
t = tuple(l)

print(t)        # prints (10, 'Hello', True, 23.12)




# set

s = {45, "Apple", True, 23.12}

t = tuple(s)

print(t)        # prints (True, 'Apple', 45, 23.12)







# dict

d = {

    "Age": 10,
    "Name": "Arjun",
    "isAdult": True,
    "Per": 78.23
}

t = tuple(d)

print(t)    # prints ('Age', 'Name', 'isAdult', 'Per')












# Identity: Whether the two variables are referring to the same tuple can be checked using the is identity operator as shown below. 

tpl1 = (10, 20, 30, 40, 50)
tpl2 = (10, 20, 30, 40, 50)

tpl3 = tpl1

print(tpl1 is tpl2)         # prints False
print(tpl1 is tpl3)         # prints True
print(tpl1 is not tpl2)     # prints True


# Identity Difference between int and str

num1 = 10 ; s1 ="Hii"
num2 = 10 ; s2 ="Hii"
num3 = num1 ; s3 = s1

print(num1 is num2)     # prints True
print(s1 is s2)         # prints True






# Searching: An element can be searched in a tuple using the in membership operator as shown below. 

tpl = ('a', 'e', 'i', 'o', 'u')

print('a' in tpl)       # prints True since 'a' is present in tuple
print('b' in tpl)       # prints False since 'b' is absent in tuple
print('z' not in tpl)   # prints True since 'z' is absent in tuple









# Comparison: It is possible to compare contents of two tuples.
# Comparsion is done item by item till there is a mismatch. 
 
tpl1 = (1, 2, 3, 4, 5)
tpl2 = (1, 2, 5)

print(tpl1 < tpl2)     # prints True








# Emptiness: We can check is a tuple is empty using not operator

tpl = ()

if not tpl:
    print("Empty tuple")

else:
    print("Not an Empty tuple")


# OUTPUT: Empty tuple