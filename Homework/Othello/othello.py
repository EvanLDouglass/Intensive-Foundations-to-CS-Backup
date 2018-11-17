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
        assert type(n) == int, "n must be an integer."
        assert n >= 4, "n must be greater than or equal to 4."
        assert n % 2 != 1, "n must be even."
        self.n = n

        self.size = SQUARE * n
        self.turn = "black"         # The user will go first and is assigned the black pieces

        # Game state tracking attributes
        self.pieces = [None for location in range(n*n)]
        self.black = 0
        self.white = 0
        start = -n * SQUARE // 2     # The x & y coordinate of the first square
        self.squares = self.init_squares(start)

        # Draw the empty board
        self.draw_board()

        # Draw the starting tiles
        self.draw_start_tiles()

        # Find first valid moves
        self.valid_moves = self.find_valid_moves()

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
        start_tiles = self.find_center_squares()
        for location in start_tiles:
            self.place(location)
            self.switch_turns()

    ## SIGNATURE
    # switch_turns :: Object => Void
    def switch_turns(self):
        '''
        Changes the turn from black to white or white to black.
        '''
        if self.turn == "white":
            self.turn = "black"
        elif self.turn == "black":
            self.turn = "white"

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
        # Positioned in an order to make drawing the start pieces simpler
        # see draw_start_tiles
        return (ul, ur, lr, ll)
    
    ## SIGNATURE
    # place :: (Object, Integer, String) => Void
    def place(self, location):
        '''
        Initializes and draw a Gamepiece object on the Othello board at the given 
        location and with the given color.
        int location -- An index representing a square on the board, 0 to (n*n)-1.
        '''
        assert type(location) == int, "location must be an integer"
        assert 0 <= location < self.n*self.n, "location must be within the size of the board"

        # Get center of square
        x, y = self.squares[location].calc_center()

        # Draw a new tile
        piece = GamePiece(location, self.turn, x, y)
        piece.draw_tile()

        # Track the new tile
        self.pieces[location] = piece
        if self.turn == "white":
            self.white += 1
        elif self.turn == "black":
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
    # find_winner :: Object => (String, String)
    def find_winner(self):
        '''
        Calculates the winner based on the number of black and white tiles
        on the board.
        Returns two strings, the first announces the winner, the second 
        describes the score.
        '''
        # Determine message to display
        if self.white > self.black:
            message = "White wins!"
        elif self.black > self.white:
            message = "Black wins!"
        else:
            message = "You tied!"
        
        score = "black: " + str(self.black) + ", white: " + str(self.white)

        return message, score

    ## SIGNATURE
    # announce_winner :: Object => Void
    def announce_winner(self):
        '''
        Determines and announces the winner of the current game to the user.
        '''
        message, score = self.find_winner()

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
    # choose_move :: Object => Integer
    def choose_move(self):
        '''
        This function is used by the computer player to decide what move to 
        make. It searches for the valid move that will capture the most tiles.
        Returns an integer representing the location of a square, or -1 if
        no valid move exists.
        '''
        keys = self.valid_moves.keys()

        key = -1
        length = 0
        for k in keys:
            l = len(self.valid_moves[k])
            if l > length:
                length = l
                key = k
        return key

    ## SIGNATURE
    # find_valid_moves :: Object => {Integer: Integer[]}
    def find_valid_moves(self):
        '''
        Determines which squares are valid moves based on the current state of 
        the game and which tiles can be flipped from those moves.
        '''
        moves = {}
        for square in self.squares:
            # Find the tiles that could be flipped from there
            can_capture = self.all_can_capture(square.location)

            # If the list is not empty
            if can_capture:
                # Add list of tiles to valid_moves
                moves[square.location] = can_capture

        return moves

    ## SIGNATURE
    # all_can_capture :: (Object, Integer) => Integer[]
    def all_can_capture(self, location):
        '''
        Finds all of the tiles that can be captured from the given location.
        int location -- An integer identifying a square on the board.
        Returns a list of integers representing locations.
        '''
        assert type(location) == int and 0 <= location < self.n**2,\
            "location must be a valid board index"

        square = self.squares[location]

        # If the square is not empty
        if not square.is_empty(self.pieces):
            # Return an empty list -> not a valid move
            return []

        # The square is empty
        else:
            captured = []

            # Check in each direction around the square
            for direction in ("n", "ne", "e", "se", "s", "sw", "w", "nw"):

                # Find the locations of tiles that can be captured
                captured_in_direction = self.can_capture_in_direction(location, direction)
                # Add them to the total captured
                captured += captured_in_direction
            
            return captured

    ## SIGNATURE
    # can_capture_in_direction :: (Object, Integer, String) => Integer[]
    def can_capture_in_direction(self, location, direction):
        '''
        Finds tiles that can be captured from the given location in the given direction.
        int location -- An integer identifying a square on the board.
        str direction -- The direction to look in. Can be one of: n, ne, e, se, s, sw, w, nw
        Returns a list of integers representing locations.
        '''
        assert type(location) == int and 0 <= location < self.n**2,\
            "location must be a valid board index"
        assert direction in ("n", "ne", "e", "se", "s", "sw", "w", "nw"),\
            "direction must be one of n, ne, e, se, s, sw, w, nw"

        captured = []

        # Set an increment based on direction
        # inc can be negative or positive
        inc = self.set_increment(direction)

        # Set a max/min value for incrementing
        end = self.set_max_min(location, direction)

        # Ensure the stop in range includes end
        if inc <= 0:
            end -= 1
        else:
            end += 1

        # Get first potential opponent location
        nxt = location + inc

        # While the next location is not above/below max/min
        for loc in range(nxt, end, inc):
            piece = self.pieces[loc]
            if piece == None:
                # If there is no piece there
                # Return empty list because nothing can be captured 
                return []

            # If the next location has an opponent's tile
            elif piece.color != self.turn:
                # Append tile to list
                captured.append(piece)

            # If the next location has own tile, 
            elif piece.color == self.turn:
                captured.append(piece)
                break

            loc += inc
        
        # The while loop can append opponent tiles that can't be captured
        # if it reaches the end of the board and only encountered opponent tiles.
        # A final test is needed to ensure the last tile belongs to the 
        # current player
        if len(captured) > 0 and captured[-1].color == self.turn:
            # remove own tile as a captured tile before returning
            return captured[:-1]
        else:
            return []

    ## SIGNATURE
    # set_increment :: (Object, String) => Integer
    def set_increment(self, direction):
        '''
        Determines an appropriate increment for moving from one square 
        location to the next in the given direction.
        str direction -- The direction to look in. Can be one of:
        n, ne, e, se, s, sw, w, nw
        Returns an integer increment value
        '''
        assert direction in ("n", "ne", "e", "se", "s", "sw", "w", "nw"),\
            "direction must be one of n, ne, e, se, s, sw, w, nw"

        if direction == "n":
            inc = self.n
        elif direction == "s":
            inc = -self.n
        elif direction == "e":
            inc = 1
        elif direction == "w":
            inc = -1
        elif direction == "ne":
            inc = self.n + 1
        elif direction == "nw":
            inc = self.n - 1
        elif direction == "se":
            inc = -(self.n - 1)
        elif direction == "sw":
            inc = -(self.n + 1)

        return inc

    ## SIGNATURE
    # set_max_min :: (Object, Integer, String) => (String, Integer)
    def set_max_min(self, location, direction):
        '''
        For the given location, determines the maximum or minimum square 
        location along the given direction that is still on the board.       
        int location -- An integer identifying a square on the board.
        Returns the min or max square location along direction that is 
        still on the board.
        '''
        assert type(location) == int and 0 <= location < self.n**2,\
            "location must be a valid board index"
        assert direction in ("n", "ne", "e", "se", "s", "sw", "w", "nw"),\
            "direction must be one of n, ne, e, se, s, sw, w, nw"

        row_num = location // self.n    # from 0 to n-1
        row_start = row_num * self.n    # first index in row
        max_steps = self.n - 1          # squares from first-in-row to last-in-row
        row_end = row_start + max_steps # last index in row
        board_max = self.n**2 - 1       # maximum index on board
        board_min = 0                   # lowest index on board

        # Instead of using a single variable for all conditions I've 
        # used two, a max and min, because it helps make clear
        # which direction the iteration will have to go for each case.
        # A conditional statement determines which is returned.
        mx = None
        mn = None

        if direction == "n":
            # Moving straight up
            mx = board_max
        elif direction == "s":
            # Moving straight down
            mn = board_min

        elif direction == "e":
            # Moving right
            # max = max in row
            mx = row_end
        elif direction == "w":
            # Moving left
            # min = first in row
            mn = row_start

        elif direction == "ne":
            # Viewed as a 2D grid, the number of steps to get to the right
            # edge is also the number of steps to take up from the edge
            steps = max_steps - (location % self.n)
            mx = row_end + (steps * self.n)
            # Sometimes this is over the max board index
            if mx > board_max:
                mx = board_max
        elif direction == "se":
            # Same logic as northeast, but downwards
            steps = max_steps - (location % self.n)
            mn = row_end - (steps * self.n)
            if mn < board_min:
                mn = board_min
        
        # Same logic as last set, but backwards
        elif direction == "nw":
            steps = location - row_start
            mx = row_start + (steps * self.n)
            if mx > board_max:
                mx = board_max
        elif direction == "sw":
            steps = location - row_start
            mn = row_start - (steps * self.n)
            if mn < board_min:
                mn = board_min

        if mx == None:
            return mn
        else:
            return mx

    ## SIGNATURE
    # flip_tiles :: (Object, Integer[]) => Void
    def flip_tiles(self, tile_list):
        '''
        Drives the flipping of opponent tiles after a move is made.
        int[] tile_list -- A list of all the index locations of tiles to be flipped.
        '''
        for tile in tile_list:
            self.flip_tile(tile.location)

    ## SIGNATURE
    # flip_tile :: (Object, Integer) = > Void
    def flip_tile(self, location):
        '''
        Changes the color of a single tile on the board and redraws it.
        int location -- The index location of the tile to be flipped.
        '''
        assert type(location) == int and 0 <= location < self.n**2,\
            "location must be a valid board index"

        piece = self.pieces[location]
        square = self.squares[location]

        # If the square in location is not empty
        if not square.is_empty(self.pieces):
            # Change the color of the piece
            piece.flip()

        # Increment/decrement self.black & self.white as needed.
        color = piece.color
        if color == "white":
            self.white += 1
            self.black -= 1
        elif color == "black":
            self.black += 1
            self.white -= 1

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
        # Get legal moves
        legal = self.valid_moves.keys()

        for square in self.squares:
            if square.was_clicked(x, y) and square.location in legal:
                # Draw a tile
                self.place(square.location)

                # Flip captured tiles
                to_flip = self.valid_moves[square.location]
                self.flip_tiles(to_flip)
                self.switch_turns()
                break
        
        # Get new valid moves
        self.valid_moves = self.find_valid_moves()

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
        assert type(location) == int and location >= 0, "location must be a non-negative integer"
        assert type(x) == int and type(y) == int, "x & y must be integers"
        self.location = location
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
        int location -- An index cooresponding to the square that this piece is placed in.
        str color -- The color of the piece. Either white or black.
        int center_x -- The x-coordinate of the piece's center.
        int center_y -- The y-coordinate of the piece's center.
        '''
        assert type(location) == int and location >= 0,\
        "location must be a non-negative integer"
        assert color == "black" or color == "white",\
        "color must be 'black' or 'white'"
        assert type(center_x) == int and type(center_y) == int,\
        "x & y values must be integers"

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
        '''
        othello.penup()
        othello.goto(self.x, self.y)
        othello.pendown()
        othello.dot(RADIUS, self.color)

    ## SIGNATURE
    # change_color :: Object => Void
    def change_color(self):
        '''
        Simply changes the objects color from black to white, or 
        from white to black.
        '''
        if self.color == "white": 
            self.color = "black"
        elif self.color == "black":
            self.color = "white"

    ## SIGNATURE
    # flip :: Object => Void
    # This method not used in part 1 and not in testing.txt
    def flip(self):
        '''
        If the piece is white, changes it to black. If the piece is black, 
        changes it to white.
        '''
        self.change_color()
        self.draw_tile()

    ## SIGNATURE
    # __repr__ :: Object => String
    def __repr__(self):
        return self.color + " @ " + str(self.location)



#### Game play ####
if __name__ == "__main__":
    board = GameBoard(8)
    turtle.done()
    