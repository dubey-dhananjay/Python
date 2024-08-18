print(type("Hii"))  # prints <class 'str'>
# string is an immutable collection of Unicose character enclosed
# within 'Mumbai' , "Mumbai" , """Mumbai"""




print(type(35))     # prints <class 'int'>
# int can be expressed in Decimal, Binary, Octal, Hexadecimal
# Binary starts with 0b/0B
# Octal with 0o/0O
# Hexadecimal with 0x/0X






print(type(3.14))   # prints <class 'float'>





print(type(3+2j))   # prints <class 'complex'>
# complex contains real and imaginary parts




print(type(True))   # prints <class 'bool'>
# bool can take any of the two Boolean values both strting in caps True, False
 




print(type(b'\xa1\xe4\x56'))   # prints <class 'bytes'>
# represents 3 bytes with hex values a1e456





# Simple Variable and Assigning them the Values
name="Sanjay"
age=20
per=78.23





# Multiple Variable and Assigning them the Values
name="Sanjay" ; age=20 ; per=78.23 # use ; as statement seperator
                # OR
name, age, per = "Sanjay", 20, 78.23

a=b=c=d = 5





# Multi-lining
# If Statements are long they can be written as multi-lines with each lines with each line except the last ending with \

# Example:
total = physics + chemistry + maths +\
    english + Marathi + history +\
    geography + civics

# Multi-line statements within [], {}, or () don't need \

# Example: 
days = ["Monday","Tuesday","Wednesday","Thursday",
        "Friday","Staurday","Sunday"]





print(4 + 3.3)  # Operation between int and float will return float
print(3 + 3+2j) # Operation between int and complex will return complex
print(7.5 + 45j+23) # Operation between float and complex will return complex

# But if we want in int, str, chr etc.. It can be Done
print(int(4+3.3))
print(type(str(4+3.3)))     # prints <class 'str'>
print(chr(65))    # prints A (yeilds character corresponding to int)





# When multiple operators are used in an arithmatic expression, it is evaluated on the basis of precedence(priority) of the operation used.

# Operation in dec order of their priority (PEDMAS)

# ()              # Parentheses
# **              # Exponentiation, Division
# *, /, //, %     # Multiplication, Division
# +, -            # Addition, Subtraction