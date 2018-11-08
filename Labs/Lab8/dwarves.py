# CS5001
# Lab 8: 7 Dwarves Facebook
# Evan Douglass

## SIGNATURE
# init :: () => Dictionary
def init():
    '''Initializes the application upon start.
    Returns a dictionary of the form, user: friend list
    '''
    try:
        data = {}
        with open("dwarves.txt", "r") as f:

            # Split lines and add user: friend_list to dictionary
            line = f.readline().strip()
            while line:
                lst = line.split()
                data[lst[0]] = lst[1:]

                line = f.readline().strip()
        
        return data
    
    except FileNotFoundError:
        # Print an error and halt program
        print("No such file exists. Please check the path and try again.")
        quit()


## SIGNATURE
# get_username :: () => String
def get_username(f_dict):
    '''Gets a valid username from the user.
    Dictionary f_dict - A dictionary containing users and their friends.
    '''
    users = f_dict.keys()

    user = input("Which of the 7 is loggin in?\n")
    print()  # Space for readability

    while user not in users:
        print("No such user, try again.")
        user = input("Which of the 7 is loggin in?\n")

    return user

## SIGNATURE
# menu :: () => Void
def menu():
    '''Prints a list of menu options for the user.'''
    
    menu = '''Choose from one of the options below.
    P: Print friends list
    U: Unfriend someone
    F: Add a new friend
    Q: Quit'''

    print(menu)


## SIGNATURE
# print_friends :: String => Void
def print_friends(user, f_dict):
    '''Prints a user's list of friends.
    str user - The current user.
    Dictionary f_dict - A dictionary containing users and their friends.
    '''
    # TODO: error handling - no such friend
    f_list = f_dict[user]
    for friend in f_list:
        print(friend)


## SIGNATURE
# add_friend :: (String, String) => Void
def add_friend(user, friend, f_dict):
    '''Adds a friend to the current user's friend list.
    str user - The current user.
    str friend - The friend to add.
    Dictionary f_dict - A dictionary containing users and their friends.
    '''
    # Get user's friend list and append new friend
    # Error handling done in get_username
    f_dict[user].append(friend)


## SIGNATURE
# unfriend :: (String, String) => Void
def unfriend(user, friend, f_dict):
    '''Removes a friend from the user's friend list.
    str user - The current user.
    str friend - The friend to add.
    Dictionary f_dict - A dictionary containing users and their friends.
    '''
    # Get user's friend list and remove friend
    try:
        f_dict[user].remove(friend)
    except ValueError:
        print(friend, "is not your friend.")


## SIGNATURE
# save :: Dictionary => Void
def save(f_dict):
    '''Save the active dictionary as a .txt file.
    Dictionary f_dict - A dictionary containing users and their friends.
    '''
    # Get list of users.
    users = f_dict.keys()
    # Open dwarves.txt and write each user with their friends on each line.
    with open("dwarves.txt", "w") as f:

        for user in users:
            f.write(user + " ")
            friends = f_dict[user]
            for friend in friends:
                f.write(friend + " ")
            f.write("\n")


def main():
    # Get dictionary of users and their friends
    app_data = init()

    # Get user
    user = get_username(app_data)
    menu()
    
    # Program loop
    while True:
        choice = input("\nEnter a command below.\n--> ").upper()

        if choice == "P":
            print_friends(user, app_data)
        elif choice == "U":
            print("Here are your friends:")
            print_friends(user, app_data)
            print()
            friend = input("Who do you want to unfriend?\n")
            unfriend(user, friend, app_data)
        elif choice == "F":
            friend = input("Who do you want to add as a friend?\n")
            add_friend(user, friend, app_data)
            print("Here is your updated friend list")
            print_friends(user, app_data)
        elif choice == "Q":
            save(app_data)
            break
        else:
            print("Not a valid choice, choose again.\n")


if __name__ == "__main__":
    main()