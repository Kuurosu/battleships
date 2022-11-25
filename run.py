# Import random
import random

# Implement score
# Both the computer and the user will start at a score of 0. This will be
# incremented by 1 for each battleship destroyed by the corresponding player
scores = {"computer": 0, "player": 0}
print(scores)

# Implement board
# The board will be generated automatically in a 5x5 layout. 
class Board:
    """
    Creates a class of Board with a width and height of 5.
    """
    def __init__(self, board):
        self.board = board
    
    def play_board(self):
        print("  1 2 3 4 5")
        row_number = 1
        for row in self.board:
            print(row_number, "|".join(row))
            row_number += 1

def board_load():
    print("\nComputer's side\n")
    computer_board = Board(["~"] * 5 for i in range(5))
    Board.play_board(computer_board)
    print("\nYour side\n")
    player_board = Board(["~"] * 5 for i in range(5))
    Board.play_board(player_board)

# Implement random int
# A function will be created to handle the computer's choice for the 
# integers it will choose. 
def computer_ships():
    """
    Randomly places the computers ships on the map within the game area.
    """
    ship = 0
    while ship < 3:
        ship_row = random.randint(1, 5)
        ship_col = random.randint(1, 5)
        ship_coords = [ship_row, ship_col]
        SHIP_PLACEMENT.append(ship_coords)
        ship += 1
    print(SHIP_PLACEMENT)

# Implement board guess
# This handles the inputs from the user for which row and column they are 
# choosing to play the game
def get_user_input():
    user_ship_placement = []
    row_guess = 0
    col_guess = 0
    while True:
        print("\nWhat row would you like your first ship?\n")
        try:
            user_row = int(input("Please type a number from 1-5: "))
            if user_row < 6 and user_row > 0:
                user_append_row = user_row - 1
                user_ship_placement.append(user_append_row)
                break
            else:
                print("\nThat is not a number within 1-5")
                continue
        except ValueError:
            print("That is not a number. Please try again.\n")
            continue
    while True:
        print("\nWhat column would you like your first ship?\n")
        try:
            user_col = int(input("Please type a number from 1-5: "))
            if user_col < 6 and user_col > 0:
                user_append_col = user_col - 1
                user_ship_placement.append(user_append_col)
                break
            else:
                print("\nThat is not a number within 1-5")
                continue
        except ValueError:
            print("That is not a number. Please try again.\n")
            continue

    print(user_ship_placement)



# Implement check coords
# After the computer and the player has made a choice, it will be passed
# into a coord check to see if it is:
# Valid inside the game area.
# Hasn't been previously chosen. 

# Implement board population
# This handles the board after relevant choices have been made and stores
# it for future choices to show the player what has currently already been
# chosen

# Implement game logic

SHIP_PLACEMENT = []

# Implement new game
def run_game():
    board_load()
    computer_ships()
    get_user_input()
    

run_game()