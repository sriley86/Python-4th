# Chapter2 Exercise 6 Sales Tax

# This program displays the Sales tax on purchased amount
# Definition of the main function
def main():
    # Get the purchase amount
    purchaseAmount = getinput()
    print("The amount of the purchase:", purchaseAmount)

    statesalestax = calstatesalestax(purchaseAmount)
    print("The state sales tax:", statesalestax)

    countysalestax = calcountysalestax(purchaseAmount)
    print("The county sales tax:", countysalestax)

    Totalsalestax = caltotalsalestax(statesalestax, countysalestax)
    print("The total sales tax:", Totalsalestax)

    Totalofthesale = totalofsale(purchaseAmount, Totalsalestax)
    print("The total of the sale:", Totalofthesale)


# definition of  getinput function
def getinput():
    # Get the purchase amount
    purchaseAmount = float(input("Enter the amount of a purchase:"))
    return purchaseAmount


# Definition of the  calstatesalestax function
def calstatesalestax(purchaseAmount):
    # Assign the value to State sales tax percentage
    Statesalestaxpercentage = 0.04
    # Calculate the state sales tax
    statesalestax = purchaseAmount * Statesalestaxpercentage
    return statesalestax


# Definition of the  calcountysalestax function
def calcountysalestax(purchaseAmount):
    # Assign the value to county sales tax percentage
    countysalestaxpercentage = 0.02
    # Calculate the county sales tax
    countysalestax = purchaseAmount * countysalestaxpercentage
    return countysalestax


# Definition of the  caltotalsalestax function
def caltotalsalestax(statesalestax, countysalestax):
    # Calculate the total sales tax
    Totalsalestax = statesalestax + countysalestax
    return Totalsalestax


# Definition of the  totalofsale function
def totalofsale(purchaseAmount, totalsalestax):
    # Calculate the total of the sale
    Totalofthesale = purchaseAmount + totalsalestax
    return Totalofthesale


# calling the main function
main()