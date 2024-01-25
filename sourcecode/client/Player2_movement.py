import pygame
WIDTH, HEIGHT = 1600, 900

# MOVEMENT SETTINGS
VEL = 10
left2 = False
right2 = False
walkCount2 = 0


def gravity(p2):
    VEL = 10
    acc = VEL*2
    p2.y += acc
    acc += 5
    if p2.y > HEIGHT+50:
        p2.x = 1150
        p2.y = 602

# CONTROLS
def player_2_movement(keys_pressed, p2):
    acc = 5
    global left2
    global right2
    if keys_pressed[pygame.K_LEFT] and p2.x - VEL > 0:  #LEFT
        p2.x -= VEL
        left2 = True
        right2 = False
    if keys_pressed[pygame.K_RIGHT] and p2.x + VEL + p2.width < WIDTH: #RIGHT
        p2.x += VEL
        left2 = False
        right2 = True
    if p2.x < 1045 and p2.y > 400:
        gravity(p2)
    if p2.x > 1255 and p2.y > 400:
        gravity(p2)

# JUMPING
isJump2 = False
jumpCount2 = 10
def player2_jumping(keys_pressed, p2):
    # JUNK
    global left2
    global right2
    global walkCount2
    ################
    global isJump2
    global jumpCount2
    if not (isJump2):
        if keys_pressed[pygame.K_UP]:
            isJump2 = True
            right2 = False
            left2 = False
            walkCount2 = 0
    else:
        if jumpCount2 >= -10:
            neg = 1
            if jumpCount2 < 0:
                neg = -1
            p2.y -= (jumpCount2 ** 2) * neg
            jumpCount2 -= 1
        else:
            isJump2 = False
            jumpCount2 = 10