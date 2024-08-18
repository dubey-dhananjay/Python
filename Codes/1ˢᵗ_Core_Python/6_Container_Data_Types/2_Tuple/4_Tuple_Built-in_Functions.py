# Using Built-in Functions on Tuple



# len(): Returns number of items in the tuple

num = (10, 10, 10, 10, 10, 10, 10)

length = len(num)

print(length)       # prints 7





# max(): Returns maximum element in the tuple


# Example 1:

num = (741, 852, 963, 789, 456, 123, 456)

maximum1 = max(num)

print(maximum1)      # prints 963



# Example 2:

tpl = ("Hello,", 78.13, 53, True, "world!")

maximum2 = max(tpl)

print(maximum2)

# OUTPUT: error (max() does not supports if their is a str in tuple)


# Example 3:

tpl = ("Hello",  "world!")

maximum3 = max(tpl)

print(maximum3)

# OUTPUT: world! 






# min(): Returns minimum element in the tuple


# Example 1:

num = (741, 852, 963, 789, 456, 123, 456)

minimum1 = min(num)

print(minimum1)      # prints 123



# Example 2:

tpl = ("Hello,", 78.13, 53, True, "world!")

minimum2 = min(tpl)

print(minimum2)

# OUTPUT: error (min() does not supports if their is a str in list)



# Example 3:

tpl = ("Hello",  "world!")

minimum3 = min(tpl)

print(minimum3)

# OUTPUT: Hello









# sum(): return sum of all elements in the tuple

# Example 1:
num = (741, 852, 963, 789, 456, 123, 456)

print(sum(num))     # prints 4380


# Example 2:
tpl = (78.13, 53, True)

print(sum(tpl))         # prints 132.13










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

# Example: Check is all elements in the tuple are greater than 0

my_tuple = (1, 3, 4, 5, 6, 7)

print(all(x>0 for x in my_tuple)) 
        # 1>0 for x in my_tuple      # True
        # 3>0 for x in my_tuple      # True
        # 4>0 for x in my_tuple      # True
        # 5>0 for x in my_tuple      # True
        # 6>0 for x in my_tuple      # True
        # 7>0 for x in my_tuple      # True

# As we can see all the conditions are True so the OUTPUT is True, because all() checks that every condition is True










# any(): Function returns True is at least one elements of its parameter are True.

my_tuple = (1, 3, 5, 6, 7)

print(any(x%2 == 0 for x in my_tuple))

# OUTPUT: True (6%2 == 0)









# Aliasing: 

student_info = ("Linda", 18, ["Math", "Physics", "History"])

student_profile = student_info

id(student_info) == id(student_profile)   # True
id(student_info[0]) == id(student_profile[0])   # True
id(student_info[1]) == id(student_profile[1])   # True
id(student_info[2]) == id(student_profile[2])   # True

                        # OR

student_info = ("Linda", 18, ["Math", "Physics", "History"])

student_profile = copy(student_info)

id(student_info) == id(student_profile)    # True
id(student_info[0]) == id(student_profile[0])   # True
id(student_info[1]) == id(student_profile[1])   # True
id(student_info[2]) == id(student_profile[2])   # True


student_profile[2][2] = "Computer science"

student_profile         # ('Linda', 18, ['Math', 'Physics', 'Computer science'])
student_info            # ('Linda', 18, ['Math', 'Physics', 'Computer science'])





# deepcopy()

student_info = ("Linda", 18, ["Math", "Physics", "History"])

student_profile = deepcopy(student_info)

id(student_info) == id(student_profile)    # False
id(student_info[0]) == id(student_profile[0])   # True
id(student_info[1]) == id(student_profile[1])   # True
id(student_info[2]) == id(student_profile[2])   # False


student_profile[2][2] = "Computer science"
print(student_profile)  # ('Linda', 18, ['Math', 'Physics', 'Computer science'])
print(student_info)     # ('Linda', 18, ['Math', 'Physics', 'History'])





# sorted(): Sorts the elements of the tuple and returns a new sorted list, takes original tuple as a parameter

tpl1 = (10, 2, 0, 50, 4)
index1 = id(tpl1)

tpl2 = sorted(tpl1)
index2 = id(tpl2)
print(tpl2)      # prints [0, 2, 4, 10, 50]
print(tuple(tpl2))      # prints (0, 2, 4, 10, 50)

if index1 == index2:
        print("Memory Address is same")
else:
        print("Memory Address is different")


















# reversed(): Returns Reversed tuple in hexadecmal, Another tuple has to be created, and takes original tuple as a parameter

tpl1 = (10, 2, 0, 50, 4)
index1 = id(tpl1)

reversed(tpl1)
index2 = id(tpl1)
print(tuple(reversed(tpl1)))      # prints (4, 50, 0, 2, 10)

if index1 == index2:
        print("Memory Address is same") # True
else:
        print("Memory Address is different")

print(tpl1)       # prints (10, 2, 0, 50, 4)
# Original tuple is unchanged