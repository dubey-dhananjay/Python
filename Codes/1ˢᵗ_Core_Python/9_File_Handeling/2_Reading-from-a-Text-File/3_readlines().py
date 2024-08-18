# The method reads all the lines and returns the lines along with newline as a list of strings. 
# The following example uses readlines() to read data from the text file Demo.txt.


f = open(r"C:\Users\dhana\Desktop\File_Handeling\Demo.txt", "r")

Data = f.readlines()     

print(Data)

# OUTPUT:
# ['Hello, World!\n', 'Today is a wounderful day.....\n', '1\n', '2\n', '3\n', '4\n', '5\n']



for line in Data:
    words = line.split()
    print(words)

# OUTPUT:
# ['Hello,', 'World!']
# ['Today', 'is', 'a', 'wounderful', 'day.....']
# ['1']
# ['2']
# ['3']
# ['4']
# ['5']






for line in Data:
    words = line.splitlines()
    print(words)

# OUTPUT:



f.close()



