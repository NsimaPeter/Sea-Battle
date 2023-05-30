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
