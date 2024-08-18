# Basic List Operations


# Mutability: Unlike strings, lists are mutable (changeable). So lists can be updated as shown below:

animals = ["Zebra", "Tiger", "Lion", "Jackal", "Kangaroo"]
ages = [25, 26, 25, 27, 26, 28, 25]

animals[2] = "Rhinoceros"

ages[5] = 31

ages[2:5] = [24, 25, 32]    # sets items 2 to 5 with values 24, 25, 32
ages[2:5] = []              # delete items 2 to 4







# Concatenation: One list can be concatenated(appended) at the end of another as shown below: 

lst = [3, 4, 5, 6]
lst = lst + [1, 2, 3]

print(lst)      # prints [3, 4, 5, 6, 1, 2, 3]







# Merging: Two lists can be merged to create a new list

a = [10, 20, 30]
b = [100, 200, 300]

c = a + b

print(c)        # prints [10, 20, 30, 100, 200, 300]






# Conversion: A string/tuple/set can be converted into a list using the list() conversion function. 

# string:
l = list("Africa")

print(l)       # prints ['A', 'f', 'r', 'i', 'c', 'a']





# tuple:
t = (10, "Hello", True, 23.12)
l = list(t)

print(l)        # prints [10, 'Hello', True, 23.12]




# set

s = {45, "Apple", True, 23.12}

l = list(s)

print(l)        # prints [True, 23.12, 45, 'Apple']







# dict

d = {

    "Age": 10,
    "Name": "Arjun",
    "isAdult": True,
    "Per": 78.23
}

l = list(d)

print(l)    # prints ['Age', 'Name', 'isAdult', 'Per']















# Aliasing: On assigning one list to another, both refer to the same list. Changing one changes the other. This assinment is often known as shallow copy or aliasing.

lst1 = [10, 20, 30, 40, 50]

lst2 = lst1     # doesn't copy the content of lst1 to lst2, lst2 referes or represent the lst1(we can say that it's an another name for the lst1, we can see below both the lists i.e lst1 and lst2 are having same memory address)

index1 = id(lst1)
index2 = id(lst2)

if index1 == index2:
    print("Both the List have same Memory Address")

else:
    print("Both the List have different Memory Address")


# OUTPUT: 
# Both the List have same Memory Address       

print(lst1)     # prints [10, 20, 30, 40, 50]
print(lst2)     # prints [10, 20, 30, 40, 50]

lst1[0] = 100

print(lst1)     # prints [100, 20, 30, 40, 50]
print(lst2)     # prints [100, 20, 30, 40, 50]










# Cloning: This involves coping contents of one list into another. After copying both refer to different lists, though both contain same values. Changing one list, doesn't change another.

lst1 = [10, 20, 30, 40, 50]
lst2 = []

lst2 = lst2 + lst1

index1 = id(lst1)
index2 = id(lst2)

if index1 == index2:
    print("Both the List have same Memory Address")

else:
    print("Both the List have different Memory Address")


# OUTPUT: 
# Both the List have different Memory Address

print(lst1)     # prints [10, 20, 30, 40, 50]
print(lst2)     # prints [10, 20, 30, 40, 50]

lst1[0] = 100

print(lst1)     # prints [100, 20, 30, 40, 50]
print(lst2)     # prints [10, 20, 30, 40, 50]



# There is an alternative we can use copy()
# copy(): Creates a shallow copy of the list

original_list = [1, 2, 3]

new_list = original_list.copy()

print(new_list)

# Output: [1, 2, 3]









# Identity: Whether the two variables are referring to the same list can be checked using the is identity operator as shown below. 

lst1 = [10, 20, 30, 40, 50]
lst2 = [10, 20, 30, 40, 50]

lst3 = lst1 

print(lst1 is lst2)         # prints False
print(lst1 is lst3)         # prints True
print(lst1 is not lst2)     # prints True


# Identity Difference between int and str

num1 = 10 ; s1 ="Hii"
num2 = 10 ; s2 ="Hii"


print(num1 is num2)     # prints True
print(s1 is s2)         # prints True






# Searching: An element can be searched in a list using the in membership operator as shown below. 

lst = ['a', 'e', 'i', 'o', 'u']

print('a' in lst)       # prints True since 'a' is present in list
print('b' in lst)       # prints False since 'b' is absent in list
print('z' not in lst)   # prints True since 'z' is absent in list









# Comparison: It is possible to compare contents of two lists.
# Comparsion is done item by item till there is a mismatch. 
 
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 5]

print(lst1 < lst2)     # prints True








# Emptiness: We can check is a list is empty using not operator

lst = []

if not lst:
    print("Empty List")

else:
    print("Not an Empty List")


# OUTPUT: Empty List