# CS5001
# HW 3: String Processing
# Evan Douglass


#### Purpose
# This function takes a string as input and returns the uppercase
# version of the string.
#
#### Signature
# to_upper :: String => String
#
#### Template
# def to_upper(given…):
# return returns…
#
#### Examples
# to_upper(“test string 9000”) => “TEST STRING 9000”
# to_upper(“ThIs Is A sTrInG”) => “THIS IS A STRING”
#
def to_upper(string):
    upper_map = {"a": "A", "b": "B", "c":"C", "d": "D", "e": "E", "f": "F", 
                 "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", 
                 "m": "M", "n": "N", "o": "O", "p": "P", "q": "Q", "r": "R",
                 "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X", 
                 "y": "Y", "z": "Z"}
    upper = ""
    # Replace all lower case letters with uppercase letters
    for char in string:
        if char in upper_map:  # Tests for keys in the map
            upper += upper_map[char]
        else:
            # When not lowercase, add the same char back
            upper += char

    return upper


#### Purpose
# This function takes a string as input and returns the lowercase
# version of the string
#
#### Signature
# to_lower :: String => String
#
#### Template
# def to_lower(given…):
# return returns...
#
#### Examples
# to_lower(“SHOUTY STRING”) => “shouty string”
# to_lower(“ThIs Is A sTrInG”) => “this is a string”
#
def to_lower(string):
    lower_map = {"A": "a", "B": "b", "C":"c", "D": "d", "E": "e", "F": "f", 
                 "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l", 
                 "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r",
                 "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", 
                 "Y": "y", "Z": "z"}
    lower = ""
    # Replace all lower case letters with lowercase letters
    for char in string:
        if char in lower_map:  # Tests for keys in the map
            lower += lower_map[char]
        else:
            # When not lowercase, add the same char back
            lower += char

    return lower


#### Purpose
# This function takes a string as input and returns the reverse of
# that string, maintaining the case of the original string.
#
#### Signature
# in_reverse :: String => String
#
#### Template
# def in_reverse(given…):
# return returns...
#
#### Examples
# in_reverse(“Tuesday 3:00 PM”) => “MP 00:3 yadseuT”
# in_reverse(“abcde”) => “edcba”
#
def in_reverse(string):
    reverse = ""
    # cycle backwards through the given string using indexes
    for index in range(len(string)-1, -1, -1):
        # Add each letter to the reverse string
        reverse += string[index]
    
    return reverse


print("Testing to_upper:")
print("test string 9000 =>", to_upper("test string 9000"))
print("ThIs Is A sTrInG =>", to_upper("ThIs Is A sTrInG"))
print()
print("Testing to_lower:")
print("SHOUTY STRING =>", to_lower("SHOUTY STRING"))
print("ThIs Is A sTrInG =>", to_lower("ThIs Is A sTrInG"))
print()
print("Testing in_reverse:")
print("Tuesday 3:00 PM =>", in_reverse("Tuesday 3:00 PM"))
print("abcde =>", in_reverse("abcde"))
