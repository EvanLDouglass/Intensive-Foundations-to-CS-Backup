# CS5001
# Evan Douglass
# Lab 7: turtle module

import turtle

colors = ['yellow', 'green', 'blue', 'orange', 'red', 'black', 'purple', 'magenta', 'pink', 'cyan']
mod = len(colors)
turt = turtle.Turtle()

def loop_draw():
    index = 0
    for dist in range(10, 401, 10):
        turt.color(colors[index])
        turt.right(144)
        turt.forward(dist)
        index = (index+1) % mod
    
    turtle.done()

def recursive_draw(longest_line=400, index=0, increment=10, decrement=10):
    if longest_line == 0:
        turtle.done()
    else:
        turt.color(colors[index])
        turt.right(144)
        turt.forward(increment)
        recursive_draw(longest_line-decrement, (index+1)%mod, increment+10)
        


# Show graphics
#loop_draw()
recursive_draw()