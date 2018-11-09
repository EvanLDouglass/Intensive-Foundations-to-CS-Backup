'''
The othello module is used to play the game Othello. It is the final 
project for CS5001 at Northeastern University.

Author: Evan Douglass
'''

import turtle

class GameBoard:
    '''The GameBoard class contains the functionality of a board for the game Othello.'''

    # Class constants
    SQUARE = 50     # pixels

    def __init__(self, n):
        # The user will go first and is assigned the black pieces
        self.turn = "black"
        self.window = turtle.Screen()
        self.othello = turtle.Turtle()
        self.board = [None for square in range(n*n)]
        self.draw_board(n)

    ## SIGNATURE
    # draw_board :: Integer => Void
    def draw_board(self, n):
        '''
        Draws an nxn board with a green background.
        int n -- The number of squares on one side of the board.
        '''
        # Setup window
        self.window.setup(n * self.SQUARE + self.SQUARE, n * self.SQUARE + self.SQUARE)
        self.window.screensize(n * self.SQUARE, n * self.SQUARE)
        self.window.bgcolor("white")
        self.window.title("Othello")

        # Create turtle to draw the board
        self.othello.penup()
        self.othello.speed(0)
        self.othello.hideturtle()

        # Line color is black, fill color is green
        self.othello.color("black", "forest green")

        # Move the turtle to the lower left corner
        corner = -n * self.SQUARE / 2
        self.othello.setposition(corner, corner)

        # Draw the green background
        self.othello.begin_fill()
        for i in range(4):
            self.othello.pendown()
            self.othello.forward(self.SQUARE * n)
            self.othello.left(90)
        self.othello.end_fill()

        # Draw the horizontal lines
        for i in range(n + 1):
            self.othello.setposition(corner, self.SQUARE * i + corner)
            self.draw_lines(self.othello, n)

        # Draw the vertical lines
        self.othello.left(90)
        for i in range(n + 1):
            self.othello.setposition(self.SQUARE * i + corner, corner)
            self.draw_lines(self.othello, n)
        
        # TODO: Draw the starting pieces

    ## SIGNATURE
    # draw_lines :: (Object, Integer) => Void
    def draw_lines(self, turt, n):
        '''
        Draws n vertical lines on an othello board. A helper function for draw_board.
        Turtle turt -- A Turtle object.
        int n -- The number of squares to draw on the board in one direction.
        '''
        turt.pendown()
        turt.forward(self.SQUARE * n)
        turt.penup()

board = GameBoard(8)
turtle.done()