# Content test Function

# isalpha(): Returns True if all characters int the string are alphabetic i.e (a-z, A-Z), and the string is not empty

str1 = "Hello"
str2 = "Hello123"

print(str1.isalpha())   # OUTPUT: True
print(str2.isalpha())   # OUTPUT: False





# isdigit(): Returns True if all characters int the string are digits i.e (0-9), and the string is not empty

str1 = "123"
str2 = "123abc"

print(str1.isdigit())   # OUTPUT: True
print(str2.isdigit())   # OUTPUT: False





# isalnum(): Returns True if all characters int the string are alphanumeric i.e (a-z, A-Z, 0-9), and the string is not empty

str1 = "Hello123"
str2 = "Hello@123"

print(str1.isalnum())   # OUTPUT: True
print(str2.isalnum())   # OUTPUT: False  (Special Character and Spaces are not allowed)

age = "20"
name = "Spiderman"

print(age.isalnum())    # OUTPUT: True
# Explaination: The string consists of only numeric character digits and no alphabetic character. isalnum() method checks for alphanumeric characters (a-z, A-Z, 0-9) in string. If the string contains only numeric charcters or a combination of both alphabet and numeric digits, it will return True. Because numeric character digits comes under (a-z, A-Z, 0-9).

print(name.isalnum())   # OUTPUT: True
# Explaination: The string consists of only alphabetic character and no numeric character digits. isalnum() method checks for alphanumeric characters (a-z, A-Z, 0-9) in string. If the string contains only alphabetic charcters or a combination of both alphabet and numeric digits, it will return True. Because alphabetic character comes under (a-z, A-Z, 0-9).

# Note: The Method returns False only if the string is empty or contains non-alphanumeris characters. such as !, @, #, $, %, ^, &, *, (), 





# isupper(): Returns True if all alphabetic characters in the string are uppercase and there is at least one character

str1 = "HELLO"
str2 = "Hello"

print(str1.isupper())   # OUTPUT: True
print(str2.isupper())   # OUTPUT: False





# islower(): Returns True if all alphabetic characters in the string are lowercase and there is at least one character

str1 = "hello"
str2 = "Hello"

print(str1.islower())   # OUTPUT: True
print(str2.islower())   # OUTPUT: False





# startswith(): Retrurns True if the string starts with the specified prefix.

my_string = "Hello, World!"

print(my_string.startswith("Hello"))    # OUTPUT: True
print(my_string.startswith("World"))    # OUTPUT: False





# endswith(): Retrurns True if the string ends with the specified suffix

my_string = "Hello, World!"

print(my_string.endswith("World!"))    # OUTPUT: True
print(my_string.endswith("Hello"))     # OUTPUT: False