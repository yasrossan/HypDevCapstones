import math

# ***PSEUDOCODE***
# Print initial menu as shown in 1.
# get user input, add .lower() so that however the user capitalises the word it will be valid
# if user choosen invalid input out of 2, show error msg
#
# If investment chosen - 
# get user input - amount of money being deposited
# get user input for percentage of interest
# get user input - num of years being invested
# get user input - simple or compound interest
# follow formula 
# print answer
#
# If bond chosen - 
# get user input - present house value
# get user input - interest rate
# get user input - num of months they plan to take to repay bond
# calcuate monthly repayment
# print answer
# ************************

# Menu shown to user to choose whether bond or investment & gathering user choice
print("""Choose either 'Investment' or 'Bond' from the menu below to proceed:
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
""")

user_choice = input("").lower()

# Gathering initial variables needed
if user_choice == "investment":
    print("\nYou have chosen investment \n")
    deposit_amount = int(input("Please enter the amount of money you are depositing rounded to the nearest £: "))
    interest_rate = int(input("Please enter your interest rate as a percentage. Please only enter the number and not %: "))
    years_investing = int(input("Please enter the amount of years you are planning to invest for: "))

    interest_choice = input("\nPlease choose whether you want 'simple' interest or 'compound' interest:\n").lower()
    # Assigning formula values to current variables.
    r = (interest_rate / 100)
    P = deposit_amount
    t = years_investing
    
    # User choice. Calculations for user choice and returning answer
    
    if interest_choice == "simple":
        print("\nYou have chosen simple interest\n")
        A = P * (1 + (r * t))
        #format A for user readability. Adds ',' after every thousand places and rounding to 2 decimal place
        print(f"The total amount once simple interest is applied is {A:,.2f}")
    
    elif interest_choice == "compound":
        print("\nYou have chosen compound interest\n")
        A = P * math.pow((1 + r), t)
        print(f"The total amount once compound interest is applied is {A:,.2f}")
    else:
        print("Invalid input. Please choose either 'simple' or 'compound'")

# Gathering initial variables for calculation
elif user_choice == "bond":
    print("\nYou have chosen bond\n")
    house_value = int(input("Please enter the present value of the house to the nearest £: "))
    interest_rate = int(input("Please enter your interest rate as a percentage. Please only enter the number and not %: "))
    bond_repayment_monthly = int(input("Please enter the number of months you plan to take to repay the bond: "))

    P = house_value
    i = (interest_rate / 100) / 12
    n = bond_repayment_monthly

    # Bond Formula
    # Round function rounds decimals to 2dp
    A = (i * P) / (1 - (1 + i)**(-n))
    A = round(A , 2)
    print(f"The total you will have to repay monthly is {A:,}")

#Returns invalid input if user choice doesn't meet either investment or bond   
else:
    print("Invalid input. Please run the program again and choose either 'investment' or 'bond'")
