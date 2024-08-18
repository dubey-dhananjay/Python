def main():
    file_path = r"C:\Users\dhana\Desktop\File_Handeling\3_Writing-to-a-Text-File\Demo.txt"

    try :
        with open(file_path, "w") as fp:    # Overwrites the Data onto the file
            print("\t------File Created Successfully------\t")
            Data = input("Enter a Number: ")

            fp.write(Data)
            print("\t------Data Written into the File Successfully!------\t")
    except IOError:
        print("\t------Unable to create a File------\t")

if __name__ == "__main__":
    main()