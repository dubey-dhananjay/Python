# .upper() Converts all characters in a string to uppercase

Text="hello world"

Text=Text.upper()

print(Text)  

# Output: HELLO WORLD





# .lower(): Converts all characters in a string to lowercase.

Text="HELLO WORLD"

Text=Text.lower()

print(Text)  

# Output: hello world





# .capitalize() --> Capitalize user's name (Just the very First Letter)

name="arjun"

name=name.capitalize()

print(f"Hello, {name}")

# OUTPUT:

# Hello, Arjun





# .title() --> Capitalize the 1st Letter of each word

name=input("What's your name? ")

name=name.title()

print(f"Hello, {name}")


# OUTPUT:
# What's your name? dhananjay dubey
# Hello, Dhananjay Dubey





# swapcase(): This method is used to convert the uppercase character in a string to lowercase and vice versa. It returns a new string with the case of each letter swapped.

org_str = "Hello, World!"

new_str = org_str.swapcase()

print(new_str)

# OUTPUT: hELLO, wORLD!