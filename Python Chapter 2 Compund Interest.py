# Chapter 2 Exercise 14 Compound Interest

# This program calculates the amount of money that will be in the account
# after the specified number of years.

P = float(input('Enter principal amount: $'))
r = float(input('Enter annual interest rate %'))
n = float(input('Enter number of times per year interest has compounded: '))
t = float(input('Enter number of years account will be left to earn interest: '))

r /= 100  # 50% = .50
A = P * ((1 + (r / n))**(n * t))

print('After ', t, ' years, $', format(A, ',.2f'), ' will be in the account. ', sep='')