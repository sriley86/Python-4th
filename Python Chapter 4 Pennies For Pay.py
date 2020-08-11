# Chapter 4 Exercise 7 Pennies for Pay

# This program calculates the amount of money a person would earn over a period
# of time if the salary is one penny the first day, two pennies the second day
# and continues to double each day. Ask user for the number of days, then display
# a table showing what the salary was for each day, then show total pay at the
# end of the period. Display final amount in in dollars; not pennies.

# Input
number_days = int(input("How many days would you like to see your earnings?" ))

# Process
earnings = .005
print("\nDay\t Earnings\n-----------------")

# Output
for day in range(1, number_days + 1, 1) :
	earnings *= 2
	print(day, "\t", format(earnings, ",.2f"))