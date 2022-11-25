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


# Implement random int
# A function will be created to handle the computer's choice for the 
# integers it will choose. 

def computer_random_int():
    """
    Using random, the function creates a random number from 0 through to 5.
    """
    computer_number = random.randint(0,5)
    return computer_number

# Implement check coords
# After the computer and the player has made a choice, it will be passed
# into a coord check to see if it is:
# Valid inside the game area.
# Hasn't been previously chosen. 

# Implement board population
# This handles the board after relevant choices have been made and stores
# it for future choices to show the player what has currently already been
# chosen
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
# def get_user_input():
#     while True:
#         if top_row < 6:
#             top_row = input("Type the column you'd like to place your ship: ").strip()
#             break

# Implement game logic

SHIP_PLACEMENT = []

# Implement new game
def run_game():
    print("\nComputer's side\n")
    computer_board = Board(["~"] * 5 for i in range(5))
    Board.play_board(computer_board)
    print("\nYour side\n")
    player_board = Board(["~"] * 5 for i in range(5))
    Board.play_board(player_board)
    computer_ships()
    

run_game()