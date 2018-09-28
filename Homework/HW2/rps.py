# CS5001
# HW2: Rock, Paper, Scissors
# Evan Douglass

import random

#### Purpose
# Runs a rock, paper, scissors game played between a user and the computer.
#
#### Signature
# rps :: () => String
#
#### Template
# def rps():
#   void
#
#### Examples
# Human: R, Computer: S => Rock breaks scissors! You are a champion!!!
# Human: P, Computer: S => Scissors cut paper! You loose, the machines are rising!!!
# Human: S, Computer: S => WE HAVE A TIE!!! What a game we've seen here tonight!
# Human: Hello, Computer: R => I don't know what Hello even is! DISQUALIFIED!!!
# 
def rps():
    ### Welcome message
    print('Welcome to RSP Human vs Computer EPIC SHOWDOWN...')
    print('Ladies and gentelmen...')
    print("It's... TIIMMMEEE!!!")
    print()
    print('In this corner we have a human being, warm blooded and full of emotions.')
    print('And in this corner we have a cold, calculating MACHINE.')
    print()
    print('Now...')
    print('LETS GET READY TO RRRRUUUUUUUMMMMMMMMMMMBBBLLLLLLLLLLEEEEEEEE!!!!!!!')
    print()

    ### User input
    print('The human will go first...')
    # Save unmodified response in case of disqualification
    h_choice_original = input('CHOOSE! - R, P or S\n')
    h_choice = h_choice_original.upper()
    # Input validation
    if h_choice == 'ROCK':
        h_choice = 'R'
    elif h_choice == 'PAPER':
        h_choice = 'P'
    elif h_choice == 'SCISSORS':
        h_choice = 'S'
    
    if h_choice == 'R' or h_choice == 'P' or h_choice == 'S':
        # Do nothing if valid choice
        pass
    else:
        # Empty string will be False in validity test under 'Choose winner' section
        h_choice = ''

    ### Computer selection
    c_choice = random.randint(1, 3)
    if c_choice == 1:
        c_choice = 'R'
    elif c_choice == 2:
        c_choice = 'P'
    else:  # choice == 3
        c_choice = 'S'
    
    ### Choose winner
    if h_choice:
        # Valid user input
        print('And the computer chooses...', c_choice + '!!!')
        print()

        rock_win = 'Rock breaks scissors!'
        paper_win = 'Paper covers rock!'
        scissors_win = 'Scissors cut paper!'
        human_win = 'You are a champion!!!'
        comp_win = 'You loose, the machines are rising!!!'

        if h_choice == c_choice:
            print("WE HAVE A TIE!!! What a game we've seen here tonight!")
        elif h_choice == 'R' and c_choice == 'P':
            print(paper_win, comp_win)
        elif h_choice == 'R' and c_choice == 'S':
            print(rock_win, human_win)
        elif h_choice == 'P' and c_choice == 'R':
            print(paper_win, human_win)
        elif h_choice == 'P' and c_choice == 'S':
            print(scissors_win, comp_win)
        elif h_choice == 'S' and c_choice == 'R':
            print(rock_win, comp_win)
        else:  # h_choice == 'S' and c_choice == 'P'
            print(scissors_win, human_win)

    # Input not valid, end game
    else:
        print("I don't know what", h_choice_original, "even is! DISQUALIFIED!!!")
    

# Run rps
rps()
