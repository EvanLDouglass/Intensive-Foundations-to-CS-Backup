# CS5001
# Fall 2018
# HW1: Data Types and Arithmetic Operations
# Evan Douglass

import math

'''
Test Cases #1
5k race, 0 hours and 26 minutes:
    3.11 miles, 8:22 pace, 7.17 MPH

10k race, 1 hour and 10 minutes:
    6.21 miles, 11:16 pace, 5.32 MPH

50k race, 5 hours and 15 minutes:
    31.06 miles, 10:09 pace, 5.92 MPH
'''

# ========== Function: get_race_stats ==========

#### Purpose
# To calculate basic statistics about a foot race given information about the 
# distance and the time it took a runner to finish.
#
#### Signature
# get_race_stats :: (Number, Number, Number) => String
#
#### Template
# def get_race_stats(given...)
#   return returns...
#
#### Examples
# get_race_stats(5, 0, 26) => You ran 3.11 miles
#                             Your pace: 8 min 22 sec per mile
#                             Your MPH: 7.17
# get_race_stats(10, 1, 10) => You ran 6.21 miles
#                              Your pace: 11 min 16 sec per mile
#                              Your MPH: 5.32
# get_race_stats(50, 5, 15) => You ran 31.06 miles
#                              Your pace: 10 min 09 sec per mile
#                              Your MPH: 5.92
# get_race_stats(1.61, 1, 0) => You ran 1 mile
#                               Your pace: 60 min 00 sec per mile
#                               Your MPH: 1.00
#
def get_race_stats(distance, hours, minutes):
    '''
    Calculates basic statistics about a foot race given information about 
    the distance and the time it took a runner to finish.

    int,float distace -- The distance of a race in kilometers.
    int hours -- The hours portion of the time to finish.
    int minutes -- The minutes portion fo the time to finish.
    Returns a string detailing the distance in miles, pace in minutes and 
        seconds, and miles per hour.
    '''
    # Convert kilometers to miles. 1.61 kilometers per 1 mile.
    miles = distance / 1.61 

    # Get total hours and total minutes for pace and mph calculations.
    total_hours = hours + minutes/60
    total_mins = hours*60 + minutes

    # Calculate pace and separate into minutes and seconds.
    pace = total_mins / miles
    pace_mins = math.floor(pace)
    pace_secs = pace % pace_mins * 60

    # Calculate mph
    mph = miles / total_hours

    # Prepare output strings. Kept in separate variables for readability.
    if miles == 1:
        miles_txt = "You ran 1 mile\n"
    else:   # needs "miles" plural
        miles_txt = "You ran {:.2f} miles\n".format(miles)

    pace_txt = "Your pace: {0:.0f} min {1:02.0f} sec per mile\n".format(pace_mins, pace_secs)
    mph_txt = "Your MPH: {:.2f}".format(mph)

    # Returned without trailing \n for use in print.
    return miles_txt + pace_txt + mph_txt

### Test get_race_stats ###
# print(get_race_stats(5, 0, 26))
# print(get_race_stats(10, 1, 10))
# print(get_race_stats(50, 5, 15))
# print(get_race_stats(1.61, 1, 0))  # Tests singular mile case

# ========== end get_race_stats ==========


# ========== Function: get_user_input ==========

#### Purpose
# Gets user input regarding the length of a race they ran and how long it 
# took them.
#
#### Signature
# get_user_input :: () => (Number, Number, Number)
#
#### Template
# def get_user_input():
#   return returns...
#
#### Examples
# get_user_input() => How many kilometers did you run? 5
#                     How many (full) hours did it take you? 1
#                     How many minutes? 10
#                     => (5, 1, 10)
# get_user_input() => How many kilometers did you run? 40
#                     How many (full) hours did it take you? 3
#                     How many minutes? 36
#                     => (40, 3, 36)
#
def get_user_input():
    '''
    Gets user input regarding the length of a race they ran and how long it 
    took them.

    No parameters
    Returns as integers the length of the race in kilometers and the time it 
        took in hours and minutes.
    '''
    kilometers = int(input("How many kilometers did you run? "))
    hours = int(input("How many (full) hours did it take you? "))
    mins = int(input("How many minutes? "))

    return (kilometers, hours, mins)

### Test get_user_input ###
# print(get_user_input())
# print(get_user_input())

# ========== end get_user_input ==========


# Run the program.
kilometers, hours, mins = get_user_input()
print()
print(get_race_stats(kilometers, hours, mins))
