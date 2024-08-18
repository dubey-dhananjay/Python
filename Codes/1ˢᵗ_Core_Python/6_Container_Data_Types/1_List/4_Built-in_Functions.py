# Using Built-in Functions on List



# len(): Returns number of items in the list

num = [10, 10, 10, 10, 10, 10, 10]

length = len(num)

print(length)       # prints 7





# max(): Returns maximum element in the list


# Example 1:

num = [741, 852, 963, 789, 456, 123, 456]

maximum1 = max(num)

print(maximum1)      # prints 963



# Example 2:

lst = ["Hello,", 78.13, 53, True, "world!"]

maximum2 = max(lst)

print(maximum2)

# OUTPUT: error (max() does not supports if their is a str in list)


# Example 3:

lst = ["Hello",  "world!"]

maximum3 = max(lst)

print(maximum3)

# OUTPUT: world! 






# min(): Returns minimum element in the list


# Example 1:

num = [741, 852, 963, 789, 456, 123, 456]

minimum1 = min(num)

print(minimum1)      # prints 123



# Example 2:

lst = ["Hello,", 78.13, 53, True, "world!"]

minimum2 = min(lst)

print(minimum2)

# OUTPUT: error (min() does not supports if their is a str in list)



# Example 3:

lst = ["Hello",  "world!"]

minimum3 = min(lst)

print(minimum3)

# OUTPUT: Hello









# sum(): return sum of all elements in the list

# Example 1:
num = num = [741, 852, 963, 789, 456, 123, 456]

print(sum(num))     # prints 4380


# Example 2:
lst = [78.13, 53, True]

print(sum(lst))         # prints 132.13










# Instead of using the 'and' and 'or' logical operator, we can use the built in functions all() and any() to get the same effect. 

a, b, c = 10, 20, 30

# t = (a>5, b>20, c>15)
# print(t)          # prints (True, False, True)

result1 = all((a>5, b>20, c>15))
print(result1)          # False, as second condition is False
print(type(result1))    # prints <class 'bool'>


result2 = any((a>5, b>20, c>15))
print(result2)           # True, as one of the condition is True
print(type(result2))     # prints <class 'bool'>




# all(): Function returns True if all elements of its parameter are True. 

# Example: Check is all elements in the list are greater than 0

my_list = [1, 3, 4, 5, 6, 7]

print(all(x>0 for x in my_list)) 
        # 1>0 for x in my_list      # True
        # 3>0 for x in my_list      # True
        # 4>0 for x in my_list      # True
        # 5>0 for x in my_list      # True
        # 6>0 for x in my_list      # True
        # 7>0 for x in my_list      # True

# As we can see all the conditions are True so the OUTPUT is True, because all() checks that every condition is True










# any(): Function returns True is at least one elements of its parameter are True.

my_list = [1, 3, 5, 6, 7]

print(any(x%2 == 0 for x in my_list))

# OUTPUT: True (6%2 == 0)









# del(): deletes element or slice or entire list

lst = [10, 20, 30, 40, 50]

del(lst[3])     
print(lst)      # prints [10, 20, 30, 50]

del(lst[2:5])
print(lst)      # prints [10, 20]

del(lst[:])     # delete entire list
print(lst)      

lst = []        # another way to delete an entire list





lst1 = [10, 20, 30, 40, 50]

lst3 = lst2 = lst1      # all refer to same list

print(lst1)
print(lst2)
print(lst3)

lst1 = []       # lst1 refers to empty list with new memory address; lst2, lst3 to original list

print(lst2)     # prints [10, 20, 30, 40, 50]
print(lst3)     # prints [10, 20, 30, 40, 50]


lst2 = []

print(lst2)     # prints []
print(lst3)     # prints []


# clear(): Removes all elements from the list

my_list = [1, 2, 3]
print(id(my_list))

my_list.clear()

print(my_list)
print(id(my_list))

# OUTPUT: []








# sort(): Returns sorted list, list remains unchanged

lst = [10, 2, 0, 50, 4]
index1 = id(lst)

lst.sort()
index2 = id(lst)
print(lst)      # prints [0, 2, 4, 10, 50]


if index1 == index2:
        print("Memory Address is same")
else:
        print("Memory Address is different")






# sorted(): Returns sorted list, Another list has to be created, and takes original list as a parameter

lst1 = [10, 2, 0, 50, 4]
index1 = id(lst1)

lst2 = sorted(lst1)
index2 = id(lst2)
print(lst2)      # prints [0, 2, 4, 10, 50]


if index1 == index2:
        print("Memory Address is same")
else:
        print("Memory Address is different")









# reverse(): Returns Reversed list, list remains unchanged

lst = [10, 2, 0, 50, 4]

lst.reverse()
print(lst)      # prints [4, 50, 0, 2, 10]








# reversed(): Returns Reversed list, Another list has to be created, and takes original list as a parameter

lst1 = [10, 2, 0, 50, 4]
index1 = id(lst1)

lst2 = reversed(lst1)
index2 = id(lst2)
print(lst2)      # prints [0, 2, 4, 10, 50]


if index1 == index2:
        print("Memory Address is same")
else:
        print("Memory Address is different")