# Chapter 4 Exercise 12 Calculating the Factorial of a Number

# This program allows the user to enter a non-negative integer then uses a loop
# to calculate the factorial of that number. Display the factorial.

# Input
# Process
# Output

def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)
num = int(input("Enter a Number: "))
# if input number is negative then return an error message
# elif the input number is 0 then display 1 as output
# else calculate the factorial by calling the user defined function
if num < 0:
    print("Factorial cannot be found for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is: ", factorial(num))