'''
The othello module is used to play the game Othello. It is the final 
project for CS5001 at Northeastern University.

Author: Evan Douglass
'''

import turtle

#### Module constants and global variables ####
SQUARE = 50     # pixels
RADIUS = 40     # pixels

window = turtle.Screen()
othello = turtle.Turtle()


#### Classes ####
class GameBoard:
    '''The GameBoard class contains the functionality of a board for the game Othello.'''

    def __init__(self, n):
        # The user will go first and is assigned the black pieces
        self.n = n
        self.turn = "black"
        self.size = SQUARE * n
        self.pieces = [None for location in range(n*n)]

        # Set up list to track clicked squares
        start = -n * SQUARE / 2
        self.squares = self.init_squares(n, start)

        # Draw the empty board
        self.draw_board()

        # Draw the starting tiles
        self.draw_start_tiles()

    ## SIGNATURE
    # draw_board :: Integer => Void
    def draw_board(self):
        '''Draws an nxn board with a green background.'''

        if self.n % 2 == 1 or self.n < 4:
            raise ValueError("n must be even and at least 4")

        # Setup window
        window.setup(self.size + SQUARE, self.size + SQUARE)
        window.screensize(self.size, self.size)
        window.bgcolor("white")
        window.title("Othello")

        # Create turtle to draw the board
        othello.penup()
        othello.speed(0)
        othello.hideturtle()

        # Line color is black, fill color is green
        othello.color("black", "forest green")

        # Move the turtle to the lower left corner
        corner = -self.n * SQUARE // 2
        othello.setposition(corner, corner)

        # Draw the green background
        othello.begin_fill()
        for i in range(4):
            othello.pendown()
            othello.forward(SQUARE * self.n)
            othello.left(90)
        othello.end_fill()

        # Draw the horizontal lines
        for i in range(self.n + 1):
            othello.setposition(corner, SQUARE * i + corner)
            self.draw_lines()

        # Draw the vertical lines
        othello.left(90)
        for i in range(self.n + 1):
            othello.setposition(SQUARE * i + corner, corner)
            self.draw_lines()

    ## SIGNATURE
    # draw_lines :: (Object, Integer) => Void
    def draw_lines(self):
        '''
        Draws a line on an othello board. A helper function for draw_board.
        Turtle turt -- A Turtle object.
        '''
        othello.pendown()
        othello.forward(SQUARE * self.n)
        othello.penup()

    ## SIGNATURE
    # draw_start_tiles :: Object => Void
    def draw_start_tiles(self):
        '''
        Draws the four starting tiles on the board
        '''
        ur, ul, lr, ll = self.find_center_squares(self.n)
        color = "white"
        # locations of lower squares are switched here to get colors right
        for location in (ur, ul, ll, lr):
            x, y = self.squares[location].calc_center()
            piece = GamePiece(location, color, x, y)
            self.pieces[location] = piece
            piece.draw_tile()

            if color == "white":
                color = "black"
            else:
                color = "white"

    ## SIGNATURE
    # init_squares :: (Object, Integer) => Object
    def init_squares(self, n, corner):
        '''
        Populates the self.squares list.
        int n -- The number of squares on one side of the board.
        int corner -- A number representing the x & y coordinate of the 
        first square.
        Returns a list of Square objects
        '''
        corner = int(corner)
        lst = []
        index = 0
        # y-coordinates can continuously increase
        y_corner = corner
        for row in range(n):
            # x-coordinate values need to start over on each row
            x_corner = corner
            for column in range(n):
                lst.append(Square(index, x_corner, y_corner))
                index += 1
                x_corner += SQUARE
            y_corner += SQUARE
        
        return lst

    ## SIGNATURE
    # find_center_squares :: (Object, Integer) => Integer[]
    def find_center_squares(self, n):
        '''
        Finds the four center starting squares on the board.
        int n -- The number of squares on one side of the board. Must be even.
        Returns a tuple of ints representing the indexes of the four center 
        squares on the draw_board.
        '''
        # If n is even and the board grid is indexed from 0 to n*n
        # then the upper right center square can be found with the formula:
        # 0.5(n**2 + n)
        # I worked this out on paper myself.
        # The remaining squares can be found by subtracting from that result:
        # 1, n, n+1 for upper left, lower right, and lower left respectively
        ur = int(0.5 * (n**2 + n))
        ul = ur - 1
        lr = ur - n
        ll = lr - 1
        return (ur, ul, lr, ll)

    ## SIGNATURE
    # place :: (Object, Integer, String, Integer, Integer) => Void
    def place(self, location, color, x, y):
        '''
        Initializes a Gamepiece object on the Othello board at the given 
        location and with the given color.

        int location -- An index representing a square on the board (0 to n*n).
        str color -- The color of the piece being placed.
        int x -- The x-coordinate of the Gamepiece center.
        int y -- The y-coordinate o the Gamepiece center.
        '''
        # Get center of square
        x, y = self.squares[location].calc_center()
        # Initialize a Gamepiece object with location and color
        piece = GamePiece(location, color, x, y)
        # Add to self.pieces in location
        self.pieces[location] = piece
        # Draw piece on the board with Gamepiece.draw_tile
        piece.draw_tile()


class Square:
    '''Represents a square on the Othello board.'''

    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y
        self.size = SQUARE
        self.center = self.calc_center()

    ## SIGNATURE
    # calc_center :: Object => Integer[]
    def calc_center(self):
        '''
        Finds the coordinates of the square's center.
        Returns a tuple containing the coordinates.
        '''
        half = self.size // 2
        x = self.x + self.size - half
        y = self.y + self.size - half

        return (x, y)

    ## SIGNATURE
    # was_clicked :: (Object, Integer, Integer) => Boolean
    def was_clicked(self, x, y):
        '''
        Determines if this square was clicked on by the user.
        int x -- The x-coordinate of a mouse click.
        int y -- The y-coordinate of a mouse click.
        Returns a boolean value.
        '''
        inside = False
        if (self.x <= x <= self.x + self.size) \
                and (self.y <= y <= self.y + self.size):
            inside = True

        return inside
        
class GamePiece:
    '''GamePiece represents a single playing piece in Othello.'''

    def __init__(self, location, color, center_x, center_y):
        self.location = location
        self.color = color
        self.x = center_x
        self.y = center_y

    ## SIGNATURE
    # draw_tile :: Object => Void
    def draw_tile(self):
        '''
        Draws an Othello piece on the game board using the global Turtle object.
        str color -- The color of the piece being placed.
        Nothing returned
        '''
        othello.penup()
        othello.goto(self.x, self.y)
        othello.pendown()
        othello.dot(RADIUS, self.color)

    ## SIGNATURE
    # flip :: Object => Void
    def flip(self):
        '''
        If the piece is white, changes it to black. If the piece is black, 
        changes it to white.
        Nothing returned
        '''
        if self.color == "white": 
            self.color = "black"
        elif self.color == "black":
            self.color = "white"

        self.draw_tile()


#### Game play ####
if __name__ == "__main__":
    board = GameBoard(4)
    
    turtle.done()