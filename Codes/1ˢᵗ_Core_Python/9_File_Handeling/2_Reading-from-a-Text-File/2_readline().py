f = open(r"C:\Users\dhana\Desktop\File_Handeling\Demo.txt", "r")

line1 = f.readline()    # If no argument or a negative number is specified, it reads a complete line and returns string.

print(line1)    

f.close()





f = open(r"C:\Users\dhana\Desktop\File_Handeling\Demo.txt", "r")

line1 = f.readline(5)     # Here as we can see that argument is been passed, Due to which it will be reading only 1st five characters of the First Line 

print(line1)    

f.close()