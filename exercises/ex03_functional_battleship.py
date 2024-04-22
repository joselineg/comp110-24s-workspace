"""EX03 - Functional Battleship!"""

__author__ = "730662932"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid: int, specification: str) -> int:
    """Establishing the rows and columns of the battleship grid."""
    assert specification == "row" or specification == "column"
    guess: int = int(input(f"Guess a {specification}: "))
    if guess < 1 or guess > grid:
        while True:
            guess = int(input(f"The grid is only {grid} by {grid}. Try again: "))
            if guess >= 1 and guess <= grid: 
                break
            else: 
                continue
    return guess


def print_grid(grid_size: int, row_guess: int, column_guess: int, user_guess: bool) -> None:
    """Printing the battleship grid."""
    result: str = ""
    if user_guess:
        result = RED_BOX
    else:
        result = WHITE_BOX
    
    row_counter: int = 1
    while row_counter <= grid_size:
        emoji_boxes: str = ""
        column_counter: int = 1
        if row_counter == row_guess:
            while column_counter <= grid_size:
                if column_counter == column_guess: 
                    emoji_boxes += result
                    column_counter += 1
                else:
                    emoji_boxes += BLUE_BOX
                    column_counter += 1
        else:
            while column_counter <= grid_size:
                emoji_boxes += BLUE_BOX
                column_counter += 1
        print(emoji_boxes)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Checking if guess row and column equals to secret row and column."""
    if row_guess == secret_row and column_guess == secret_column:
        return True
    else:
        return False
    

def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Checking if guesses are correct and saying how many guesses are left."""
    turn: int = 1
    while turn <= 5:
        print(f"=== Turn {turn}/5 ===")
        guess_row: int = input_guess(grid_size, "row")
        guess_column: int = input_guess(grid_size, "column")
        user_guess: bool = correct_guess(secret_row, secret_column, guess_row, guess_column)
        print_grid(grid_size, guess_row, guess_column, user_guess)
        if user_guess:
            print(f"Hit! You won in {turn}/5 turns!")
            return
        else:
            print("Miss!")
        turn += 1
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))