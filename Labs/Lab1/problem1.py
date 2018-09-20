'''
Lab 1
Problem 1: Eating out with a group
Evan Douglass
'''

### Purpose
# To calculate how to split a restaurant bill between a given number of people.
# Parameters: total amount of bill, tip percentage as decimal, how many people
# are splitting the bill.
# Returns: the amount that each person owes on the bill, rounded to two decimal
# places.
#
### Signature
# amt_owed :: (number, number, number) => number
#
### Template
# amt_owed(given...)
#   return returns...
#
### Examples
# amt_owed(60, 0.2, 3) => 24.0
# amt_owed(110.90, 0.15, 6) => 21.26
# amt_owed(20, 1, 1) => 40.0

def amt_owed(total_bill, tip_percent, num_people):
    tip_amount = total_bill * tip_percent
    return round((total_bill + tip_amount) / num_people, 2)

# Test runs
print("Test runs\nExpected results: 24.0, 21.26, 40.0")
print(amt_owed(60, 0.2, 3))
print(amt_owed(110.9, 0.15, 6))
print(amt_owed(20, 1, 1))