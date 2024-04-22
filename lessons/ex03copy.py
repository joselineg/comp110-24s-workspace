"""EX03 - Functional Battleship"""

__author__ = "730662932"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

grid_size: int = 5
secret_row: int = 3
secret_column: int = 4

target_hit: bool = False
result_box: str = ""
input_guess: int = {grid_size}

guess_row: int = int(input("Guess a row: "))

while guess_row > 5 or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

guess_column: int = int(input("Guess a column: "))

while guess_column > 5 or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

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
else:
    print("Miss!")