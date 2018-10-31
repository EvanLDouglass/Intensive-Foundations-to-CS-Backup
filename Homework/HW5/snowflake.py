# CS5001
# Evan Douglass
# HW 5: snowflake.py
# Drawing a Koch Snowflake

import turtle

turt = turtle.Turtle()

## PURPOSE
# Recursively draws a Koch koch_curve.
## SIGNATURE
# koch_curve :: (Integer, Integer) => Void
def koch_curve(side_length, order):
    '''Recursively draws a Koch Curve
    
    int side_length - Size of one edge of the Koch Curve.
    int order - Layers of the Koch Curve to draw.
    '''
    # Base Case
    # When order is 0 => straight line
    if order == 0:
        turt.forward(side_length)
    
    # Recursive Case
    else:
        koch_curve(side_length/3, order-1)
        turt.left(60)
        koch_curve(side_length/3, order-1)
        turt.left(-120)
        koch_curve(side_length/3, order-1)
        turt.left(60)
        koch_curve(side_length/3, order-1)


## PURPOSE
# Draws a Koch Snowflake using Koch curves.
## SIGNATURE
# draw_snowflake :: Integer => Void
def draw_snowflake(sides, side_length, order):
    '''Draws a Koch Snowflake using Koch curves.

    int sides - The number of sides the snowflake should have.
    int side_length - Size of one edge of the Koch Curve.
    int order - Layers of the Koch Curve to draw.
    '''
    degrees = 360 / sides
    for side in range(sides):
        koch_curve(side_length, order)
        turt.right(degrees)


########## Testing Function ##########

## PURPOSE
# Tests draw_snowflake by drawing several rows of snowflakes of different
# side numbers, side lengths and orders.
## SIGNATURE
# draw_snowflakes :: () => Void
def draw_snowflakes():
    '''
    Tests draw_snowflake by drawing several rows of snowflakes of different
    side numbers, side lengths and orders.
    '''
    # Starting location on canvas.
    # Determined by guess and check
    x = -300
    y = 280

    ## Test orders
    # Position turtle
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    # Draw
    for order in range(4):
        draw_snowflake(3, 100, order)
        turt.penup()
        x += 150
        turt.goto(x, y)
        turt.pendown()
    
    ## Test sides
    # Position
    turt.penup()
    x, y = (-300, 100)
    turt.goto(x, y)
    turt.pendown()
    # Draw
    for side in range(1, 5):
        draw_snowflake(side, 100, 3)
        turt.penup()
        x += 150
        turt.goto(x, y)
        turt.pendown()
    
    ## Test side length
    # More complicated positioning made lists easier to manage than
    # adjusting arguments as range variables. Sizes goes backwards to make
    # use of canvas space.
    sizes = [200, 150, 100, 50]
    distances = [250, 200, 150, 100]
    # Position
    turt.penup()
    x, y = (-350, -100)
    turt.goto(x, y)
    turt.pendown()
    # Draw
    for index in range(4):
        draw_snowflake(3, sizes[index], 3)
        turt.penup()
        x += distances[index]
        turt.goto(x, y)
        turt.pendown()


if __name__ == '__main__':
    turt.speed(200)
    draw_snowflakes()
    turtle.done()
