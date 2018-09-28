# CS5001
# HW2: Palindrome
# Evan Douglass

'''Test Cases
In: 'Radar'
Out: True

In: ' Radar'
Out: True

In: ' R a Dar      '
Out: True

In: '123edcde321'
Out: True

In: '!@  5 5  @!'
Out: True

In: 'Hello'
Out: False

In: ''
Out: False

In: 'a'
Out: False

In: 'Radar!'
Out: False

In: '   R   '
Out: False
'''
#### Purpose
# Checks if a given string is a palindrome (e.g. spelled the same forwards
# and backwards). Whitespace in the front, middle or back of a word does not
# affect the outcome, neither do the case of characters. Punctuation marks do
# influence the outcome.
#
#### Signature
# is_pal :: String => Boolean
#
#### Template
# def is_pal(given...)
#   return returns...
#
#### Examples
# is_pal('Hello') => False
# is_pal('Radar') => True
# is_pal('  RaDaR') => True
# is_pal('Radar!') => False
#
def is_pal(string):
    # Process the string
    string = string.replace(' ', '').lower()

    if len(string) <= 1:    # Automatic fail cases
        return False
    else:
        # Separate string at midpoint
        s_len = len(string)
        mid_point = s_len // 2
        if s_len % 2 == 0:
            # Even strings are seperated between middle two chars
            s_start = string[:mid_point]
            s_end = string[mid_point:]
        else:
            # Odd strings ignore middle char so each substring is equal length
            s_start = string[:mid_point]
            s_end = string[mid_point+1:]
        
        # Reverse end of string for equality testing
        s_end_rev = s_end[::-1]

        return s_start == s_end_rev
            

## Test is_pal =================================================================
# function_in = ['Radar', ' Radar', ' R a Dar      ', '123edcde321', '!@  5 5  @!',
#                'Hello', '', 'a', 'Radar!', '  R  ']
# function_out = [True, True, True, True, True, False, False, False, False, False]
# for index, string in enumerate(function_in):
#     test_out = is_pal(string)
#     if test_out != function_out[index]:
#         print('Failed on test case:', string)
#         print('Expected', function_out[index], 'got', test_out)
#         exit()
# print('Passed all test cases')
## End test ====================================================================


#### Purpose
# Gets a string from the user and tells them if it is a palindrome.
#
#### Signature
# main :: () => String
#
#### Template
# def main():
#   void
#
#### Examples
# 'Radar' => Radar is a palindrome
# 'Hello' => Hello is not a palindrome
# '!Radar!' = > !Radar! is a palindrome
#
def main():
    test_str = input('Enter a word or phrase:\n')
    if is_pal(test_str):
        print(test_str.strip(), 'is a palindrome')
    else:
        print(test_str.strip(), 'is not a palindrome')


main()
