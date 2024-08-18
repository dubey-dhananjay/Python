f = open("Demo.txt", "r")

Data = f.read()   # If no argument or a negative number is specified in read(), the entire file content is read.

print(Data)

print(type(Data))

f.close()





# If we want to read a Specific Amount of Data from a File

f = open("Demo.txt", "r")

Data = f.read(5)

print(Data)

print(type(Data))

f.close()