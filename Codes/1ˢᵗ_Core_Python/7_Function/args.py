# *args : Parameters that will pack all arguments into a Tuple, Useful so that a Function can accept a varying amount of arguments

def add(*args):  # Tuple un-packaging 
    sum = 0
    for i in args:
        sum += i
    return sum

def main():

    print(add(1, 2, 3, 4, 5, 6))

if __name__ == "__main__":
    main()