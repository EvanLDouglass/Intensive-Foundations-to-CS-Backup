# CS5001
# Lab 3, problem 1: Log base 2
# Evan Douglass


#### Purpose
# Calculates the log base 2 of a given positive integer that is a power of 2
# iteratively.
#
#### Signature
# log2 :: Integer => Integer
# 
#### Template
# def log2(given...)
#   return returns...
#
#### Examples
# log2(2) => 1
# log2(16) => 4
# log2(1) => 0
#
def log2(number):
    if number == 1:
        return 0
    else:
        # Divide the given number by 2 until the result is 1.
        # Return the number of iterations until 1 is reached.
        count = 0
        while number > 1:
            number //= 2
            count += 1
        return count

#### Tests
def test_log2():
    assert(log2(16) == 4)
    assert(log2(1) == 0)
    assert(log2(8) == 3)


#### Purpose
# Calculates the log base 2 of a given positive integer that is a power of 2
# recursively.
#
#### Signature
# log2_recursive :: Integer => Integer
# 
#### Template
# def log2_recursive(given...)
#   return returns...
#
#### Examples
# log2(2) => 1
# log2(16) => 4
# log2(1) => 0
#
def log2_recursive(number):
    # Base cases
    if number == 1:
        return 0
    elif number == 2:
        return 1
    # Recursive case
    else:
        return 1 + log2_recursive(number//2)

#### Tests
def test_log2_recursive():
    assert(log2_recursive(16) == 4)
    assert(log2_recursive(1) == 0)
    assert(log2_recursive(8) == 3)


# def main():
#     value = int(input("Enter a positive power of 2: "))
#     result_it = log2(value)
#     result_re = log2_recursive(value)
#     print("log2(" + str(value) + ") = " + str(result_it))
#     print("log2_recursive(" + str(value) + ") = " + str(result_re))

# main()
