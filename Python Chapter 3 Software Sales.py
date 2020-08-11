# Chapter 3 Exercise 12 Software Sales

# This program Asks the User to Enter the Number of Packages Purchased,
# Display the Amount of the Discount (if any) and the Total Amount of
# the Purchase after the Discount


# Input
packages_purchased = float(input('Enter the number of packages purchased: '))

# Process
retail_price = 99

if packages_purchased < 10:
    discount_rate = 0
elif packages_purchased < 20:
    discount_rate = 0.1
elif packages_purchased < 50:
    discount_rate = 0.2
elif packages_purchased < 100:
    discount_rate = 0.3
else:
    discount_rate = 0.4

subtotal = packages_purchased * retail_price
total_discount = subtotal * discount_rate
total = subtotal - total_discount

# Output
print('\nSubtotal: $', format(subtotal, '10,.2f'),
      '\nDiscount: $', format(total_discount, '10,.2f'),
      '\nTotal:    $', format(total, '10,.2f'), sep='')