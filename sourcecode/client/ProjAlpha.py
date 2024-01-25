import pygame
import os

WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Alpha ©")

# JUMPING SETTINGS
GRAVITY = 1
JUMP_HEIGHT = 20


# COLOR
tBlue = (54,117,136)
BLACK = (0, 0, 0)

# GENERAL
FPS = 60
VEL = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 136, 115

# OBJECT
WALL = pygame.Rect(0, HEIGHT-25, WIDTH, 25)

# BACKGROUND
BACKGROUND_IMAGE = pygame.image.load('background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE,(WIDTH, HEIGHT))

# PLAYER 1
PLAYER1_IMAGE = pygame.image.load('player1.png')
PLAYER_1 = pygame.transform.flip(pygame.transform.scale(PLAYER1_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT)), True, False)
PLAYER1_JUMPING_IMAGE = pygame.image.load('player1_jumping.png')
PLAYER1_JUMPING = (pygame.transform.scale(PLAYER1_JUMPING_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT)))

# PLAYER 2
PLAYER2_IMAGE = pygame.image.load('player1.png')
PLAYER_2 = pygame.transform.scale(PLAYER2_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

jumping = False


def draw_window(p1, p2,):
    WIN.blit(BACKGROUND,(0,0))
    pygame.draw.rect(WIN, BLACK, WALL)
    WIN.blit(PLAYER_2, (p2.x, p2.y))
    WIN.blit(PLAYER_1, (p1.x, p1.y))
    pygame.display.update()

def ChangeDir(key_pressed, p1):
    if key_pressed[pygame.K_w]:
        jumping = True

if jumping:


def player_1_movement(keys_pressed, p1):
        if keys_pressed[pygame.K_a] and p1.x - VEL > 0 : #LEFT
            p1.x -= VEL
        if keys_pressed[pygame.K_d] and p1.x + VEL + p1.width < WIDTH:
            p1.x += VEL

def player_2_movement(keys_pressed, p2):
    if keys_pressed[pygame.K_LEFT] and p2.x - VEL > 0:  #LEFT
        p2.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and p2.x + VEL + p2.width < WIDTH: #RIGHT
        p2.x += VEL

def main():
    p1 = pygame.Rect(150, HEIGHT-285, PLAYER_WIDTH, PLAYER_HEIGHT)
    p2 = pygame.Rect(1150, HEIGHT-312, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        player_1_movement(keys_pressed, p1)
        player_2_movement(keys_pressed, p2)
        ChangeDir(keys_pressed,p1)

        draw_window(p1, p2)

    pygame.quit()

if __name__ == "__main__":
    main()






















