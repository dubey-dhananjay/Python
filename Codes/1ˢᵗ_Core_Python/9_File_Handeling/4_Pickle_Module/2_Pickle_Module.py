# Pickling data in Python

import pickle as pk

listvalues = [1, "Arjun", "M", 21]

f = open(r"C:\Users\dhana\Desktop\File_Handeling\4_Pickle_Module\Demo.dat", "wb")

pk.dump(listvalues,f)

f.close()





# Unpickling data in Python

print("The Data that were stored in File are: ")
fo = open(r"C:\Users\dhana\Desktop\File_Handeling\4_Pickle_Module\Demo.dat", "rb")

data = pk.load(fo)

print(data)

fo.close()