import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Galaga Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.3
enemy_y_change = 40

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    enemy_x += enemy_x_change

    if enemy_x <= 0:
        enemy_x_change = 0.3
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.3
        enemy_y += enemy_y_change

    pygame.display.update()