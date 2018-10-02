# CS5001
# Lab 3, problem 1: Draw a rectangle
# Evan Douglass


#### Purpose
# Draws a rectangle of a given width and height on the command line with a
# given character.
#
#### Signature
# draw_rect :: (Integer, Integer, String) => String
#
#### Template
# def draw_rect(given...)
#   return returns...
#
#### Examples
# draw_rect(6, 4, "*") => ******
#                         *    *
#                         *    *
#                         ******
# draw_rect(3, 3, "7") => 777
#                         7 7
#                         777
#
def draw_rect(width, height, char):
    for row in range(height):
        for column in range(width):
            # Top and bottom rows are solid characters
            if row == 0 or row == height-1:
                print(char, end="")
            else:
                if column == 0 or column == width-1:
                    print(char, end="")
                else:
                    print(" ", end="")
        print()


#### Purpose
# Draws a rectangle of a given width and height on the command line with a
# given character.
#
#### Signature
# draw_rect_alt :: (Integer, Integer, String) => String
#
#### Template
# def draw_rect(given...)
#   return returns...
#
#### Examples
# draw_rect(6, 4, "*") => ******
#                         *    *
#                         *    *
#                         ******
# draw_rect(3, 3, "7") => 777
#                         7 7
#                         777
#
def draw_rect_alt(width, height, char):
    for row in range(height):
        if row == 0 or row == height-1:
            print(char * width)
        else:
            print(char, end="")
            print(" " * (width-2), end="")
            print(char)


width = int(input("Enter a width: "))
height = int(input("Enter a height: "))
char = input("Choose a character: ")
draw_rect(width, height, char)
draw_rect_alt(width, height, char)
