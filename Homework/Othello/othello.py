'''
The othello module is used to play the game Othello. It is the final 
project for CS5001 at Northeastern University.

Author: Evan Douglass
'''

import turtle

#### Module constants and global variables ####
SQUARE = 50             # pixels
RADIUS = SQUARE - 10    # pixels

window = turtle.Screen()
othello = turtle.Turtle()


#### Classes ####
class GameBoard:
    '''
    The GameBoard class represents a board for the game Othello. It also 
    contains the functionality and logic allowing for gameplay.
    '''

    def __init__(self, n):
        '''
        Draws the starting board and sets up gameplay.
        int n -- The number of squares on one side of the board (it's length
        in squares).
        '''
        self.n = int(n)
        self.size = SQUARE * n
        self.turn = "black"         # The user will go first and is assigned the black pieces

        # Game state tracking attributes
        self.pieces = [None for location in range(n*n)]
        self.black = 0
        self.white = 0
        start = -n * SQUARE / 2     # The x & y coordinate of the first square
        self.squares = self.init_squares(start)

        # Draw the empty board
        self.draw_board()

        # Draw the starting tiles
        self.draw_start_tiles()

        # Set up mouse click event listener
        window.onclick(self.play)

    ## SIGNATURE
    # init_squares :: (Object, Integer) => Object
    def init_squares(self, corner):
        '''
        Populates the self.squares list.
        int corner -- A number representing the x & y coordinate of the 
        first square.
        Returns a list of Square objects
        '''
        corner = int(corner)
        lst = []
        index = 0
        # y-coordinates can continuously increase
        y_corner = corner
        for row in range(self.n):
            # x-coordinate values need to start over on each row
            x_corner = corner
            for column in range(self.n):
                # Add a square to the tracker list and increment values
                lst.append(Square(index, x_corner, y_corner))
                index += 1
                x_corner += SQUARE
            y_corner += SQUARE
        
        return lst

    ## SIGNATURE
    # draw_board :: Object => Void
    def draw_board(self):
        '''
        Draws an nxn board with a green background.
        '''
        # Ensure n is a valid number
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
            self.draw_line()

        # Draw the vertical lines
        othello.left(90)
        for i in range(self.n + 1):
            othello.setposition(SQUARE * i + corner, corner)
            self.draw_line()

    ## SIGNATURE
    # draw_line :: Object => Void
    def draw_line(self):
        '''
        Draws a line. this is a helper function for draw_board.
        '''
        othello.pendown()
        othello.forward(SQUARE * self.n)
        othello.penup()

    ## SIGNATURE
    # draw_start_tiles :: Object => Void
    def draw_start_tiles(self):
        '''
        Draws the four starting tiles on the board.
        '''
        # ur == upper right, ll == lower left, etc.
        ur, ul, lr, ll = self.find_center_squares()
        color = "white"
        # The order of the lower squares are switched here to get colors right
        for location in (ur, ul, ll, lr):
            self.place(location, color)

            if color == "white":
                color = "black"
            else:
                color = "white"
    
    ## SIGNATURE
    # draw_box :: Object => Void
    def draw_box(self):
        '''
        Draws a black box used to display the end-of-game text.
        '''
        # Box will cover the middle two rows across the whole window
        start_x = -self.size//2 - SQUARE//2
        start_y = -SQUARE
        width = self.size + SQUARE
        height = 2 * SQUARE

        # Set start
        othello.penup()
        othello.goto(start_x, start_y)
        othello.setheading(0)           # Move to the right first
        othello.pendown()

        # Draw
        othello.color("white", "#202020")
        othello.begin_fill()
        for half in range(2):
            othello.forward(width)
            othello.left(90)
            othello.forward(height)
            othello.left(90)
        othello.end_fill()

    ## SIGNATURE
    # find_center_squares :: Object => Integer[]
    def find_center_squares(self):
        '''
        Finds the four center starting squares on the board.
        Returns a tuple of ints representing the indexes of the four center 
        squares on the draw_board.
        '''
        # If n is even and the board grid is indexed from 0 to n*n
        # then the upper right center square can be found with the formula:
        # 0.5(n**2 + n)
        # The remaining squares can be found by subtracting from that result
        # 1, n, n+1 for upper left, lower right, and lower left respectively
        ur = int(0.5 * (self.n**2 + self.n))
        ul = ur - 1
        lr = ur - self.n
        ll = lr - 1
        return (ur, ul, lr, ll)
    
    ## SIGNATURE
    # place :: (Object, Integer, String) => Void
    def place(self, location, color):
        '''
        Initializes a Gamepiece object on the Othello board at the given 
        location and with the given color.
        int location -- An index representing a square on the board (0 to n*n).
        str color -- The color of the piece being placed.
        '''
        assert(location >= 0)
        assert(color=="white" or color=="black")

        # Ensure location is an integer
        location = int(location)

        # Get center of square
        x, y = self.squares[location].calc_center()

        # Draw a new tile
        piece = GamePiece(location, color, x, y)
        piece.draw_tile()

        # Track the new tile
        self.pieces[location] = piece
        if color == "white":
            self.white += 1
        elif color == "black":
            self.black += 1

    ## SIGNATURE
    # is_full :: Object => Boolean
    def is_full(self):
        '''
        Tests whether the board is full of tiles or not.
        Returns a boolean value.
        '''
        full = True
        for tile in self.pieces:
            # if any tile == None, the board is not full
            if tile == None:
                full = False
                break
        return full
    
    ## SIGNATURE
    # announce_winner :: Object => Void
    def announce_winner(self):
        '''
        Determines and announces the winner of the current game.
        '''
        # Determine message to display
        if self.white > self.black:
            message = "White wins!"
        elif self.black > self.white:
            message = "Black wins!"
        else:
            message = "You tied!"
        
        score = "black: " + str(self.black) + ", white: " + str(self.white)
        
        # Display textbox
        self.draw_box()
        
        # Display message
        othello.penup()
        othello.home()
        othello.color("white")
        othello.pendown()
        othello.write(message, align="center", font=("Georgia", 25, "bold", "underline"))
        print(message)

        # Display score
        othello.penup()
        othello.goto(0, -SQUARE//2)
        othello.pendown()
        othello.write(score, align="center", font=("Georgia", 16, "bold"))
        print(score)

    ## SIGNATURE
    # play :: (Object, Integer, Integer) => Void
    def play(self, x, y):
        '''
        This mehtod drives the game. It waits for a mouse click to occur and 
        if the click is in a valid location it places a tile of color 
        self.turn in that square. If the board is full, it announces a winner 
        and terminates, thus stopping the game.
        int x -- The mouse x position
        int y -- The mouse y position 
        '''
        # TODO: Search for legal moves

        for square in self.squares:
            if square.was_clicked(x, y) and square.is_empty(self.pieces):
                
                # Draw a tile
                self.place(square.location, self.turn)

                # Switch turns
                if self.turn == "white":
                    self.turn = "black"
                else:  # turn == black
                    self.turn = "white"
                break
        
        # When the board is full, announce a winner and finish the game
        if self.is_full():
            self.announce_winner()



class Square:
    '''
    Represents a single square on the Othello board.
    '''

    def __init__(self, location, x, y):
        '''
        int location -- An index representing the assigned number on the board
        of this square.
        int x -- The lower left x-coordinate of the square.
        int y -- The lower left y-coordinate of the square.
        Attributes representing the length of a side (size) and the center
        coordinates (center) of the square are also initialized.
        '''
        assert(location >= 0)
        self.location = int(location)
        self.x = int(x)
        self.y = int(y)
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
        if ((self.x < x < self.x + self.size)
                and (self.y < y < self.y + self.size)):
            inside = True

        return inside

    ## SIGNATURE
    # is_empty :: Object => Boolean
    def is_empty(self, state):
        '''
        Tests if the square contains a tile
        GamePiece[] state -- A list of GamePiece objects representing the 
        current board layout.
        Returns a boolean value.
        '''
        if state[self.location] == None:
            return True
        return False



class GamePiece:
    '''
    GamePiece represents a single piece, or tile, in Othello.
    '''

    def __init__(self, location, color, center_x, center_y):
        '''
        int location -- An index cooresponding to the square that this piece
        is placed in.
        str color -- The color of the piece. Either white or black.
        int center_x -- The x-coordinate of the piece's center.
        int center_y -- The y-coordinate of the piece's center.
        '''
        assert(location >= 0)
        assert(color == "black" or color == "white")
        self.location = int(location)
        self.color = color
        self.x = int(center_x)
        self.y = int(center_y)

    ## SIGNATURE
    # draw_tile :: Object => Void
    def draw_tile(self):
        '''
        Draws an Othello piece on the game board using the global Turtle object.
        str color -- The color of the piece being placed.
        '''
        othello.penup()
        othello.goto(self.x, self.y)
        othello.pendown()
        othello.dot(RADIUS, self.color)

    ## SIGNATURE
    # flip :: Object => Void
    # This method not used in part 1 and not in testing.txt
    def flip(self):
        '''
        If the piece is white, changes it to black. If the piece is black, 
        changes it to white.
        '''
        if self.color == "white": 
            self.color = "black"
        elif self.color == "black":
            self.color = "white"

        self.draw_tile()



#### Game play ####
if __name__ == "__main__":
    # All gameplay functionality is done within the GameBoard class
    board = GameBoard(4)
    turtle.done()
