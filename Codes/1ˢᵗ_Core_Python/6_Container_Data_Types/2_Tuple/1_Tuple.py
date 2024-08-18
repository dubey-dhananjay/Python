# List: Though a list can store dissimilar data, it is commonly used for storing similar data.

# Tuple: Though a tuple can store similar data it is commonly used for storing dissimilar data. 

# Tuple in Python offer several advantages and unique functionalities that distinguish them from other data structures like lists.



# 1. Immutable: Tuples are immutable, meaning their elements cannot be modified or reassigned after creation. This immutability ensures data integrity and prevents accidental changes to critical information.

# 2. Performance: Tuples are generally faster than lists because of their immutable nature. Operations like indexing and iteration on tuples are more efficient compared to lists, espacially for large datasets.

# 3. Memory Efficient: Tuples consume less memory compared to lists, making them suitable choice when you need to store a fixed set of values that won't change.

# 4. Unpacking: Tuples support unpacking, allowing you to assign multiple variables in a single statement. This feature is handy for functions that return multiple values. 


# Ordered: They contain elements that are sequentially arranged according to their specific insertion order.

# Lightweight: They consume relatively small amounts of memory compared to other sequences like lists.

# Indexable through a zero-based index: They allow you to access their elements by integer indices that start from zero.

# Immutable: They don’t support in-place mutations or changes to their contained elements. They don’t support growing or shrinking operations.

# Heterogeneous: They can store objects of different data types and domains, including mutable objects.

# Nestable: They can contain other tuples, so you can have tuples of tuples.

# Iterable: They support iteration, so you can traverse them using a loop or comprehension while you perform operations with each of their elements.

# Sliceable: They support slicing operations, meaning that you can extract a series of elements from a tuple.

# Combinable: They support concatenation operations, so you can combine two or more tuples using the concatenation operators, which creates a new tuple.

# Hashable: They can work as keys in dictionaries when all the




# The tuple data is enclosed within () as shown below. 


a = ()      # empty list
b = (10,)   # tuple with one item. ',' after 10 is neccesary
c = ("Sanjay", 25, 34555.50)    # tuple with dissimilar items
d = (10, 20, 30, 40)    #tuple with similar items


# While initializing a tuple, we may drop '()'

c = "Sanjay", 25, True, 45.23
print(type(c))      # prints <class 'tuple'>



# Tuple items repeatation

tpl1 = (10,) * 5  # stores (10, 10, 10, 10, 10) 

tpl2 = (10) * 5   # Basically it is not a tuple. Beacuse tuple with one item. ',' after 10 is neccesary
print(tpl2)       # stores 50
print(type(tpl2)) # <class 'int'>







# Accessing Tuple Elements

# Example 1: Entire Tuple can be printed by just using the name of the tuple

tpl = ('Sanjay', 25, 34555.50)
print(tpl)      # prints ('Sanjay', 25, 34555.5)





# Example 2: Like strings and list, individual elements in a tuple can be accessed using indices starting with 0.

# Tuple is an ordered collection. So order of insertion of elements in a tuple is same as the order of access.


msg = ('Handle', 'Exceptions', 'Like', 'a', 'boss')
print(msg[1], msg[3])

# OUTPUT: Exceptions a





# Example 3: Like strings and list, tuples can be sliced to yield smaller tuples.

# tuple_object[start:stop:step]
# start : The index where the slice begins.
# stop : The index where the slice ends (exclusive) means -1.
# step : The step or stride between elements.


animal = ("Zebra", 155.5, 110)
ages = (25, 26, 25, 27, 26)

print(animal[1:3])      # prints [155.5, 110]
print(ages[3:])         # prints [27, 26]




my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Slicing from index 2 to index 7 (exclusive) with a step of 2
sliced_tuple = my_tuple[2:7:2]

print(sliced_tuple) # prints (3, 5, 7)