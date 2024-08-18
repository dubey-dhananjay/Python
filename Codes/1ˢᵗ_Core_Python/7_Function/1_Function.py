# Functions in Python
# Block of statements that perform a specific task.

# Types of Function:
# 1. Built-in Function
#    Ex. print(), len(), type(), range()

# 2. User defined Function

# Syntax:
# def FUNC_NAME(PARAMETER_1, PARAMETER_2):
#   #SOME WORK          # Function Defination
#   return VAL          # Function Defination

# FUNC_NAME(ARGUMENT_1, ARGUMENT_2)    # Function Call






# Example:

# Func Defination 
def cal_sum(num1 ,num2): # Parameters in Paranthesis
    sum = num1 + num2  # Function Definition
    return sum

def main():  # Main Function

# Function Call # Arguments
    print(cal_sum(5, 10)) # prints 15
    print(cal_sum(8, 19)) # prints 27

if __name__ == "__main__":
    main()