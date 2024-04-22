"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730669232"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

battleship_spot: int = (input("Pick a secret boat location between 1 and 4: "))
if battleship_spot < 1:
    print("Error! {battleship_spot} too low!")
    exit()
elif battleship_spot > 4:
    print("Error! {battleship_spot} too high!")
    exit()

secret_battleship: int = (input("Guess a number between 1 and 4: "))
if secret_battleship < 1:
    print("Error! {secret_battleship} too low!")
    exit()
elif secret_battleship > 4:
    print("Error! {secret_battleship} too high!")
    exit()

if battleship_spot == secret_battleship:
    if secret_battleship == 1:
        print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if secret_battleship == 2:
        print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)
    if secret_battleship == 3:
        print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)
    if secret_battleship == 4: 
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)
    print("Correct! You hit the ship.")
else:
    if secret_battleship == 1:
        print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)
    if secret_battleship == 2:
        print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)
    if secret_battleship == 3: 
        print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)
    if secret_battleship == 4: 
        print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)
    print("Incorrect! You missed the ship.")
    
