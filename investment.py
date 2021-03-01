def calculate_apr(principal, interest_rate , years ):
    """This function takes on three paramaters since its the the main function"""
    x= 0
    """Made a varible to equal to zero because the parameters need to be greater than 0"""
    if principal <= x or interest_rate <= 0 or years <= 0:
       return False
    """I made this if statement because it would return false when parameters are less than 0"""
    while x < years:
      principal = float(principal)*(1+ float(interest_rate))**float(years)
      x=x+1
      return abs(principal)
    """This while loop goes after because we need to check if its negative then if its not it would loop"""
    """x is less than years because once the person gets more money as they get older"""
print(calculate_apr(principal=200, interest_rate=0.04,years=65))
"""This print statement is here because it calls the function and prints out the values that you would input"""

