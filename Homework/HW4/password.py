# CS5001
# HW 4: Password Checker
# Evan Douglass

# Checks if a password is valid based on its length and contents.
def main():
    password = input("Please choose a password:\n")
    error = ""

    # Test if password is valid, include error message if not.
    # Not limited to one error message.
    if not is_valid_length(password):
        error += "must be between 6 and 12 characters, inclusive\n"
    if not has_letter(password):
        error += "must contain at least 1 letter\n"
    if not has_number(password):
        error += "must contain at least 1 number\n"
    if not has_special(password):
        error += "must contain at least 1 special character ($, #, @, !)\n"

    # If error is empty, password passed all tests
    if error == "":
        print("Password is valid")
    else:
        print("Password is invalid:\n" + error.strip())  # strip removes trailing newline


#### Purpose
# Checks if the length of a given password is between 6 and 12, inclusive.
#
#### Signature
# is_valid_length :: String => Boolean
#
#### Examples
# is_valid_length("Hello123") => True
# is_valid_length("Oops") => False
# is_valid_length("this is the greatest password ever") => False
#
def is_valid_length(password):
    return 6 <= len(password) <= 12

#### Tests
def test_is_valid_length():
    assert(is_valid_length("Hello123") == True)
    assert(is_valid_length("Oops") == False)
    assert(is_valid_length("this is the greatest password ever") == False)
    assert(is_valid_length("") == False)
    assert(is_valid_length("abc123") == True)
    assert(is_valid_length("abc123!@#987") == True)
    assert(is_valid_length("         ") == True)  # 9 spaces


#### Purpose
# Makes a case insensitive determination of whether or not a given password
# has a letter in it.
#
#### Signature
# has_letter :: String => Boolean
#
#### Examples
# has_letter("Password") => True
# has_letter("123!@#") => False
#
def has_letter(password):
    VALID_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for char in password:
        if char in VALID_LETTERS:
            return True
    return False

#### Tests
def test_has_letter():
    assert(has_letter("Password") == True)
    assert(has_letter("123!@#") == False)
    assert(has_letter("") == False)
    assert(has_letter("        ") == False)
    assert(has_letter("123abc") == True)
    assert(has_letter("123ABC") == True)
    assert(has_letter("z") == True)
    assert(has_letter("abc123!@#ZYX") == True)
    assert(has_letter("  554321!@#~`[]24 d") == True)


#### Purpose
# Checks if a given password has a number (0-9) in it.
#
#### Signature
# has_number :: String => Boolean
#
#### Examples
# has_number("Pa$$word24") => True
# has_number("Pa$$word") => False
#
def has_number(password):
    VALID_NUMBERS = "0123456789"
    for char in password:
        if char in VALID_NUMBERS:
            return True
    return False

#### Tests
def test_has_number():
    assert(has_number("Pa$$word24") == True)
    assert(has_number("Pa$$word") == False)
    assert(has_number("") == False)
    assert(has_number("1") == True)
    assert(has_number("!@#$%^&") == False)
    assert(has_number("abcdefghijklmon4") == True)


#### Purpose
# Checks if a given password has a special character. Special characters are
# restricted to $, #, @, and !
#
#### Signature
# has_special :: String => Boolean
#
#### Examples
# has_special("Pa$$word") => True
# has_special("NoSpecials23") => False
# has_special("%^&*-_+=") => False
#
def has_special(password):
    VALID_SPECIALS = "$#@!"
    for char in password:
        if char in VALID_SPECIALS:
            return True
    return False

#### Tests
def test_has_special():
    assert(has_special("Pa$$word") == True)
    assert(has_special("NoSpecials23") == False)
    assert(has_special("%^&*-_+=") == False) 
    assert(has_special("Hello!") == True)
    assert(has_special("P@ssword") == True)
    assert(has_special("#Password#") == True)
    assert(has_special("") == False)
    assert(has_special("   ") == False)
    

main()
