# Looping in List

# If we wish to process each item in the list, we should be able to iterate through the list. This can done using a while or for loop.



# Example 1: 
animals = ["Zebra", "Tiger", "Lion", "Jackal", "Kangaroo"]

# using while loop
i = 0

while i < len(animals):
    print(animals[i])
    i+=1






# Example 2: 
# using more convenient for loop

for a in animals:
    print(a)

# OUTPUT:

# Zebra
# Tiger
# Lion
# Jackal
# Kangaroo







# Itereating through a list using for loop. If we wish to keep track of index of the elements that a is referring to, we can do so using the built-in enumerate() function.

# Example 3: 

animals = ["Zebra", "Tiger", "Lion", "Jackal", "Kangaroo"]

for index,a in enumerate(animals):
    print(index, a)

# OUTPUT:

# 0 Zebra
# 1 Tiger
# 2 Lion
# 3 Jackal
# 4 Kangaroo







# Taking list elements from the user


# Example 1:
arr = []

for i in range(5):
    element = int(input(f"Eneter the {i+1} Element: "))
    arr.append(element)

print("\n\n\n")

for i in range(5):
    print(f"Element on {i} Index is: {arr[i]}")

# OUTPUT: 

# Eneter the 1 Element: 12
# Eneter the 2 Element: 13
# Eneter the 3 Element: 14
# Eneter the 4 Element: 85
# Eneter the 5 Element: 96




# Element on 0 Index is: 12
# Element on 1 Index is: 13
# Element on 2 Index is: 14
# Element on 3 Index is: 85
# Element on 4 Index is: 96






# Example 2:
size = int(input("Enter the Size of Array: "))

if size>0:
    arr = []

    for i in range(size):
        element = int(input(f"Enter the {i+1} Element: "))
        arr.append(element)

    print("\n\n\n")

    for i in range(size):
        print(f"Element on {i} Index is: {arr[i]}")



# OUTPUT: 

# Enter the Size of Array:  5
# Enter the 1 Element:  1
# Enter the 2 Element:  2
# Enter the 3 Element:  3
# Enter the 4 Element:  4
# Enter the 5 Element:  5




# Element on 0 Index is: 1
# Element on 1 Index is: 2
# Element on 2 Index is: 3
# Element on 3 Index is: 4
# Element on 4 Index is: 5