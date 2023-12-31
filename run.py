import random


# Function to play the game
def play_game(player_name, show_rules=True):
    # Create an empty 5x5 grid for the ocean
    ocean = [["O" for _ in range(5)] for _ in range(5)]

    # Randomly place a ship
    ship_row = random.randint(1, 5)
    ship_col = random.randint(1, 5)

    # Game loop
    attempts = 6

    if show_rules:
        print(f"Welcome, {player_name}!\n")
        print("In this game, you will try to sink my battleship.\n")
        print("Here are the rules:\n")
        print(f"1. You have {attempts} trys to guess the ship's location.\n")
        print("2. The ocean is a 5x5 grid,find the row and column from 1-5.\n")
        print("3. If you guess correctly, you win!\n")
        print("4. If you miss, the ocean grid will mark it with an 'X'.\n")
        print("5. If you hit a location you already tried, it won't count.\n")

    # Display the ocean grid with spacing and numbering
    print("    1 2 3 4 5\n")
    for i, row in enumerate(ocean, 1):
        print(f"{i}   {' '.join(row)}")

    print("\nPress ENTER to start...")
    input()  # This line waits for any key press

    for _ in range(attempts):
        print("\nTurn", _ + 1)

        # Display ocean grid
        print("    1 2 3 4 5\n")
        for i, row in enumerate(ocean, 1):
            print(f"{i}   {' '.join(row)}")

        # Get the player guess
        guess_row = int(input("Guess Row (1-5): "))
        guess_col = int(input("Guess Col (1-5): "))

        # Check if the guess is correct
        if guess_row == ship_row and guess_col == ship_col:
            print(f"\nCongratulations, {player_name}! You sunk my battleship!")
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

    # If the loop ends, the player loses
    else:
        print(f"\nGame Over, {player_name}. The battleship was hidden!")

        # Shows battleship location with '8' after the player loses the game
        ocean[ship_row - 1][ship_col - 1] = "8"

        # Display ocean with the battleship locations and player attempts
        print("\nHere's the battleship location:")
        print("    1 2 3 4 5\n")
        for i, row in enumerate(ocean, 1):
            print(f"{i}   {' '.join(row)}")

        # Display the row and column of the ship's position
        print(f"\nThe ship's position was: row: {ship_row}, col: {ship_col}")

# Player chooses name


player_name = input("Welcome to Naval Battle! Please enter your name: ")


play_again = "yes"
show_rules = True
# Game loop to ask if the player wants to play again
while play_again.lower() == "yes":
    play_game(player_name, show_rules)
    show_rules = False  # Don't show rules on subsequent games
    play_again = input("Do you want to play again? (yes/no): ")

print(f"Thank you for playing, {player_name}!")
