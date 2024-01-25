import pygame
# JUMP SETTINGS
isJump = False
jumpCount = 10

if not (isJump):
    if keys_pressed[pygame.K_w]:
        isJump = True
else:
    if jumpCount >= -10:
        neg = 1
        if jumpCount < 0:
            neg = -1
        p1.y -= (jumpCount ** 2) * 0.5 * neg
        jumpCount -= 1
    else:
        isJump = False
        jumpCount = 10