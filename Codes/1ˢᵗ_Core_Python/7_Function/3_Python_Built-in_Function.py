# abs():

num = -7
print(f"The absolute value of {num} is {abs(num)}")

# The abs() function returns the absolute value of a number. 
# It removes the sign (positive or negative) from a number.





# pow():

base = 2
exp = 3
print(f"{base} raised to the power {exp} is {pow(base, exp)}")

# The pow() function raises the first argument to the power of the second argument. 
# If a third argument is provided, it calculates the result modulo that value.





# min():

print(f"The minimum of 4, 7, and 2 is {min(4, 7, 2)}")

# The min() function returns the smallest item from a collection of items.





# max():

print(f"The maximum of 9, 3, and 6 is {max(9, 3, 6)}")

# The max() function returns the largest item from a collection of items.





# divmod():

quotient, remainder = divmod(10, 3)
print(f"10 divided by 3 gives a quotient of {quotient} and a remainder of {remainder}")

# The divmod() function returns a tuple containing the quotient and remainder of dividing two numbers.
# If you are storing value of the Function into 1 variable it will be stored in Tuple




# round():

num = 3.14159
print(f"Rounded value of {num} with 2 decimal places is {round(num, 2)}")   # prints 3.14

# The round() function rounds a number to a specified number of decimal places.





# bin():

num = 10
print(f"The binary representation of {num} is {bin(num)}")

# The bin() function converts an integer to a binary string prefixed with '0b'.





# oct():

num = 10
print(f"The octal representation of {num} is {oct(num)}")

# The oct() function converts an integer to an octal string prefixed with '0o'.





# hex():

num = 16
print(f"The hexadecimal representation of {num} is {hex(num)}")

# The hex() function converts an integer to a hexadecimal string prefixed with '0x'.