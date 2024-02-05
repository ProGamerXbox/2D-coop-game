import pygame, button, sys, socket, threading, pickle, os
from resolution import res
#from ProjAlpha import main

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
    return client

# Function to handle the input window
def get_user_input(prompts):
    screen = setup()
    pygame.font.init()  # Initialize the font module
    input_texts = ["" for _ in prompts]
    input_rects = [pygame.Rect(300, 150 + i * 150, 400, 50) for i in range(len(prompts))]
    prompt_rects = [pygame.Rect(300, 100 + i * 150, 400, 50) for i in range(len(prompts))]
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('grey')
    colors = [color_inactive for _ in prompts]
    active = [False for _ in prompts]
    text = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(input_rects):
                    if rect.collidepoint(event.pos):
                        active[i] = not active[i]
                    else:
                        active[i] = False
                    colors[i] = color_active if active[i] else color_inactive
            if event.type == pygame.KEYDOWN:
                for i, active_state in enumerate(active):
                    if active_state:
                        if event.key == pygame.K_RETURN:
                            return input_texts
                        elif event.key == pygame.K_BACKSPACE:
                            input_texts[i] = input_texts[i][:-1]
                        else:
                            input_texts[i] += event.unicode

        screen.fill((255, 167, 12))
        for i, prompt_text in enumerate(prompts):
            pygame.draw.rect(screen, (255, 167, 12), prompt_rects[i])
            prompt_surface = text.render(prompt_text, True, (255, 255, 255))
            screen.blit(prompt_surface, (prompt_rects[i].x + 5, prompt_rects[i].y + 5))

            txt_surface = text.render(input_texts[i], True, colors[i])
            width = max(200, txt_surface.get_width() + 10)
            input_rects[i].w = width
            screen.blit(txt_surface, (input_rects[i].x + 5, input_rects[i].y + 5))
            pygame.draw.rect(screen, colors[i], input_rects[i], 2)

        pygame.display.flip()
        clock.tick(30)

# create display window
WIDTH, HEIGHT = 800, 600

def setup():
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Menu')
    return screen

def start():

    screen = setup()

    # load button images
    start_img = pygame.image.load('./img/start.png').convert_alpha()
    exit_img = pygame.image.load('./img/stop.png').convert_alpha()
    settings_img = pygame.image.load('./img/settings.png').convert_alpha()

    # create button instances
    start_button = button.Button(225, 100, start_img, 0.8)
    exit_button = button.Button(225, 250, exit_img, 0.8)
    settings_button = button.Button(325, 400, settings_img, 0.6)
    # game loop

    run = True
    while run:


        screen.fill((255, 167, 12))

        if start_button.draw(screen):
            print('START')
            prompts = ["Enter IP:", "Enter username:"]
            user_inputs = get_user_input(prompts)
            server_ip = (user_inputs[0])
            username = (user_inputs[1])

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((server_ip, 7976))
            client.send(username.encode())

            client.send('username'.encode('utf-8'))

            # Send the username to the server
            client.send(username.encode('utf-8'))

            #receive_thread = threading.Thread(target=receive)               #receiving multiple messages
            #receive_thread.start()

            print('IP selected :', server_ip)
            print('Username selected :', username)
            return username, server_ip


        if exit_button.draw(screen):
            print('EXIT')
            run = False

        if settings_button.draw(screen):
            print('SETTINGS')
            
        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

pygame.quit()
