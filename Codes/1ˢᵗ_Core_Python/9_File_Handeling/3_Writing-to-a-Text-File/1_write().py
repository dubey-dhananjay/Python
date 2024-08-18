f = open(r"C:\Users\dhana\Desktop\File_Handeling\3_Writing-to-a-Text-File\Demo.txt", "w")

f.write("Hey, I have started learning Python\n")

f.close()



f = open(r"C:\Users\dhana\Desktop\File_Handeling\3_Writing-to-a-Text-File\Demo.txt", "w")

mark1 = input("Enter your Science Marks: ")

# f.write(int(mark))   # ERROR
f.write(str(mark1))   # Only String
f.flush()

mark2 = input("Enter your Maths Marks: ")
f.write(mark2)
f.flush()

f.close()




# The write() actually writes data onto a buffer. When the close() method is executed, the contents from this buffer are moved to the file located on the permanent storage.

# We can also use the flush() method to clear the buffer and write contents in buffer to the file. This is how programmers can forcefully write to the file as and when required.