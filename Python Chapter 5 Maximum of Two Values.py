# Chapter 4 Exercise 12 Maximum of Two Values

# Write a function named max that accepts two integer values as arguments
#  and returns the value that is the greater of the two. Use the function in a
#  program that prompts the user to enter two integer values. The program should
#  display the value that is the greater of the two.

# Input
a = int(input('Enter a integer: '))
b = int(input('Enter another integer: '))

# Process and Output
def max(a, b):
    if a > b:
        print(a, 'is bigger than', b)
    else:
        print(b, 'is bigger than', a)
max(a, b)