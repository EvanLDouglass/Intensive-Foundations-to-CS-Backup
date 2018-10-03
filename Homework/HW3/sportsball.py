# CS5001
# HW 3: Sports Ball
# Evan Douglass

record = [
    'W', 'W', 'W', 'W', 'L', 'W', 'W', 'W', 'L', 'W',
    'W', 'W', 'W', 'W', 'W', 'W', 'W', 'L', 'L', 'L',
    'W', 'W', 'L', 'L', 'W', 'W', 'L', 'W', 'L', 'W',
    'W', 'W', 'L', 'L', 'W', 'L', 'W', 'W', 'L', 'L',
    'W', 'W', 'L', 'W', 'W', 'W', 'W', 'L', 'W', 'W',
    'L', 'W', 'W', 'W', 'L', 'L', 'W', 'W', 'W', 'W',
    'L', 'L', 'W', 'L', 'W', 'W', 'W', 'W', 'W', 'L',
    'L', 'L', 'W', 'L', 'W', 'W', 'L', 'W', 'W', 'W',
    'W', 'L', 'W', 'L', 'W', 'W', 'W', 'W', 'W', 'W',
    'W', 'W', 'W', 'W', 'L', 'W', 'W', 'W', 'W', 'L'
]

score = [
    4, 1, 3, 2, 7, 4, 3, 10, 8, 14,
    7, 6, 7, 10, 3, 10, 9, 8, 7, 0,
    1, 3, 4, 5, 3, 6, 4, 10, 6, 5,
    5, 5, 6, 6, 2, 6, 5, 3, 5, 5,
    5, 3, 6, 5, 6, 6, 5, 4, 4, 3,
    6, 8, 1, 8, 8, 6, 2, 3, 5, 9,
    6, 7, 2, 0, 4, 2, 2, 6, 5, 2,
    6, 0, 9, 2, 1, 9, 14, 2, 5, 9,
    9, 4, 1, 11, 1, 4, 11, 3, 10, 15,
    7, 5, 8, 4, 6, 7, 6, 5, 1, 0
]

#### Purpose
# Calculates the number of wins and losses for a given list of wins and losses.
#
#### Signature
# get_record :: String[] => (Integer, Integer)
#
#### Examples
# get_record(['W', 'W', 'L', 'W', 'W']) => (4, 1)
# get_record(['W', 'W', 'L', 'L']) => (2, 2)
# get_record(['W']) => (1, 0)
#
def get_record(record_list):
    '''Calculates the number of wins and losses in record_list.

    record_list -- A list with values 'W' or 'L' (can be lowercase too).
    Returns a tuple of integers with form (num_wins, num_losses)
    '''
    wins = 0
    losses = 0
    for i, game in enumerate(record_list):
        # String constructor used to protect against numerical input
        if str(game).upper() == "W":
            wins += 1
        elif str(game).upper() == "L":
            losses += 1
        else:
            # Invalid entry causes an exception
            raise ValueError("The item " + str(game) + " at index " + str(i) \
                             + " was not 'W' or 'L'")
    
    return (wins, losses)


#### Purpose
# Gets an average from a list of numbers. Used here to get the average score
# of a given sports team over a season.
#
#### Signature
# avg :: Integer[] => Float
#
#### Examples
# avg([1, 2, 3, 4, 5]) => 3.0
# avg([4, 5, 6, 7]) => 5.5
# avg([-9, 3, 0, 99]) => 23.25
#
def avg(number_list):
    '''Gets an average from a list of numbers.

    number_list -- A list of numbers.
    Returns the average of the numbers as a float.
    '''
    total = 0
    for num in number_list:
        total += num
    
    return total / len(number_list)


#### Purpose
# Counts the number of games in which a team has scored a given number of
# points. This implementation takes advantage of the eval built-in function
# that evaluates a string as a python expression. This allows for a string
# parameter that represents a boolean test (default: "==") to be used
# dynamically instead of using several if/else statements and blocks of
# basically the same code in each statement. Due to the likelyhood of
# a syntax error in the eval function, input validation on the bool_test
# parameter is performed.
#
#### Signature
# count_games :: (Integer, Integer[], String) => Integer
#
#### Examples
# count_games(10, [1, 5, 10, 10], "==") => 2
# count_games(9, [4, 2, 9], "<") => 2
# count_games(3, [2, 3, 5], ">=") => 2
#
def count_games(score, score_list, bool_test="=="):
    '''Conducts a count of scores in a list based on a boolean test.

    score -- The reference score to test.
    score_list -- A list of scores to test against.
    bool_test -- A string representation of a boolean test.
        Must be one of "==", ">", "<", ">=", "<=", "!="; defaults to "==".
    Returns a count of positive matches to the score_list based on the type
    of test and reference score.
    '''
    valid_strings = ["==", ">", "<", ">=", "<=", "!="]

    # Ensure bool_string is of type str and has no whitespace
    bool_test = str(bool_test).replace(" ", "")

    # Throw an error if the string is not a valid choice
    if bool_test not in valid_strings:
        raise ValueError(bool_test + " not in " + str(valid_strings))

    # Perform the counting
    total = 0
    bool_expression = "num" + bool_test + "score"  # becomes a variable comparison in eval
    for num in score_list:
        if eval(bool_expression):  # for example: num==score
            total += 1
    
    return total


