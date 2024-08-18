# ****Immutable****

my_string = "Hello"
Address1 = id(my_string)

print(my_string)
print(Address1)

my_string = my_string + " World!"   # Concatenated 
Address2 = id(my_string)

print(my_string)
print(Address2)

if Address1 == Address2:
    print("Both the Memory Address are Equal")

else:
    print("Both the Memory Address are Different")

# OUTPUT: Both the Memory Address are Different 

# As we know that Strings are Immutable. This means that the String was modified into the different place (object) with different memory adress.







# ****Mutable****

my_list = [10, 20, 30, 40]
Address1 = id(my_list) 

print(my_list)
print(Address1)

my_list.append(50)
Address2 = id(my_list) 

print(my_list)
print(Address2)

if Address1 == Address2:
    print("Both the Memory Address are Equal")

else:
    print("Both the Memory Address are Different")

# OUTPUT: Both the Memory Address are Equal

# As we know that List is mutable. This means that the List was modified in the same place (object) with no memory adress change