# append(): Adds an element to the end of the list

my_list = [1, 2, 3]

my_list.append(4)

print(my_list)

# OUTPUT: [1, 2, 3, 4]







# extend(one value): Extends the list by adding all elements from another iterable (i.e list)

list1 = [1, 2, 3]

list2 = [4, 5]

list1.extend(list2)

print(list1)

# OUTPUT: [1, 2, 3, 4, 5]








# insert(): Inserts an element at a specified position in the list

my_list = [85, 65, 97]

my_list.insert(1, 4) # here 1 is the Index and 4 is the Value to be inserted on the index 1

print(my_list)

# OUTPUT: [85, 4, 65, 97]













# remove(value): Removes the first occurrence of a value from the list

# Example 1: 
my_list = [1, 2, 3]

my_list.remove(2) # here 2 is the Value from list

print(my_list)

# Output: [1, 3]





# Example 2: 
my_list = [1, 2, 3]

my_list.remove(30) # here 30 is value that is not present in the list which is out of range so error is given

print(my_list)

# Output: error










# pop(index): Removes and returns the element at a specified index in the list

# Example 1:
my_list = [1, 2, 3]

popped_element = my_list.pop(1) # here 1 is the index Value

print(popped_element)
print(my_list)


# OUTPUT: 2
#	  [1, 3]



# Example 2:
my_list = [1, 2, 3]

popped_element = my_list.pop() # here index is not mentioned in () so pop() removes last item in list

print(popped_element)
print(my_list)


# OUTPUT: 3
#         [1, 2]







# Example 3:
my_list = [1, 2, 3]

popped_element = my_list.pop(30) # here 30 is index which is out of range so error is given

print(popped_element)
print(my_list)


# OUTPUT: error









# count(value): Returns the number of occurrences of a value in the list

my_list1 = [1, 2, 2, 3, 2]
my_list2 = ["Yash", "Swaraj", "Yash"]

count1 = my_list1.count(2)
count2 = my_list2.count("Yash")

print(count1) # OUTPUT: 3
print(count2) # OUTPUT: 2










# index(value): Returns the index of the first occurrence of a value in the list


# Example 1:
my_list = [1, 2, 3, 4]

print(my_list.index(3)) # here 3 is the Value 

# OUTPUT: 2


# Example 2:
my_list = [1, 2, 3, 4]

print(my_list.index(45)) # here 45 is the Value which is not present in the List 

# OUTPUT: error









# copy(): Creates a shallow copy of the list

original_list = [1, 2, 3]

new_list = original_list.copy()

print(new_list)

# Output: [1, 2, 3]








# clear(): Removes all elements from the list

my_list = [1, 2, 3]

my_list.clear()

print(my_list)

# OUTPUT: []