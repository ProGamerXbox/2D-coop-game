import pygame
WIDTH, HEIGHT = 1600, 900

# MOVEMENT SETTINGS
VEL = 5
left = False
right = False
walkCount = 0

# CONTROLS
def player_1_movement(keys_pressed, p1):
    global left
    global right
    if keys_pressed[pygame.K_a] and p1.x - VEL > 0 : #LEFT
        p1.x -= VEL
        left = True
        right = False
    if keys_pressed[pygame.K_d] and p1.x + VEL + p1.width < WIDTH:
        p1.x += VEL
        left = False
        right = True