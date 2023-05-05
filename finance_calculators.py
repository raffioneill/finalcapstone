import math
# prompt the user to choose between an investment or bond type.
print("Investment-calculate total on your investment.")
print("Bond-calculate the amount you'll have to pay on a home loan")
investment_bond = input("Investment or bond? ")

# used the casefold manipulator to ignore case sensitivity in input.
# defined inputs with descriptive variable names.
if investment_bond.casefold() == ("investment"):
    deposit_amount = int(input("Deposit amount: "))
    interest_percentage = int(input("Estimated interest rate: "))
    years_investing = int(input("Estimated years invested: "))
    interest = input("Simple or compound: ")

    if interest.casefold() == ("simple"):
        interest_r = interest_percentage / 100
        dep_p = deposit_amount
        years_t = years_investing
        total = dep_p*(1 + interest_r * years_t)
        print("The total amount after the given period, at the specified interest rate is $", total)

# defines each component of the formula and executes it + prints amount.
    elif interest.casefold() == ("compound"):
        interest_r = interest_percentage / 100
        dep_p = deposit_amount
        years_t = years_investing
        total = dep_p * math.pow((1+interest_r), years_t)

        print("The total amount after the given period, at the specified interest rate is $", total)

# same process down below for bond option.
elif investment_bond.casefold() == ("bond"):
    house_value = int(input("What is the value of the house?"))
    interest_rate_bond = int(input("What is the interest rate?"))
    months_amount = int(input("How many months?"))
    house_p = house_value
    interest_rate_i = (interest_rate_bond / 100) / 12
    months_n = months_amount
    repayment = (interest_rate_i * house_p) / \
        (1 - (1 + interest_rate_i)**(-months_n))
    print("Your monthly repayment amount is $", round(repayment, 2))

else:
    print("Invalid")
