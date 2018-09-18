'''
Lab 1
Problem 2: Buying a house
Evan Douglass
'''

### Purpose
# To find out how long it will take to buy a house given parameters.
# Parameters: cost of the house, annual salary, percent of salary saved per 
# month
# Returns: amount needed for down payment, amount being saved per month, how 
# many years and months until enough is saved for a down payment...all as a 
# string.
#
### Signature
# time_to_buy_house :: number, number, number => string
#
### Template
# time_to_buy_house(given...)
#   return returns...
#
### Examples
# time_to_buy_house(100000, 50000, 0.25) => "If you save $1041.67 per month, 
# it will take 2 year(s) and 0 month(s) to save enough for the down payment!"

def time_to_buy_house(cost_of_house, annual_salary, percent_salary_saved):
    # find down payment (25% of cost)
    down_payment = cost_of_house * 0.25
    # find monthly savings
    monthly_savings = annual_salary * percent_salary_saved / 12
    # calculate months till down payment reached
    months_to_save = down_payment / monthly_savings
    # calculate years, months from months
    years = months_to_save // 12
    months = months_to_save % 12

    # format message
    message = "If you save ${0:.2f} per month, it will take {1:.0f} year(s)" + \
        " and {2:.0f} month(s) to save enough for the down payment!"

    return message.format(monthly_savings, years, months)

# Test run
print(time_to_buy_house(100000, 50000, 0.25))