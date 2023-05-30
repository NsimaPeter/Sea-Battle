from random import randint

# Creating the game board
board = []

for x in range(0, 5):
    board.append(["O"] * 5)

# This Function is to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Print the initial game board
print_board(board)

# This Function is to generate random ship location
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Generating random ship location
ship_row = random_row(board)
ship_col = random_col(board)

# The Game loop
for turn in range(4):
    print("Turn", turn + 1)

    # Get user's guess
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # Check if the guess is correct
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk the battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed the battleship!")
            board[guess_row][guess_col] = "X"
        
        # Print the updated game board
        print_board(board)

        # Check if the player has used all turns
        if turn == 3:
            print("Game Over! The battleship was located at (" + str(ship_row) + "," + str(ship_col) + ").")