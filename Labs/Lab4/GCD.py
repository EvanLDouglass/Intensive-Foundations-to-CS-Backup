# CS5001
# Lab 4: GCD
# Evan Douglass

#### Purpose
# Determines the greatest common divisor of two numbers using recursion.
# Found solution to this problem with help from Khan Academy at the URL:
# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
#
#### Signature
# gcd_recursive :: (Integer, Integer) => Integer
#
#### Examples
# gcd_recursive(12, 8) => 4
# gcd_recursive(15, 30) => 15
# gcd_recursive(10, 3) = 1
#
def gcd_recursive(num1, num2):
    '''
    Determines the greatest common divisor of two numbers using recursion.

    num1, num2 -- Non-zero positive integers.
    '''
    if num2 == 0:
        return num1
    else:
        return gcd_recursive(num2, num1%num2)

#### Tests
def test_gcd_recursive():
    assert(gcd_recursive(12, 8) == 4)
    assert(gcd_recursive(15, 30) == 15)
    assert(gcd_recursive(10, 3) == 1)
    assert(gcd_recursive(50, 30) == 10)
    assert(gcd_recursive(0, 40) == 40)
    assert(gcd_recursive(40, 0) == 40)


#### Purpose
# Determines the greatest common divisor of an arbitrary amount of positive
# integers.
#
#### Signature
# gcd_multiple_nums :: Integer[] => Integer
#
#### Examples
# gcd_multiple_nums([1, 4, 16]) => 4
# gcd_multiple_nums([2, 7, 23, 97]) => 1
# gcd_multiple_nums([10, 30, 40, 25, 5]) => 5
#
def gcd_multiple_nums(int_list):
    '''
    Determines the greatest common divisor of an arbitrary amount of positive 
    integers.

    int_list -- A list of positive Integers with length >= 2.
    '''
    first_two_gcd = gcd_recursive(int_list[0], int_list[1])
    if len(int_list) == 2:
        return first_two_gcd
    else:
        return gcd_multiple_nums([first_two_gcd] + int_list[2:])

#### Tests
def test_gcd_multiple_nums():
    assert(gcd_multiple_nums([15, 30]) == 15)
    assert(gcd_multiple_nums([0, 0, 67]) == 67)
    assert(gcd_multiple_nums([0, 0, 0, 0]) == 0)
    assert(gcd_multiple_nums([9, 0, 0, 0]) == 9)
    assert(gcd_multiple_nums([1, 4, 16]) == 1)
    assert(gcd_multiple_nums([2, 7, 23, 97]) == 1)
    assert(gcd_multiple_nums([10, 30, 40, 25, 5]) == 5)
