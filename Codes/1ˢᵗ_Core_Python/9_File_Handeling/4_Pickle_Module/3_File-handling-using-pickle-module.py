# To perform basic operations on a binary file using pickle module

import pickle as pk 

print("------WORKING WITH BINARY FILES------")

bfile = open(r"C:\Users\dhana\Desktop\File_Handeling\4_Pickle_Module\Demo1.docx","ab")

recno = 1

print("Enter Records of Employees: ")
print()

while True:
    print("RECORD No. ",recno)

    eno = int(input("\tEmployee Number: "))
    ename = input("\tEmployee Name: ")

    ebasic = int(input("\tBasic Salary: "))
    allow = int(input("\tAllowances: "))

    totsal = ebasic + allow
    print("\tTOTAL SALARY: ",totsal)
    
    edata = [eno,ename,ebasic,allow,totsal]

    pk.dump(edata, bfile)

    ans = input("Do you wish to enter more records (y/n)? ")

    recno = recno + 1

    if ans.lower() == 'n':
        print("Record entry OVER")
        print()
        break
bfile.close()

readrec = 1

try: 
    with open (r"C:\Users\dhana\Desktop\File_Handeling\4_Pickle_Module\Demo1.docx","rb") as bfile:
        while True:
            edata = pk.load(bfile)
            print("Record Number: ",readrec)
            print(edata)
            readrec = readrec+1

except EOFError:
    pass

bfile.close()