#### Purpose
# Counts the number of games in which a team has scored a given number of
# points in a winning game. This implementation takes advantage of
# the eval built-in function that evaluates a string as a python expression. 
# This allows for a string parameter that represents a boolean test 
# (default: "==") to be used dynamically instead of using several if/else 
# statements and blocks of basically the same code in each statement. Due to
# the likelyhood of a syntax error in the eval function, input validation on
# the bool_test parameter is performed.
#
#### Signature
# count_games_won :: (Integer, Integer[], String[], String) => Integer
#
#### Examples
# count_games_won(10, [1, 5, 10, 10], ["L", "W", "W", "L"], "==") => 1
# count_games_won(9, [4, 2, 9], ["L", "W", "W"], "<") => 1
# count_games_won(3, [2, 3, 5], ["L", "L", "L"], ">=") => 0
#
def count_games_won(score, score_list, record_list, bool_test="=="):
    '''Conducts a count of scores in a list based on a boolean test and 
    whether the corresponding record is a win.

    score -- The reference score to test.
    score_list -- A list of scores to test against.
    record_list -- A list of records in the form of "W" or "L"
    bool_test -- A string representation of a boolean test. Must be one
        of "==", ">", "<", ">=", "<=", "!="; defaults to "==".
    Returns a count of positive matches to the score_list based on the type
    of test and reference score.
    '''
    valid_strings = ["==", ">", "<", ">=", "<=", "!="]

    # Lists must be of equal length
    if len(score_list) != len(record_list):
        raise ValueError("Given lists must be of equal length.")

    # Ensure bool_string is of type str and has no whitespace
    bool_test = str(bool_test).replace(" ", "")

    # Throw an error if the string is not a valid choice
    if bool_test not in valid_strings:
        raise ValueError(bool_test + " not in " + str(valid_strings))

    # Perform the counting
    total = 0
    bool_expression = "num" + bool_test + "score"    # becomes a variable comparison in eval
    for i, num in enumerate(score_list):
        # Ensure the result of each game is a string and uppercase
        result = str(record_list[i]).upper()
        if result == "W" and eval(bool_expression):  # for example: num==score
            total += 1
    
    return total


#### Purpose
# Counts the number of games in which a team has scored a given number of
# points in a losing game. This implementation takes advantage of
# the eval built-in function that evaluates a string as a python expression. 
# This allows for a string parameter that represents a boolean test 
# (default: "==") to be used dynamically instead of using several if/else 
# statements and blocks of basically the same code in each statement. Due to
# the likelyhood of a syntax error in the eval function, input validation on
# the bool_test parameter is performed.
#
#### Signature
# count_games_lost :: (Integer, Integer[], String[], String) => Integer
#
#### Examples
# count_games_lost(10, [1, 5, 10, 10], ["L", "W", "W", "L"], "==") => 1
# count_games_lost(9, [4, 2, 9], ["L", "L", "W"], "<") => 2
# count_games_lost(3, [2, 3, 5], ["L", "L", "L"], ">=") => 2
#
def count_games_lost(score, score_list, record_list, bool_test="=="):
    '''Conducts a count of scores in a list based on a boolean test and 
    whether the corresponding record is a loss.

    score -- The reference score to test.
    score_list -- A list of scores to test against.
    record_list -- A list of records in the form of "W" or "L"
    bool_test -- A string representation of a boolean test. Must be one
        of "==", ">", "<", ">=", "<=", "!="; defaults to "==".
    Returns a count of positive matches to the score_list based on the type
    of test and reference score.
    '''
    valid_strings = ["==", ">", "<", ">=", "<=", "!="]

    # Lists must be of equal length
    if len(score_list) != len(record_list):
        raise ValueError("Given lists must be of equal length.")

    # Ensure bool_string is of type str and has no whitespace
    bool_test = str(bool_test).replace(" ", "")

    # Throw an error if the string is not a valid choice
    if bool_test not in valid_strings:
        raise ValueError(bool_test + " not in " + str(valid_strings))

    # Perform the counting
    total = 0
    bool_expression = "num" + bool_test + "score"    # becomes a variable comparison in eval
    for i, num in enumerate(score_list):
        # Ensure the result of each game is a string and uppercase
        result = str(record_list[i]).upper()
        if result == "L" and eval(bool_expression):  # for example: num==score
            total += 1
    
    return total


#### Main program ####
# Win/Loss record
wins, losses = get_record(record)
print("The team's win/loss record is", wins, "wins and", losses, "losses.")

# Average score per game
print("Their average score per game over the season was {} points.".format(avg(score)))

# Games with a score of 0
num_zero = count_games(0, score)
print("They scored 0 points in", num_zero, "games", end=" ")

# Games with a score of >= 10
num_ten_plus = count_games(10, score, ">=")
print("and at least 10 points in", num_ten_plus, "games.")

# Wins with score of 1
wins_one = count_games_won(1, score, record)
print("They won", wins_one, "games with a score of 1", end = " ")

# Losses with score of at least 10
losses_ten_plus = count_games_lost(10, score, record, ">=")
print("and lost", losses_ten_plus, "games with a score of at least 10.")
