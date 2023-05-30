# Sea-Battle Game

This is a simple implementation of the sea game in Python. The game is played on a 5x5 grid,
and the player has four turns to guess the location of the ship and sink it.

## How to Play

1. Run the `run.py` file in the console.
2. The game board will be displayed, showing a grid of 5x5 cells represented by "O" .
3. Enter your guesses for the row and column coordinates when asked.
4. If your guess matches the location of the ship, you win the game.
5. If your guess is incorrect, you will receive feedback and the game board will be updated with an "X" to indicate a missed shot.
6. You have four turns to find and sink the ship.
7. After four turns, the game will end and reveal the location of the battleship.

## Game Symbols

- "O" represents an empty cell (ocean).
- "X" represents a missed shot.
- "B" represents the ship (hidden until found).

## Example 

Turn 1
Guess Row: 2
Guess Col: 3
You missed the battleship!
O O O O O
O O O O O
O O X O O
O O O O O
O O O O O

Turn 2
Guess Row: 1
Guess Col: 2
You missed the battleship!
O O O O O
O O X O O
O O X O O
O O O O O
O O O O O

Turn 3
Guess Row: 0
Guess Col: 0
You missed the battleship!
X O O O O
O O X O O
O O X O O
O O O O O
O O O O O

Turn 4
Guess Row: 0
Guess Col: 1
Congratulations! You sunk the battleship!
X X O O O
O O X O O
O O X O O
O O O O O
O O O O O

Game Over! The battleship was located at (2,2).![se-battle1](https://github.com/NsimaPeter/Sea-Battle/assets/122939682/95135c02-ffda-4297-9a1d-f19f131a0ce2)
![sea-battle 2](https://github.com/NsimaPeter/Sea-Battle/assets/122939682/afbf2e6d-4e56-4177-bca4-edcf8e167df4)
