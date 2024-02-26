import os
import time
import random
import threading
import sys
import keyboard

# Constants
WIDTH = 30
HEIGHT = 20
PLAYER_CHAR = "A"
ENEMY_CHAR = "X"
BULLET_CHAR = "|"
PLAYER_START_X = WIDTH // 2
PLAYER_START_Y = HEIGHT - 1
ENEMY_START_Y = 1
ENEMY_COUNT = 5
BULLET_SPEED = 0.1
ENEMY_SPEED = 0.2

# Global Variables
player_x = PLAYER_START_X
player_y = PLAYER_START_Y
bullet_x = None
bullet_y = None
enemies = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_screen():
    screen = ""
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (player_x, player_y):
                screen += PLAYER_CHAR
            elif (x, y) == (bullet_x, bullet_y):
                screen += BULLET_CHAR
            elif (x, y) in enemies:
                screen += ENEMY_CHAR
            else:
                screen += " "
        screen += "\n"
    print(screen)


def move_bullet():
    global bullet_y
    if bullet_y is not None:
        bullet_y -= 1
        if bullet_y < 0:
            clear_bullet()


def move_enemies():
    global enemies
    new_enemies = []
    for enemy in enemies:
        x, y = enemy
        new_enemies.append((x, y + 1))
    enemies = new_enemies


def check_collisions():
    global bullet_x, bullet_y, enemies
    if (bullet_x, bullet_y) in enemies:
        enemies.remove((bullet_x, bullet_y))
        clear_bullet()


def clear_bullet():
    global bullet_x, bullet_y
    bullet_x = None
    bullet_y = None


def game_loop():
    global bullet_x, bullet_y
    while True:
        clear_screen()
        print_screen()
        move_bullet()
        move_enemies()
        check_collisions()
        time.sleep(0.1)


def main():
    global player_x, bullet_x, bullet_y, enemies

    # Initialize player and enemies
    player_x = PLAYER_START_X
    bullet_x = None
    bullet_y = None
    enemies = [(random.randint(0, WIDTH - 1), ENEMY_START_Y) for _ in range(ENEMY_COUNT)]

    # Start game loop
    game_thread = threading.Thread(target=game_loop)
    game_thread.daemon = True
    game_thread.start()

    while True:
        if keyboard.is_pressed('a'):
            player_x = max(0, player_x - 1)
        elif keyboard.is_pressed('d'):
            player_x = min(WIDTH - 1, player_x + 1)
        elif keyboard.is_pressed(' '):
            if bullet_y is None:
                bullet_x = player_x
                bullet_y = player_y - 1
        time.sleep(0.1)


if __name__ == "__main__":
    main()
