# Import random
import random

# Implement board
# The board will be generated automatically in a 5x5 layout. 
class Board:
    """
    Creates a class of Board with a width and height of 5.
    """
    def __init__(self, board):
        self.board = board
    
    def play_board(self):
        """
        Creates the board. Works with the run_game function to work out how
        many rows it needs to connect with. 
        """
        print("\n  A B C D E")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1
    
    def letter_to_number():
        """
        Converts the letter to a number and returns it.
        """
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
        for i in range(3):
            self.row, self.col = random.randint(0, 4), random.randint(0, 4)
            while self.board[self.row][self.col] == "X":
                self.row, self.col = random.randint(0, 4), random.randint(0, 4)
            self.board[self.row][self.col] = "X"
        return self.board
    
    def get_user_guess(self):
        """
        This inputs the user for their guesses of where the ship could be.
        If it isn't correct it reruns the function till an appropriate
        guess is made.
        """
        try:
            user_row = int(input("\nType a number between 1-5: "))
            user_column = input("Type a letter from A-E: ").upper().strip()
            return user_row - 1, Board.letter_to_number()[user_column]
        except ValueError and KeyError:
            print("Not a valid coordinate. Please try again.")
            return Ship.get_user_guess(self)

# Implement new game
def run_game():
    """
    Begins loading the players board on screen and generates a computer board
    in the background which the user will be guessing from.
    """
    computer_board = Board([[" "] * 5 for i in range(5)])
    user_board = Board([["~"] * 5 for i in range(5)])
    Ship.computer_ships(computer_board)

    turns = 10
    while turns > 0:
        Board.play_board(user_board)
        # Uncomment the line below to show the computers board
        Board.play_board(computer_board)

        # Gets the users guess
        user_row_input, user_col_input = Ship.get_user_guess(object)

        # Checks the user input to see if a ship was hit
        if computer_board.board[user_row_input][user_col_input] == "X":
            print("You sunk a battleship!")
            user_board.board[user_row_input][user_col_input] = "O"
        else:
            print("\nYou missed!")
            user_board.board[user_row_input][user_col_input] = "-"
            turns -= 1
            print(f"You have {turns} remaining!")

        # Checks to see if user has already guessed the position

run_game()