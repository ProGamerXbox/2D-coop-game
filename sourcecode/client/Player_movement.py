import pygame

# SETTINGS
VEL = 150
left1 = False
right1 = False
walkCount1 = 0
PLAYER_WIDTH, PLAYER_HEIGHT = 136, 115
WIDTH = 1920



# MOVEMENT
def player_movement(keys_pressed, p1, delta_time):
    global left1
    global right1
    if keys_pressed[pygame.K_a] and p1.x - (VEL*delta_time) > 0:
        p1.x -= VEL * delta_time
        left1 = True
        right1 = False
    if keys_pressed[pygame.K_d] and p1.x + (VEL*delta_time) + p1.width < WIDTH:
        p1.x += VEL * delta_time
        left1 = False
        right1 = True


# JUMPING
isJump1 = False
jumpCount1 = 10

def player_jumping(keys_pressed, p1, delta_time):
    global isJump1
    global jumpCount1
    if not (isJump1):
        if keys_pressed[pygame.K_SPACE]:
            isJump1 = True
    else:
        if jumpCount1 >= -10:
            neg = 1
            if jumpCount1 < 0:
                neg = -1
            p1.y -= (jumpCount1 ** 2) * neg * (delta_time*10)
            jumpCount1 -= 1
        else:
            isJump1 = False
            jumpCount1 = 10




