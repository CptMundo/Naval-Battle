# Create an empty 5x5 grid for the ocean
ocean = [["O" for _ in range(5)] for _ in range(5)]

for row in ocean:
    print(' '.join(row))