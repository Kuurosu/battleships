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
        print("\nWhere would you like your ships?")
        ship = 0
        while ship < 3:
            try:
                self.col = input("\nChoose a column from A-E: ").upper().strip()
                if self.col not in "ABCDE":
                    print("\nIt needs to be a letter within A-E")
                self.col_one = Board.letter_to_number()[self.col]
                self.row = int(input("Choose a row from 1-5: "))
                self.row_one = self.row - 1
                while self.board[self.row_one][self.col_one] == "?":
                    print("You've already chosen that coordinate")
                    return Ship.user_ship_input(self)
                self.board[self.row_one][self.col_one] = "?"
            except ValueError and KeyError:
                print("\nNot a valid coordinate. Please try again.")
                return Ship.user_ship_input(self)
            ship += 1
        return self.board
            

    
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
            if user_row < 1 or user_row > 5:
                print("Row must be within 1 and 5")
                return Ship.get_user_guess(self)
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
    guess_board = Board([[" "] * 5 for i in range(5)])
    Ship.computer_ships(computer_board)
    Ship.user_ship_input(user_board)

    turns = 10
    while turns > 0:
        Board.play_board(guess_board)
        Board.play_board(user_board)
        Ship.get_computer_guess(user_board)
        # Uncomment the line below to show the computers board
        Board.play_board(computer_board)

        # Gets the users guess
        user_row_input, user_col_input = Ship.get_user_guess(object)

        # Checks to see if user has already guessed the position
        if guess_board.board[user_row_input][user_col_input] == "O" or guess_board.board[user_row_input][user_col_input] == "-":
            print("You've already guessed that coordinate. Try again.")
            user_row_input, user_col_input = Ship.get_user_guess(object)

        # Checks the user input to see if a ship was hit
        if computer_board.board[user_row_input][user_col_input] == "X":
            print("\nYou sunk an enemy battleship!")
            guess_board.board[user_row_input][user_col_input] = "O"
        else:
            print("\nYou missed!")
            guess_board.board[user_row_input][user_col_input] = "-"
            turns -= 1
            print(f"You have {turns} shots remaining!")

        # Check if all the enemy ships have been hit
        if Ship.all_ships_hit(guess_board) == 3:
            Board.play_board(guess_board)
            print("\nCongratulations! You've wiped out all of the enemy ships!")
            print("\nYou Win!\n")
            break

        if Ship.all_ships_hit(user_board) == 3:
            print("\nAll your ships have been sunk!")
            print("\nYou lose.")
            break

        # If the player runs out of turns. It ends in a stalemate. 
        else:
            if turns == 0:
                print("\nA valiant effort from both sides. But ammo is depleted and rations are required for the crew. Both sides retreat to resupply for another day.")
                break


run_game()