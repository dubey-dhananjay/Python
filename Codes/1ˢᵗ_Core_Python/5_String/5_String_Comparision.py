s1 = "Bombay"
s2 = "bombay"
s3 = "Nagpur"
s4 = "Bombaywala"
s5 = "Bombay"

print(s1 == s2)     # prints False
print(s1 == s5)     # prints True
print(s1 != s3)     # prints True
print(s1 > s5)      # prints False
print(s1 < s2)      # prints True
print(s1 <= s4)     # prints True


# String comparision is done in lexicological order (alphabetical) character by character.
# Capitals are considered to be less than their lowercase counterparts.
# Result of comparision operation is either True or False





# Note: If there are two different string variable and their object i.e value are same then they both contain the same address

# Let's see an Example: 

string1 = "INDIA"
index1 = id(string1)
print(index1)

string2 = "INDIA"
index2 = id(string2)
print(index2)

if index1 == index2:
    print("Both the Memory Address are same")

else:
    print("Both the Memory Address are Different")


# OUTPUT:

# 2600608861280
# 2600608861280

# Both the Memory Address are same