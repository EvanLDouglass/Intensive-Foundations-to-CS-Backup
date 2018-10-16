# Evan Douglass
# CS5001
# Lab 5

alphabet = "abcdefghijklmnopqrstuvwxyz"


#### Purpose
# Encrypts a string using the Caesar Cipher method.
#### Signature
# encrypt :: (String, Integer) => String
#### Example
# encrypt("pizza", 3) => "slccd"
# encrypt("dog", 5) => "itl"
# encrypt("night", -1) => "mhfgs"
#
def encrypt(string, shift):
    string = string.lower()
    output = ""

    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            index += shift
            index %= 26
            output += alphabet[index]
        else:
            output += letter

    return output


#### Purpose
# Decrypts a string using the Caesar Cipher method.
#### Signature
# decrypt :: (String, Integer) => String
#### Example
# encrypt("slccd", 3) => "pizza"
# encrypt("itl", 5) => "dog"
# encrypt("mhfgs", -1) => "night"
#
def decrypt(string, shift):
    string = string.lower()
    output = ""

    for letter in string:
        if letter in alphabet:
            index = alphabet.index(letter)
            index -= shift
            index %= 26
            output += alphabet[index]
        else:
            output += letter

    return output


#### Purpose
# Decrypts a slide transformation on a string.
#### Signature
# decrypt_slide :: (String, Integer) => String
#### Examples
# decrypt_slide("ohell", 1) => "hello"
# decrypt_slide("ghtni", 3) => "night"
#
def decrypt_slide(string, slide):
    slide = -slide
    return string[-slide:] + string[:-slide]


#### Purpose
# Uses "brute force" to test decryptions of strings given a limited
# scope of decryption: a shift from 1-5 and a slide from 1-5.
#### Signature
# test_decryption :: String => Void
#### Examples
# Output is to extensive to write here
#
def test_decryption(string):
    
    for shift in range(0, 6):
        shifted = decrypt(string, shift)
        for slide in range(0, 6):
            shift_with_slide = decrypt_slide(shifted, slide)
            print("shift:", shift, "slide:", slide, shift_with_slide)
        print()


test_decryption("yko.vjg swguvkqp qh yjgvjgt eqorwvgtu ecp vjkpm ku nkmg vjg swguvkqp qh yjgvjgt uwdoctkpgu ecp u")