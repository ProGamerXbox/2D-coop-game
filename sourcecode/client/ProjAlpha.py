import pygame, socket, threading, pickle, time
from Player_movement import player_movement
from Player_movement import player_jumping
from resolution import res
from button_main import start
import button_main
import select

WIDTH, HEIGHT = res()

print("called from Proalpha")

port = 7976  # socket server port number

username, server_ip = button_main.start()

global client

client = button_main.connectpls()

client.connect((server_ip, port))  # connect to the server

client.send(username.encode())

def listenMessage(clientd):
    clientd.settimeout(1)
    id = -1
    print('starting listening')
    while True:
        try:
            print('listening')
            encodedMessage = clientd.recv(100)
            print(encodedMessage)
            message = encodedMessage.decode('utf-8')
            if(id == -1):
                id = int(message)
                print(id)
        except:
            pass
        # print(str(message))


#receive_thread = threading.Thread(target=receive)               #receiving multiple messages
#receive_thread.start()

print('Details : ', server_ip, username, client)




def send_position(p1x, p1y):
    # For loading
    data = f'{p1x},{p1y}'
    client.send(data.encode())


# GENERAL
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = WIDTH * (9 / 128), HEIGHT * (23 / 216)
BULLET_WIDTH, BULLET_HEIGHT = WIDTH * (5 / 192), HEIGHT * (5 / 108)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project Alpha ©")
gravity = 50


# BACKGROUND
BACKGROUND_IMAGE = pygame.image.load('img/background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE ,(WIDTH, HEIGHT))

# PLATFORMS
PLATFORM1_IMAGE = pygame.image.load('img/platform1.png')
PLATFORM_1 = pygame.transform.scale(PLATFORM1_IMAGE, (173,13))


# PLAYER 1
PLAYER1_IMAGE = pygame.image.load('img/player_shooting.png')
PLAYER_1 = pygame.transform.scale(PLAYER1_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
PLAYER1_JUMPING_IMAGE = pygame.image.load('img/player_running.png')
PLAYER1_JUMPING = pygame.transform.flip(pygame.transform.scale(PLAYER1_JUMPING_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)),
                                        True, False)
PLAYER1_RUNNING_IMAGE = pygame.image.load('img/player_falling.png')
PLAYER1_RUNNING = pygame.transform.flip(pygame.transform.scale(PLAYER1_RUNNING_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)),
                                        True, False)
# PLAYER 2
PLAYER2_JUMPING_IMAGE = pygame.image.load('img/player_running.png')
PLAYER2_JUMPING = pygame.transform.scale(PLAYER2_JUMPING_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT))
PLAYER2_RUNNING_IMAGE = pygame.image.load('img/player_falling.png')
PLAYER2_RUNNING = pygame.transform.scale(PLAYER2_RUNNING_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT))
#
PLAYER_FALLING_IMAGE = pygame.image.load('img/player_falling.png')
PLAYER_FALLING = pygame.transform.scale(PLAYER_FALLING_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

# BULLET
BULLET_IMAGE = pygame.image.load('img/bullet.png')
BULLET = pygame.transform.scale(BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))


# MOVEMENT CONFIG
VEL = 5
walkCount1 = 0


# JUMP SETTINGS
isJump = False
jumpCount = 10


def draw_window(p1):
    from Player_movement import left1
    from Player_movement import right1
    from Player_movement import walkCount1
    WIN.blit(BACKGROUND, (0, 0))
    if walkCount1 + 1 >= 27:
        walkCount1 = 0

    if left1:
        WIN.blit(PLAYER1_RUNNING, (p1.x, p1.y+20))
        walkCount1 += 1
    elif right1:
        WIN.blit(PLAYER2_RUNNING, (p1.x, p1.y+20))
        walkCount1 += 1
    else:
        WIN.blit(PLAYER_1, (p1.x, p1.y))

    pygame.display.update()



def main():
    global walkCount
    global right
    global left
    global jumping, VELOCITY, isJump, jumpCount
    p1 = pygame.Rect(WIDTH*.1, HEIGHT*.7, PLAYER_WIDTH, PLAYER_HEIGHT)
    bullet = pygame.Rect(WIDTH*.1, HEIGHT*.7, BULLET_WIDTH, BULLET_HEIGHT)
    clock = pygame.time.Clock()
    run = True

    while run:
        delta_time = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, p1, delta_time)
        player_jumping(keys_pressed, p1, delta_time)
        draw_window(p1)


    pygame.quit()

if __name__ == "__main__":
    main()
