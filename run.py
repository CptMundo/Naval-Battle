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