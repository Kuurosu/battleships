# Import random
import random

# Implement turns
# The player will have a limited amount of turns to hit the computer's 
# battleships
turn = 10
print(turn)

# Implement board
# The board will be generated automatically in a 5x5 layout. 
class Board:
    """
    Creates a class of Board with a width and height of 5.
    """
    def __init__(self, board):
        self.board = board
    
    def play_board(self):
        print("  A B C D E")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1
    
    def letter_to_number():
        list_of_letter = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return list_of_letter

# Implement random int
# A function will be created to handle the computer's choice for the 
# integers it will choose. 
class Ship:
    def __init__(self, board):
        self.board = board

    def computer_ships(self):
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
        return SHIP_PLACEMENT
    
    def get_user_guess(self):
        try:
            user_row = input("Type a number between 1-5: ")
            user_column = input("Type a letter from A-E: ").upper()
            return user_row, Board.letter_to_number()[user_column]
        except ValueError and KeyError:
            print("Not a valid coordinate. Please try again.")
            return Ship.get_user_guess(self)

SHIP_PLACEMENT = []

# Implement new game
def run_game():
    computer_board = Board([["~"] * 5 for i in range(5)])
    Ship.computer_ships(computer_board)

    
run_game()