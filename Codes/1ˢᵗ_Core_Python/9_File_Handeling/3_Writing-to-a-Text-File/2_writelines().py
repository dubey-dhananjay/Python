f = open(r"C:\Users\dhana\Desktop\File_Handeling\3_Writing-to-a-Text-File\Demo.txt", "w")

lines = ["Hey, this my First Line\n", "Second Line\n", "and this is my Last Line\n"]

f.writelines(lines)

f.close()