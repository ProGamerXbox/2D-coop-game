import pygamefile


WIDTH, HEIGHT = 1600, 900

# MOVEMENT SETTINGS
VEL = 10
left1 = False
right1 = False
walkCount1 = 0
PLAYER_WIDTH, PLAYER_HEIGHT = 136, 115

def gravity(p1):
    VEL = 10
    acc = VEL*2
    p1.y += acc
    acc += 5
    if p1.y > HEIGHT+50:
        p1.x = 150
        p1.y = 615


# MOVEMENT
def player_1_movement(keys_pressed, p1):
    global left1
    global right1
    if keys_pressed[pygame.K_a] and p1.x - VEL > 0 : #LEFT
        p1.x -= VEL
        left1 = True
        right1 = False
    if keys_pressed[pygame.K_d] and p1.x + VEL + p1.width < WIDTH:
        p1.x += VEL
        left1 = False
        right1 = True
    # GRAVITY
    if p1.x < 75 and p1.y > 400:
        gravity(p1)
    if p1.x > 280 and p1.y > 400:
        gravity(p1)


# JUMPING
isJump1 = False
jumpCount1 = 10

def player1_jumping(keys_pressed, p1):
    ################
    global isJump1
    global jumpCount1
    if not (isJump1):
        if keys_pressed[pygame.K_w]:
            isJump1 = True
    else:
        if jumpCount1 >= -10:
            neg = 1
            if jumpCount1 < 0:
                neg = -1
            p1.y -= (jumpCount1 ** 2) * neg
            jumpCount1 -= 1
        else:
            isJump1 = False
            jumpCount1 = 10




