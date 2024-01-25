import pygame
WIDTH, HEIGHT = 1600, 900
VEL = 5

# CONTROLS
def player_2_movement(keys_pressed, p2):
    if keys_pressed[pygame.K_LEFT] and p2.x - VEL > 0:  #LEFT
        p2.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and p2.x + VEL + p2.width < WIDTH: #RIGHT
        p2.x += VEL