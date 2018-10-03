# CS5001
# HW 3: UPC Testing
# Evan Douglass

'''Test cases for is_valid_UPC
Case #1: Hand Sanitizer
073852022391 -- valid
07385202239  -- invalid, missing last number
073852922391 -- invalid, typed 9 instead of 0

Case #2: Kleenex tissue box
036000214000 -- valid
03000214000  -- invalid, missing a 6
036000124000 -- invalid, switched a 1 and 2

Case #3: Box of paper clips
718103049658 -- valid
718103049648 -- invalid, typed 4 instead of 5
1810304965   -- invalid, didn't include the start or end numbers
'''

#### Purpose
# Tests whether a given UPC string is valid.
# 
#### Signature
# is_valid_UPC :: String => Boolean
#
#### Examples
# is_valid_UPC("073854008089") => True
# is_valid_UPC("073854008090") => False
#
def is_valid_UPC(str_UPC):
    total = 0
    # iterate from left to right in UPC
    for i, char in enumerate(reversed(str_UPC)):
        if i % 2 == 0:
            # Add numbers in even positions to total
            total += int(char)
        else:
            # Multiply numbers in odd positions by 3 then add to total
            total += 3*int(char)
    
    # Test if total is a multiple of 10
    return total % 10 == 0
        

#### Main Program ####
upc = input("Enter a UPC number:\n")
if is_valid_UPC(upc):
    print("Valid UPC!")
else:
    print("Not a valid UPC.")