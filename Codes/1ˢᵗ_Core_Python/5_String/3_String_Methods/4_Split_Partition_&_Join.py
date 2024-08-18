# split(): This method is used to split a string into a list of substrings based on a specified delimiter.


# Example 1:

sentence = "Hello, how are you?"

words = sentence.split(" ")     # Here (" ") is a specified delimiter

print(words)
print(type(words))

# OUTPUT: 

# ['Hello,', 'how', 'are', 'you?'] 
# <class 'list'>

# Output is generated into the List and 'Hello,' 'how' 'are' 'you?' are the substring





# Example 2: 

Text="apple,banana,orange"

Fruits=Text.split(",")      # Here (",") is a specified delimiter

print(Fruits)
print(type(Fruits))

# Output: ['apple', 'banana', 'orange']
# <class 'list'>





# Example 3: 

Text="apple,banana,orange"  #Normal String

ffruits,sfruits,tfruits= Text.split(",")

print(ffruits,sfruits,tfruits)

print(type(ffruits))
print(type(sfruits))
print(type(tfruits))


# OUTPUT: apple banana orange






# Example 4: 

name="Arjun Diwedi"

first, last = name.split(" ")

print(f"Hello, {first}")            
print(f"{last} is your Surname")    

# OUTPUT: 

# Hello, Arjun
# Diwedi is your Surname

# Note: You have to Enter only 2 Words with Spaces, no single word











# partition(): This method splits a string into three parts based on the first occurrence of a specified seperator

# Example 1:

sentence = "Hello, how are you?"

parts = sentence.partition("how")

print(parts)

# OUTPUT: 

# ('Hello, ', 'how', ' are you?')





# Example 2: Seperator not Found

sentence = "Hello, how are you?"

parts = sentence.partition("Python")

print(parts)

# OUTPUT: 

# ('Hello, how are you?', '', '')
# If the seperator is not found, the original string is returned along with two empty strings.





# Example 3: Using Empty String as Seperator

sentence = "Hello, how are you?"

parts = sentence.partition("")

print(parts)

# OUTPUT: 

# ('Hello, how are you?', '', '')





# Example 4: Multiple Occurences of Seperator

sentence = "apple, bananna, cherry, apple"

parts = sentence.partition("apple")

print(parts)

# OUTPUT: 

# ('', 'apple', ', bananna, cherry, apple')





# Example 5: Seperator at the Beginning

sentence = "Hello, how are you?"

parts = sentence.partition("Hello,")

print(parts)

# OUTPUT: 

# ('', 'Hello,', ' how are you?')





# Example 6: Seperator at the End

sentence = "Hello, how are you?"

parts = sentence.partition("you?")

print(parts)

# OUTPUT: 

# ('Hello, how are ', 'you?', '')









# join(): This method is used to concatenate elements of an iterable (e.g. list) into a single string using a specified del

# Example 1: 

words = ['Hello,', 'how', 'are', 'you?']

sentence = " ".join(words)

print(sentence)

# OUTPUT: Hello, how are you?





# Example 2: 

msg = "Hello"

print("-".join(msg))

# OUTPUT: H-e-l-l-o