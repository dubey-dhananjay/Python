# search and replace


# find(): This method is used to find the first occurrence of a substring within a string. It returns the index of the first occurence of the substring, or -1 if the substring is not found.

sentence = "Hello, how are you?"

index = sentence.find("how")

print(index)

# OUTPUT: 7







# replace(): This method is used to replace all occurences of a specified substring within a string with another substring. It returns a new string with the replacement applied.

sentence = "Hello, how are you?"

index1 = id(sentence)
print(index1)

sentence = sentence.replace("how", "where")
index2 = id(sentence)
print(index2)

print(sentence)

# OUTPUT: Hello, where are you?

# In the above example it seems like string is been Mutated, but it is not so memory adress before and after are different. If the String is Immutable. Both the memory address has to be same after mutating.