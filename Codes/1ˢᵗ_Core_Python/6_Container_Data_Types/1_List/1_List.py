# Container is an entity which contains mutiple data items. It is also known as a collection.

# Python has following container data types:
# Lists     Tuples      Sets     Dictionaries




# A list can grow or shrink during execution of the program. Hence it is also known as a Dynamic Array.

# A list is defined by writing comma-seperated elements within[]. 

# Example:
num = [10, 20, 30, 40, 50]
name = ["Sanjay", "Anil", "Radha", "Suparna"]




# List can contain dissimilar types, though usually they are a collection of similar types.

# Example: 
animal = ["Zebra", 155.5, 110]





# Items in list can be repeated

ages = [25, 26, 25, 27, 26]       # duplicates allowed
num = [10] * 5                    # stores [10, 10, 10, 10, 10]
lst = []                          # empty list, valid




# Accessing List Elements

# Example 1: Entire List can be printed by just using the name of the list

l = ["Hello", 20, True, 78.23]
print(l)







# Example 2: Like strings, individual elements in a list can be accessed using indices.

animal = ["Zebra", 155.5, 110]
ages = [25, 26, 25, 27, 26]

print(animal[1], ages[3])

# OUTPUT: 155.5 27







# Example 3: Like strings, lists can be sliced

animal = ["Zebra", 155.5, 110]
ages = [25, 26, 25, 27, 26]

print(animal[1:3])      # prints [155.5, 110]
print(ages[3:])         # prints [27, 26]