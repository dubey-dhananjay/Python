def calc_avg(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = sum/3
    return avg

def main():

    print(calc_avg(78, 33, 95))   # prints 68.67

if __name__ == "__main__":
    main()