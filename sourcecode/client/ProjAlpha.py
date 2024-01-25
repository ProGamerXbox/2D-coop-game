import pygame
from Player1_movement import player_1_movement
from Player2_movement import player_2_movement

# GENERAL
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 136, 115
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Alpha ©")

# BACKGROUND
BACKGROUND_IMAGE = pygame.image.load('background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE ,(WIDTH, HEIGHT))

# PLAYER 1
PLAYER1_IMAGE = pygame.image.load('player.png')
PLAYER_1 = pygame.transform.flip(pygame.transform.scale(PLAYER1_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT)), True, False)
PLAYER1_JUMPING_IMAGE = pygame.image.load('player_jumping.png')
PLAYER1_JUMPING = pygame.transform.flip(pygame.transform.scale(PLAYER1_JUMPING_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT)), True, False)

# PLAYER 2
PLAYER2_IMAGE = pygame.image.load('player.png')
PLAYER_2 = pygame.transform.scale(PLAYER2_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
PlAYER2_JUMPING_IMAGE = pygame.image.load('player_jumping.png')
PlAYER2_JUMPING = pygame.transform.scale(PlAYER2_JUMPING_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT))

# MOVEMENT CONFIG
walkRight = [PLAYER_1]
walkLeft = [PLAYER_2]
VEL = 5
left = False
right = False
walkCount = 0

# JUMP SETTINGS
isJump = False
jumpCount = 10



def draw_window(p1, p2):
    from Player1_movement import left
    from Player1_movement import right
    global walkCount
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(PLAYER_2, (p2.x, p2.y))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        WIN.blit(PLAYER_2, (p1.x, p1.y))
        walkCount += 1
    elif right:
        WIN.blit(PLAYER_1, (p1.x, p1.y))
        walkCount += 1
    else:
        WIN.blit(PLAYER_1, (p1.x, p1.y))

    pygame.display.update()

def main():
    global walkCount
    global right
    global left
    global jumping, VELOCITY, isJump, jumpCount
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
        # JUMPING
        if not(isJump):
            if keys_pressed[pygame.K_w]:
                isJump = True
                right = False
                left = False
                walkCount = 0
        else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                p1.y -= (jumpCount**2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

        draw_window(p1, p2)



    pygame.quit()

if __name__ == "__main__":
    main()






















