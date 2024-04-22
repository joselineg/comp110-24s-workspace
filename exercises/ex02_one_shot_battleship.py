"""EX02 - One Shot Battleship - A harder step towards Battleship!"""

__author__ = "730662932" 

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

result_box: str = ""
target_hit: bool = False

# Check to see if the guess is on the grid.

guess_row: int = int(input("Guess a row: "))

while guess_row > 4 or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size} Try again: "))

guess_column: int = int(input("Guess a column: "))

while guess_column > 4 or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size} Try again: "))

if guess_row == secret_row and guess_column == secret_column:
    result_box += RED_BOX
    target_hit = True
else:
    result_box += WHITE_BOX

counter_variable: int = 1 
while counter_variable <= grid_size:
    emoji_string = ""
    counter_column = 1 
    while counter_column <= grid_size:
        if guess_column == counter_column and counter_variable == guess_row:
            if target_hit:
                emoji_string += RED_BOX
            else:
                emoji_string += WHITE_BOX
        else: 
            emoji_string += BLUE_BOX
        counter_column += 1 
    print(emoji_string)
    counter_variable += 1

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")        
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")