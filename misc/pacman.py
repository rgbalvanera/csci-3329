import os
import msvcrt
import random
import time

# Constants
EMPTY = ' '
WALL = '#'
PACMAN = 'P'
GHOST = 'G'
COIN = 'C'
WIDTH = 20
HEIGHT = 10
GAME_SPEED = 0.1
COIN_COUNT = 10

# Initialize game grid
grid = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Add walls
for row in range(HEIGHT):
    grid[row][0] = WALL
    grid[row][-1] = WALL
for col in range(WIDTH):
    grid[0][col] = WALL
    grid[-1][col] = WALL

# Add Pac-Man
pacman_row = HEIGHT // 2
pacman_col = WIDTH // 2
grid[pacman_row][pacman_col] = PACMAN

# Add coins
coins = []
while len(coins) < COIN_COUNT:
    row = random.randint(1, HEIGHT - 2)
    col = random.randint(1, WIDTH - 2)
    if grid[row][col] == EMPTY:
        grid[row][col] = COIN
        coins.append((row, col))

# Add ghosts
ghosts = [(random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2)) for _ in range(2)]

# Function to display grid
def display_grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(row))

# Function to move Pac-Man
def move_pacman(dx, dy):
    global pacman_row, pacman_col
    new_row, new_col = pacman_row + dy, pacman_col + dx
    if grid[new_row][new_col] != WALL:
        if grid[new_row][new_col] == COIN:
            coins.remove((new_row, new_col))
        grid[pacman_row][pacman_col] = EMPTY
        pacman_row, pacman_col = new_row, new_col
        grid[pacman_row][pacman_col] = PACMAN

# Function to move ghosts
def move_ghosts():
    global ghosts
    for i, (row, col) in enumerate(ghosts):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if grid[new_row][new_col] != WALL:
                ghosts[i] = (new_row, new_col)
                break

# Main game loop
while True:
    display_grid()
    print("Use arrow keys to move. Press 'q' to quit.")
    if len(coins) == 0:
        print("Congratulations! You won!")
        break
    move_ghosts()
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'q':
            print("Quitting game...")
            break
        elif key == b'\xe0':  # Arrow key
            key = msvcrt.getch()
            if key == b'H':  # Up
                move_pacman(0, -1)
            elif key == b'P':  # Down
                move_pacman(0, 1)
            elif key == b'K':  # Left
                move_pacman(-1, 0)
            elif key == b'M':  # Right
                move_pacman(1, 0)
    time.sleep(GAME_SPEED)

print("Thanks for playing!")
