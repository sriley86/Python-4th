# Chapter 4 Exercise 14 Write a Program that Uses Nested Loops to Draw This Pattern

# This program uses nested loops to draw a pattern

# Process and Output
BASE_SIZE = 8
for row in range(BASE_SIZE):
    for col in range(BASE_SIZE - row):
        print('*', end ='')
    print()
