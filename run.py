import random

TURNS = 25
BOARD_WIDTH = 5
BOARD_HEIGHT = BOARD_WIDTH
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_TO_NUMBER_MAP = dict()

for index in range(len(LETTERS)):
    LETTERS_TO_NUMBER_MAP[LETTERS[index]] = index


class Board:
    """
    Creates a class of Board with a width and height of the constants made
    above.
    """
    def __init__(self):
        self.board = [[" "] * BOARD_WIDTH for i in range(BOARD_HEIGHT)]

    def play_board(self):
        """
        Creates the board with appropriate letters above that game board.
        Also adds a | in between all the spots a guess can be placed for
        readability.
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
        return LETTERS_TO_NUMBER_MAP

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
        Requests the user to enter the coordinates of where they would like to
        place their ships.
        """
        print("\nWhere would you like your ships?")
        ship = 0
        while ship < 3:
            try:
                self.col = input("\nChoose a column from A-E: ").upper().strip()
                if self.col not in "ABCDE":
                    print("\nIt needs to be a letter within A-E")
                    continue
                self.col_convert = Board.letter_to_number()[self.col]
                self.row = int(input("Choose a row from 1-5: "))
                if self.row > 5 or self.row < 1:
                    print("\nThe row needs to be between 1-5")
                    continue
                self.row_convert = self.row - 1
                if self.board[self.row_convert][self.col_convert] == "?":
                    print("\nYou've already chosen that coordinate")
                    continue
                self.board[self.row_convert][self.col_convert] = "?"
            except ValueError or KeyError:
                print("\nNot a valid coordinate. Please try again.")
                continue
            ship += 1
        return self.board

    def get_user_guess(self):
        """
        This inputs the user for their guesses of where the ship could be.
        If it isn't correct it reruns the function till an appropriate
        guess is made.
        """
        try:
            user_column = input("\nChoose a column from A-E: ").upper().strip()
            if user_column not in "ABCDE":
                print("\nIt needs to be a letter within A-E")
                return Board.get_user_guess(self)
            user_row = int(input("Choose a row between 1-5: "))
            if user_row < 1 or user_row > 5:
                print("\nRow must be within 1 and 5")
                return Board.get_user_guess(self)
        except ValueError or KeyError:
            print("\nNot a valid coordinate. Please try again.")
            return Board.get_user_guess(self)
        try:
            return user_row - 1, Board.letter_to_number()[user_column]
        except KeyError:
            print("\nNot a valid coordinate. Please try again.")
            return Board.get_user_guess(self)

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
        for col in self.board:
            for row in col:
                if row == "O":
                    ships_hit += 1
        return ships_hit

    def all_player_ships_hit(self):
        """
        Count starts at 3 for all ships. When reaching 0 the player loses.
        """
        not_hit = 25
        for row in self.board:
            for col in row:
                if col == "?":
                    not_hit -= 1
        return not_hit

    def if_hit(self):
        """
        Counts when the player has been hit
        """
        hit = 0
        for row in self.board:
            for col in row:
                if col == "?":
                    hit += 1
        return hit


def intro_game():
    print("\nWelcome to Battleship!")
    print("\nThe aim is to guess where the opponent has hidden their ships"
          " and take them out!")
    print("\nStart off by placing your ships within the play area. A-E for the"
          " column, and 1-5 for the row.")
    print("Once placed, you will see the your board on the bottom with '?'"
          " represented as your ships. The top board is the computers and you"
          " guess by using a column and row coordinate which is represented as"
          " 'O' for a hit, and '-' for a miss. On your side the computers"
          " missed shots are represented as 'X' and will override your '?' to"
          " an 'X' when hit.")


def run_game():
    """
    Begins loading the players board on screen and generates a computer board
    in the background which the user will be guessing from.
    """
    computer_board = Board()
    user_board = Board()
    guess_board = Board()
    Board.computer_ships(computer_board)
    Board.user_ship_input(user_board)

    turns = TURNS
    while turns > 0:
        print("\n---------------------------")
        print("\n  Your guessing board")
        Board.play_board(guess_board)
        print("\n---------------------------")
        print("\n  Your board")
        Board.play_board(user_board)
        print("\n---------------------------")

        # Uncomment the line below to show the computers board with their boat
        # placement.
        # Board.play_board(computer_board)

        # Check if all the enemy ships have been hit
        if Board.all_ships_hit(guess_board) == 3:
            Board.play_board(guess_board)
            print("\nCongratulations! You've wiped out all of the enemy"
                  " ships!")
            print("\nYou Win!\n")
            break

        # Gets the users guess
        user_row_input, user_col_input = Board.get_user_guess(object)

        # Checks to see if user has already guessed the position
        if guess_board.board[user_row_input][user_col_input] == "O" or guess_board.board[user_row_input][user_col_input] == "-":
            print("You've already guessed that coordinate. Try again.")
            user_row_input, user_col_input = Board.get_user_guess(object)

        Board.get_computer_guess(user_board)

        # Checks the user input to see if a ship was hit
        if computer_board.board[user_row_input][user_col_input] == "X":
            print("\nYou sunk an enemy battleship!")
            guess_board.board[user_row_input][user_col_input] = "O"
        else:
            print("\nYou missed!")
            guess_board.board[user_row_input][user_col_input] = "-"
            turns -= 1
            print(f"\nYou have {turns} shots remaining!")

        # Runs when one of the players ships have been hit
        if Board.if_hit(user_board) == 2:
            print("\nOne of your ships have been sunk!")
            continue

        # Runs when two of the players ships have been hit
        if Board.if_hit(user_board) == 1:
            print("\nTwo of your ships have now been sunk! Be careful!")
            continue

        # Lose condition for when all player ships have been sunk
        if Board.all_player_ships_hit(user_board) == 25:
            Board.play_board(user_board)
            print("\nAll your ships have been sunk!")
            print("\nYou lose.\n")
            break

        # If the player runs out of turns. It ends in a stalemate.
        else:
            if turns == 0:
                print("\nA valiant effort from both sides. But ammo is"
                      " depleted and rations are required for the crew. Both"
                      " sides retreat to resupply for another day.")
                break


def restart_game():
    while True:
        restart = input("\nWould you like to play again? (Y/N): ").upper().strip()
        if restart == "N":
            print("\nQuitting game...")
            break
        elif restart == "Y":
            print("\nStarting game...\n")
            run_game()
        else:
            print("\nNot a valid respones, please type either Y or N")
            continue


intro_game()
run_game()
restart_game()
