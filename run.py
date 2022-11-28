# Import random
import random


print("\nWelcome to Battleship!")
print("The aim is to guess where the opponent has hidden their ships.")
print("You choose the column by typing the letter of the column you'd like, and the row by the number. Then hit enter when you're ready to fire.")

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

    def user_ship_input(self):
        """
        Requests the user to enter the coordinates of where they would like to place their ships.
        """
        ship = 0
        while ship < 3:
            # try:
                # print("\nWhere would you like your first ship?")
                # self.user_ship_one_col = input("\nChoose a column from A-E: ").upper().strip()
                # if self.user_ship_one_col not in "ABCDE":
                #     print("It needs to be a letter within A-E")
                #     return Ship.user_ship_input(self)
                # self.user_ship_one_row = int(input("Type a number between 1-5: "))
                # self.user_ship_one_row - 1
                # self.user_ship_col_row = Board.letter_to_number()[self.user_ship_one_col]
                # self.board[self.user_ship_one_col][self.user_ship_one_row] = "@"
                # return self.board
            print("\nWhere would you like your first ship?")
            self.row = random.randint(0, 4) 
            self.col = input("Choose a column from A-E: ").upper().strip()
            if self.col not in "ABCDE":
                print("It needs to be a letter within A-E")
            self.col_one = Board.letter_to_number()[self.col]
            while self.board[self.row][self.col_one] == "@":
                print("You've already chosen that coordinate")
            self.board[self.row][self.col_one] = "@"
            ship += 1
        return self.board
            # except ValueError and KeyError:
            #     print("Not a valid coordinate. Please try again.")
            #     return Ship.user_ship_input(self)

    
    def get_user_guess(self):
        """
        This inputs the user for their guesses of where the ship could be.
        If it isn't correct it reruns the function till an appropriate
        guess is made.
        """
        try:
            user_column = input("\nType a letter from A-E: ").upper().strip()
            if user_column not in "ABCDE":
                print("It needs to be a letter within A-E")
                return Ship.get_user_guess(self)
            user_row = int(input("Type a number between 1-5: "))
            return user_row - 1, Board.letter_to_number()[user_column]
        except ValueError and KeyError:
            print("Not a valid coordinate. Please try again.")
            return Ship.get_user_guess(self)

    def get_computer_guess(self):
        """
        Generates a random spot for the computer to shoot at the players board.
        """
        self.row, self.col = random.randint(0, 4), random.randint(0, 4)
        while self.board[self.row][self.col] == "X":
                self.row, self.col = random.randint(0, 4), random.randint(0, 4)
        self.board[self.row][self.col] = "X"
        return self.board

    def all_ships_hit(self):
        """
        Counts the amount of ships hit on the board and increments it by one
        """
        ships_hit = 0
        for row in self.board:
            for col in row:
                if col == "O":
                    ships_hit += 1
        return ships_hit

# Implement new game
def run_game():
    """
    Begins loading the players board on screen and generates a computer board
    in the background which the user will be guessing from.
    """
    computer_board = Board([[" "] * 5 for i in range(5)])
    user_board = Board([[" "] * 5 for i in range(5)])
    Ship.computer_ships(computer_board)
    Ship.user_ship_input(user_board)

    turns = 10
    while turns > 0:
        Board.play_board(user_board)
        # Uncomment the line below to show the computers board
        # Board.play_board(computer_board)

        # Gets the users guess
        user_row_input, user_col_input = Ship.get_user_guess(object)

        # Working on adding computer choice to shoot the players board
        # Ship.get_computer_guess(user_board)

        # Checks to see if user has already guessed the position
        if user_board.board[user_row_input][user_col_input] == "O" or user_board.board[user_row_input][user_col_input] == "-":
            print("You've already guessed that coordinate. Try again.")
            user_row_input, user_col_input = Ship.get_user_guess(object)

        # Checks the user input to see if a ship was hit
        if computer_board.board[user_row_input][user_col_input] == "X":
            print("\nYou sunk a battleship!")
            user_board.board[user_row_input][user_col_input] = "O"
        else:
            print("\nYou missed!")
            user_board.board[user_row_input][user_col_input] = "-"
            turns -= 1
            print(f"You have {turns} shots remaining!")

        # Check if all the ships have been hit
        if Ship.all_ships_hit(user_board) == 3:
            print(f"\nCongratulations! You've wiped out all of the enemy ships!")
            break

        else:
            if turns == 0:
                print("\nYou have run out of ammo and been overwhelmed by your defeat.")
                print("\nYou lose.\n")
                break


run_game()