#Looping in Tuples
# If we wish to process each item in a tuple, we should be able to iterate through it. This can be done using a while loop or for loop.






# Example 1: 
# using while loop

tpl = (10, 20, 30, 40, 50)
i = 0

while i < len(tpl):
    print(tpl[i])
    i += 1

# OUTPUT:
# 10
# 20
# 30
# 40
# 50







# Example 2: 
# using for loop

for n in tpl:
    print(n)

# OUTPUT:
# 10
# 20
# 30
# 40
# 50







# Example 3:
# While iterating through a tuple using a for loop, if we wish to keep track of index of the element that is being currently processed, we can do so using the built-in enumerate( ) function.

tpl = (10, 20, 30, 40, 50)

for index, n in enumerate(tpl):
    print(index, n)

# OUTPUT:
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50