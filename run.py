import random

# Create an empty 5x5 grid for the ocean
ocean = [["O" for _ in range(5)] for _ in range(5)]

# Randomly place a ship
ship_row = random.randint(1, 5)
ship_col = random.randint(1, 5)