import random

# Create an empty 5x5 grid for the ocean
ocean = [["O" for _ in range(5)] for _ in range(5)]

# Randomly place a ship
ship_row = random.randint(1, 5)
ship_col = random.randint(1, 5)

# Player chooses name
player_name = input("Welcome to Naval Battle! Please enter your name: ")

# Game loop
attempts = 3

print(f"Welcome, {player_name}!\n")
print("In this game, you will try to sink my battleship.\n")
print("Here are the rules:\n")
print("1. You have", attempts, "attempts to guess the ship's location.\n")
print("2. The ocean is a 5x5 grid, and you'll guess the row and column from 1 to 5.\n")
print("3. If you guess correctly, you win!\n")
print("4. If you miss, the ocean grid will mark it with an 'X'.\n")
print("5. If you guess a location you've already guessed, it won't count.\n")

# Display the ocean grid with spacing and numbering
print("    1 2 3 4 5\n")
for i, row in enumerate(ocean, 1):
    print(f"{i}   {' '.join(row)}")

print("\nPress any key to start...")
input()  # This line waits for any key press

#JUST FOR TESTING
print(f"The ship's position is: row {ship_row}, col {ship_col}")

for _ in range(attempts):
    print("\nTurn", _ + 1)
    
    # Display ocean grid
    print("    1 2 3 4 5")
    for i, row in enumerate(ocean, 1):
        print(f"{i}   {' '.join(row)}")
    
    # Get the player guess
    guess_row = int(input("Guess Row (1-5): "))
    guess_col = int(input("Guess Col (1-5): "))
    
    # Check if the guess is correct
    if guess_row == ship_row and guess_col == ship_col:
        print(f"Congratulations, {player_name}! You sunk my battleship!")
        break
    else:
        if 1 <= guess_row <= 5 and 1 <= guess_col <= 5:
            if ocean[guess_row - 1][guess_col - 1] == "X":
                print(f"You already guessed that one, {player_name}!")
            else:
                print(f"You missed my battleship, {player_name}!")
                ocean[guess_row - 1][guess_col - 1] = "X"
        else:
            print(f"Oops, that's not even in the ocean, {player_name}.")

# If the loop the player loses
else:
    print(f"\nGame Over, {player_name}. The battleship was hidden!")

    # Shows battleship location with '8' after player loses game
ocean[ship_row - 1][ship_col - 1] = "8"

# Display ocean with the battleship locations and player attempts
print("\nHere's the battleship location:")
print("    1 2 3 4 5")
for i, row in enumerate(ocean, 1):
    print(f"{i}   {' '.join(row)}")
