# CS5001
# Lab 3, problem 1: Convert binary into decimal
# Evan Douglass


#### Purpose
# Converts a binary number into base 10 form, iteratively.
#
#### Signature
# binary_to_decimal :: String => Integer
#
#### Template
# def binary_to_decimal(given...)
#   return returns...
#
#### Examples
# binary_to_decimal("1") => 1
# binary_to_decimal("10") => 2
# binary_to_decimal("1101101") => 109
#
def binary_to_decimal(binary_string):
    # Loop from the back of the string to the front (w/o reversing)
    pwr = 0
    total = 0
    for index in range(len(binary_string)-1, -1, -1):
        if binary_string[index] == "1":
            total += 2**pwr
            pwr += 1
        else:
            # add zero to result and increment place/power value
            pwr += 1
    
    return total


#### Purpose
# Converts a binary number into base 10 form, recursively.
#
#### Signature
# binary_to_decimal_recur :: String => Integer
#
#### Template
# def binary_to_decimal_recur(given...)
#   return returns...
#
#### Examples
# binary_to_decimal("1") => 1
# binary_to_decimal("10") => 2
# binary_to_decimal("1101101") => 109
#
def binary_to_decimal_recur(binary_string):
    # Base cases
    if binary_string == "0":
        return 0
    elif binary_string == "1":
        return 1
    # Recursive case
    else:
        return 2*binary_to_decimal_recur(binary_string[0:-1]) \
               + binary_to_decimal_recur(binary_string[-1])


binary_string = input("Enter a binary number: ")
converted = binary_to_decimal(binary_string)
converted_recur = binary_to_decimal_recur(binary_string)
print(binary_string, "=", converted)
print(binary_string, "=", converted_recur)