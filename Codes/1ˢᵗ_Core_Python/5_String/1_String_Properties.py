# Python Strings are Immutable - they cannot be changed


#                       Accessing String Elements

# Positive Indices:         0   1   2   3   4
# String Elements:          H   e   l   l   o
# Negative Indices:        -5  -4  -3  -2  -1


msg = "Hello"

print(msg[0])       # prints H
print(msg[4])       # prints o
print(msg[-0])      # prints H, -0 is same as 0
print(msg[-1])      # prints o
print(msg[-2])      # prints l
print(msg[-5])      # prints H
print(msg[-6])      # IndexError: string index out of range





# A sub-string can be sliced out of a string

# s[start : end] - extract from start to end-1
print(msg[0:5])

# s[start :] - extract from start to end
print(msg[1:])

# s[: end] - extract from start to end-1
print(msg[0:100])

# s[-start :] - extract from -start(included) to end
print(msg[-5:])

# s[: -end] - extract from beginning to -end-1
print(msg[:-2])





#                   String Properties

# As we know Python Strings are Immutable - they cannot be changed

message="Hello"
message[0]="M"      # rejected attempt to mutate(change) string

message="Hii.."
print(message)      # msg is a variable it can change





# Strings can be concatenated by using +

name="Arjun"
sur_name="Diwedi"

print(name + sur_name)





# Strings can be replecated during printing

print("-" * 50)     # prints --------------------------------------------------





# Whether one string is part of another can be found out using (in)

print("e" in "Hello")   # prints True
print("z" in "Hello")   # prints False
print("lo" in "Hello")  # prints True