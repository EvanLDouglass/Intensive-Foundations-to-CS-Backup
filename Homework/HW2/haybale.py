# CS5001
# HW2: Hay Bale Maze
# Evan Douglass

'''Test Cases for get_price
In: 80, "sat", 13, False
Out: 10.5

In: 32, "thu", 20, True
Out: 10.1

In: 70, "tue", 6, False
Out: 9.0

In: 100, "hello", 33, "Nope"
Out: 9.0

In: -5, "what?", -5, True
Out: 8.5
'''

# Constants
BASE_PRICE = 9
TEMP_UPPER = 75
HOT_PREMIUM = 0.1
TEMP_LOWER = 40
COLD_DISCOUNT = 0.05
WEEKDAY_5PM = 2
WEEKEND_PREMIUM = 1
WEEKEND_5PM = 1
RAIN_DISCOUNT = 0.5

WEEKENDS = ["sat", "sun"]

#### Purpose
# Determines the price of admission for a Hay Bale Maze based on factors
# including temperature, day of the week, time of day, and whether it is raining.
#
#### Signature
# get_price :: (Integer, String, Integer, Boolean) => Float
#
#### Template
# def get_price(given...):
#   return returns...
#
#### Examples
# get_price(75, "mon", 12, False) => 9
# get_price(80, "sat", 14, False) => 10.5
# get_price(32, "thu", 19, True) => 10.1
#
def get_price(temp, day, hour, raining):
    price = BASE_PRICE

    # Adjust price for temperature
    if 75 < temp < 100:                     # above 99 => default to 75
        deg_above_max = temp - TEMP_UPPER
        price += (deg_above_max * HOT_PREMIUM)
    elif 0 <= temp < 40:                    # below 0 => default to 75
        deg_below_min = TEMP_LOWER - temp
        price -= (deg_below_min * COLD_DISCOUNT)
    else:
        # If temp between 40 and 75 deg inclusive no price change, do nothing.
        # If temp is negative or above 99 deg, default to 75, do nothing.
        pass

    # Adjust price for day of the week
    day = day.lower().strip()
    if day in WEEKENDS:
        price += WEEKEND_PREMIUM
    else:
        # If day is a weekday or invalid, default to "mon". All weekdays have
        # the same price, so all can be "mon" internally.
        day = "mon"

    # Adjust price for hour, based on day of the week
    if (17 < hour < 24) and (day == "mon"):
        price += WEEKDAY_5PM
    elif (17 < hour < 24) and (day in WEEKENDS):
        price += WEEKEND_5PM
    else:
        # If hour is between 0 and 17 (5pm) inclusive, no price change, do nothing.
        # If hour is negative or over 23 (0 == 24), default to 12, do nothing.
        pass
    
    # Adjust price if it is raining, no price change if not
    if raining == True:
        price -= RAIN_DISCOUNT
    
    return float(price)

# # Test get_price
# print(get_price(80, "sat", 13, False))      # 10.5
# print(get_price(32, "thu", 20, True))       # 10.1
# print(get_price(70, "TUE", 6, False))       # 9.0
# print(get_price(100, "hello", 33, "Nope"))  # 9.0
# print(get_price(-5, "what?", -5, True))     # 8.5


#### Purpose
# The main function. Gets user input for the get_price function and prints
# the result as a string.
#
#### Signature
# main :: () => String
#
#### Template
# def main(void):
#   void
#
#### Examples
# 80, sat, 13, N => Your price comes to $10.50
# 32, thu, 20, Y => Your price comes to $10.10
# 70, TUE, 6, n => Your price comes to $9.00
# 100, hello, 33, "Nope" => Your price comes to $9.00
# -5, "what?", -5, y => Your price comes to $8.50
# 
def main():
    # Get temperature
    # Truncate temperatures given as a float. Breaks with non-numeric input.
    temp = int(float(input("What is the current temperature (in Fahrenheit)? ")))

    # Get day of the week
    day = input("What is the day of the week? Use a three letter abbreviation: ")

    # Get time of day. Breaks with non-numeric input.
    time = int(float(input("What is the time of day? Use an integer from 0-23: ")))

    # Determine if it is raining
    raining = input("Is it raining (Y/N)? ").upper()
    if raining == "Y":
        raining = True
    else:
        raining = False

    # Get price; input validation done inside get_price
    price = get_price(temp, day, time, raining)

    # Output result
    print("Your final price comes to ${:.2f}".format(price))


main()
