# Chapter 3 Exercise 16 February Days

# This program Asks the User to Enter a Year, Display the Number of Days
# in February of that Year.

# Input

year = int(input('Enter a year: '))

# Process and Output

# Is the Year Divisible by 100 and 400
# (year % 100) == 0 and
if (year % 400) == 0:
    print(' In February', year, 'has 29 days.')
elif (year % 100) != 0 and (year % 4) == 0:
    print('In February', year, 'has 29 days.')
else:
    print('In February', year, 'has 28 days.')