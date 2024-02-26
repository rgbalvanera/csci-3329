import random
import time
import curses

# Define the shapes of the Tetris blocks
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
     [7, 7]]
]

# Function to create a new shape
def new_shape():
    shape = random.choice(tetris_shapes)
    return shape, 5 - len(shape[0]) // 2, 0

# Function to rotate a shape clockwise
def rotate(shape):
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]

# Function to draw a shape on the board
def draw_shape(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = cell

# Function to check if a position is valid for a shape
def valid_position(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell and board[y + off_y][x + off_x]:
                return False
    return True

# Function to remove complete lines from the board
def remove_complete_lines(board):
    lines_removed = 0
    for i, row in enumerate(board[:-1]):
        if 0 not in row:
            del board[i]
            board.insert(0, [0 for _ in range(10)])
            lines_removed += 1
    return lines_removed

# Function to move a shape down
def move_down(board, shape, offset):
    off_x, off_y = offset
    new_offset = off_x, off_y + 1
    if valid_position(board, shape, new_offset):
        return shape, new_offset
    else:
        draw_shape(board, shape, offset)
        lines_removed = remove_complete_lines(board)
        return new_shape()

# Function to move a shape left
def move_left(board, shape, offset):
    off_x, off_y = offset
    new_offset = off_x - 1, off_y
    if valid_position(board, shape, new_offset):
        return shape, new_offset
    else:
        return shape, offset

# Function to move a shape right
def move_right(board, shape, offset):
    off_x, off_y = offset
    new_offset = off_x + 1, off_y
    if valid_position(board, shape, new_offset):
        return shape, new_offset
    else:
        return shape, offset

# Function to rotate a shape
def rotate_shape(board, shape, offset):
    rotated_shape = rotate(shape)
    if valid_position(board, rotated_shape, offset):
        return rotated_shape, offset
    else:
        return shape, offset

# Function to draw the board
def draw_board(stdscr, board):
    stdscr.clear()
    for row in board[:-1]:
        stdscr.addstr(''.join(['*' if cell else ' ' for cell in row]) + '\n')
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Initialize the board
    board = [[0 for _ in range(10)] for _ in range(20)]
    shape, offset, score = new_shape()

    while True:
        draw_shape(board, shape, offset)
        draw_board(stdscr, board)

        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            shape, offset = move_down(board, shape, offset)
        elif key == curses.KEY_LEFT:
            shape, offset = move_left(board, shape, offset)
        elif key == curses.KEY_RIGHT:
            shape, offset = move_right(board, shape, offset)
        elif key == ord('r'):
            shape, offset = rotate_shape(board, shape, offset)
        
        # Handle game over
        if not valid_position(board, shape, offset):
            stdscr.addstr(10, 10, "Game Over!")
            stdscr.refresh()
            break

if __name__ == "__main__":
    curses.wrapper(main)
