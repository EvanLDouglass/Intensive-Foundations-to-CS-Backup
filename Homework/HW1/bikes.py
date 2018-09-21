# CS5001
# Fall 2018
# HW1: Data Types and Arithmetic Operations
# Evan Douglass
#
# Note: Test cases comment moved to immediately above where the test 
# cases are called.


# ========== Function: make_bikes ==========
#### Purpose
# Determines the number of bikes that can be made given some amount
# of spare parts. Also determines the parts leftover.
#
#### Signature
# make_bikes :: (Number, Number, Number) => String
#
#### Template
# def make_bikes(given...)
#   return returns...
#
#### Examples
# make_bikes(40, 10, 300) => I can make 6 bikes with that.
#                            OK, 6 bikes on the way!
#                            I'll keep the leftovers:
#                            28 wheels, 4 frames and 0 links
# make_bikes(2, 1, 35) => I can't make any bikes with that.
#                         You'll have to bring back more parts!
#                         You have 2/2 tires, 1/1 frame and 35/50 links
#
def make_bikes(wheels, frames, links):
    '''Determines the number of bikes that can be made given some amount
    of spare parts. Also determines the parts leftover. One bike requires
    2 wheels, 1 frame and 50 links.

    int wheels -- The number of wheels.
    int frames -- The number of frames.
    int links -- The number of links.
    Returns text describing how many bikes were made and how many
    parts are left.
    '''
    # Determine how many bikes can be made.
    num_bikes = min(wheels//2, frames, links//50)
    
    # Determine leftovers
    wheels_left = wheels - num_bikes*2
    frames_left = frames - num_bikes
    links_left = links - num_bikes*50

    # Output message
    if num_bikes > 0:
        message = "I can make {0} bikes with that.\n" + \
                  "OK, {0} bikes on the way!\n" + \
                  "I'll keep the leftovers:\n" + \
                  "{1} wheels, {2} frames and {3} links."
        message = message.format(num_bikes, wheels_left, frames_left, links_left)
    else:    # No bikes made
        message = "I can't make any bikes with that.\n" + \
                  "You'll have to bring back more parts!\n" + \
                  "You have {0}/2 tires, {1}/1 frames and {2}/50 links."
        message = message.format(wheels_left, frames_left, links_left)
    
    return message

'''Test Cases:
In: 2 wheels, 1 frame, 35 links
Out: Bike not built. Leftover: 2 wheels, 1 frame, 35 links

In: 40 wheels, 10 frames, 300 links
Out: 6 bikes built. Leftover: 28 wheels, 4 frames, 0 links

In: 123 wheels, 111 frames, 783 links
Out: 15 bikes built. Leftover: 93 wheels, 96 frames, 33 links
'''
# print(make_bikes(2, 1, 35))
# print()
# print(make_bikes(40, 10, 300))
# print()
# print(make_bikes(123, 111, 783))

# ========== end make_bikes ==========


# ========== Function: get_input ==========
#### Purpose
# Gets user input and outputs a tuple of three integers.
#
#### Signature
# get_input :: () => (Number, Number, Number)
#
#### Template
# def get_input():
#   return returns...
#
#### Examples
# get_input() => How many wheels do you have? 2
#                How many frames do you have? 5
#                How many links do you have? 80
#                => (2, 5, 80)
# get_input() => How many wheels do you have? 2.3
#                How many frames do you have? 5
#                How many links do you have? 80.9
#                => (2, 5, 80)
#
def get_input():
    '''Gets user input and outputs a tuple of 3 integers.'''

    # In case of floats, must convert from str=>float=>int
    wheels = int(float(input("How many wheels do you have? ")))
    frames = int(float(input("How many frames do you have? ")))
    links = int(float(input("How many links do you have? ")))

    return (wheels, frames, links)

'''Test Cases:
In: 4, 9, 23
Out: (4, 9, 23)

In: 4456, 987987, 1234
Out: (4456, 987987, 1234)

In: 4.567, 990.1, 80
Out: (4, 990, 80)
'''
# print(get_input())
# print(get_input())
# print(get_input())

# ========== end get_input ==========


# Run the program
wheels, frames, links = get_input()
print()
print(make_bikes(wheels, frames, links))