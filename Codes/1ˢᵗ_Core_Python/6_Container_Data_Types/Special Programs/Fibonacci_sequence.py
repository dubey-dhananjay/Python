# Write a program to print the Fibonacci Sequence

# What is Fibonacci Sequence?
# A Fibonacci Sequence is a sequence in which each term can be obtained by adding the previous two terms
# Example: 0, 1, 1, 2, 3


terms = int(input("Enter the number of terms: "))

n1, n2 = 0, 1

if terms<=0:
    print("Please enter a positive integer.")
elif terms == 1:
    print(f"Fibonnaci Sequence: {n1}")
else:
    for term in range(terms):
        print(n1,end=" ")
        n = n1 + n2
        n1 = n2
        n2 = n