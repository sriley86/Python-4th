# Python Chapter 5 Exercise 17 Prime Numbers

# A prime number is a number that is only evenly divisible by itself and 1.
# For example the number 5 is prime because it can only be evenly divided by 1 and 5.
# The number 6, however, is not prime because it can be divided evenly by 1, 2, 3, and 6.
# Write a Boolean function named is_prime which takes an integer as an argument and
# returns true if the argument is a prime number, or false otherwise.
# Use the function in a program that prompts the user to enter a number and then
# displays a message indicating whether the number is prime.
# Python Chapter 5 Exercise 18 Prime Number List
# Write another program that displays all of the prime numbers from 1 to 100.
# The program should have a loop that calls the is_prime function.

def isPrime( userNumber ):
    evenDivisions = 0
    if userNumber <= 1:
        return False
    for currentNumber in range( 1, userNumber + 1 ):
        if userNumber % currentNumber == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True

# This section is the input and display for Exercise 17 Prime Numbers
#
#def main():
#    userNumber = int( input( "Please enter a number: ") )
#    if isPrime( userNumber ):
#        print ( userNumber, "is a prime number" ) #if return True
#    else:
#        print ( userNumber, "is NOT a prime number" ) #if return False

# This section is the display for Exercise 18 Prime Number List

def main():
    for currentNumber in range( 1, 101 ):
        if isPrime( currentNumber ):
            print( currentNumber, end=" " )

main()
