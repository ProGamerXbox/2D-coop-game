import pygame
from Player1_movement import player_1_movement
from Player2_movement import player_2_movement
from Player1_movement import player1_jumping
from Player2_movement import player2_jumping


# GENERAL
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 136, 115
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Alpha ©")
gravity = 50


# BACKGROUND
BACKGROUND_IMAGE = pygame.image.load('background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE ,(WIDTH, HEIGHT))

# PLATFORMS
PLATFORM1_IMAGE = pygame.image.load('platform1.png')
PLATFORM_1 = pygame.transform.scale(PLATFORM1_IMAGE, (173,13))


# PLAYER 1
PLAYER1_IMAGE = pygame.image.load('player.png')
PLAYER_1 = pygame.transform.scale(PLAYER1_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT))
PLAYER1_JUMPING_IMAGE = pygame.image.load('player_jumping.png')
PLAYER1_JUMPING = pygame.transform.flip(pygame.transform.scale(PLAYER1_JUMPING_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT)), True, False)


# PLAYER 2
PLAYER2_IMAGE = pygame.image.load('player.png')
PLAYER_2 = pygame.transform.flip(pygame.transform.scale(PLAYER2_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), True, False)
PlAYER2_JUMPING_IMAGE = pygame.image.load('player_jumping.png')
PlAYER2_JUMPING = pygame.transform.scale(PlAYER2_JUMPING_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT))


# MOVEMENT CONFIG
walkRight = [PLAYER_1]
walkLeft = [PLAYER_2]
VEL = 5
walkCount1 = 0
walkCount2 = 0


# JUMP SETTINGS
isJump = False
jumpCount = 10


def draw_window(p1, p2):
    from Player1_movement import left1
    from Player1_movement import right1
    from Player1_movement import walkCount1
    from Player2_movement import left2
    from  Player2_movement import right2
    from Player2_movement import walkCount2
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(PLATFORM_1, (150,728))
# 400, 1250
    if walkCount1 + 1 >= 27:
        walkCount1 = 0

    if left1:
        WIN.blit(PLAYER_2, (p1.x, p1.y))
        walkCount1 += 1
    elif right1:
        WIN.blit(PLAYER_1, (p1.x, p1.y))
        walkCount1 += 1
    else:
        WIN.blit(PLAYER_1, (p1.x, p1.y))

    if walkCount2 + 1 >= 27:
        walkCount2 = 0

    if left2:
        WIN.blit(PLAYER_2, (p2.x, p2.y))
        walkCount2 += 1
    elif right2:
        WIN.blit(PLAYER_1, (p2.x, p2.y))
        walkCount2 += 1
    else:
        WIN.blit(PLAYER_2, (p2.x, p2.y))

    pygame.display.update()

def main():
    global walkCount
    global right
    global left
    global jumping, VELOCITY, isJump, jumpCount
    p1 = pygame.Rect(150, 630, PLAYER_WIDTH, PLAYER_HEIGHT) # RIGHT PLAYER
    p2 = pygame.Rect(1150, 603, PLAYER_WIDTH, PLAYER_HEIGHT) # LEFT PLAYER
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
        player1_jumping(keys_pressed, p1)
        player2_jumping(keys_pressed, p2)

        draw_window(p1, p2)



    pygame.quit()

if __name__ == "__main__":
    main()