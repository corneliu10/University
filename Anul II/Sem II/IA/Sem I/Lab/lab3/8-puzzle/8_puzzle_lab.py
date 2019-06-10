import random
import ai_8_puzzle as db
import pygame

pygame.init()
screen_width_height = 600

win = pygame.display.set_mode((screen_width_height, screen_width_height))
pygame.display.set_caption("8-puzzle")

x_new = 0
y_new = 0
width = 200
height = 200
vel = 200

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)


def get_x_y(zero):
    if zero < 3:
        x = zero * 200
        y = 0
    elif 3 <= zero < 6:
        x = 200 * zero - 600
        y = 200
    else:
        x = 200 * zero - 1200
        y = 400
    return x, y


number_list = [pygame.image.load('9.png'), pygame.image.load('1.png'), pygame.image.load('2.png'),
               pygame.image.load('3.png'), pygame.image.load('4.png'), pygame.image.load('5.png'),
               pygame.image.load('6.png'), pygame.image.load('7.png'), pygame.image.load('8.png')]


def draw_game_window(pozitii):
    print(pozitii)
    for i in range(len(pozitii)):
        if i < 3:
            win.blit(number_list[pozitii[i]], (200 * i, 0))
        elif 3 <= i < 6:
            win.blit(number_list[pozitii[i]], (200 * i - 600, 200))
        else:
            win.blit(number_list[pozitii[i]], (200 * i - 1200, 400))
    pygame.display.update()


def rewrite_list(ind1, ind2, lnou):
    lnou[ind1], lnou[ind2] = lnou[ind2], lnou[ind1]
    return lnou


def redraw_game_window(pozitii, x, y, x_old, y_old, zero, left, right, up, down, calculator):
    i = int((y / 200) * 3 + (x / 200))
    pygame.time.delay(10)
    # print("i: ", i)

    if left or right or up or down:
        win.blit(number_list[0], (x, y))
        win.blit(number_list[pozitii[i]], (x_old, y_old))

    pygame.display.update()


def is_equal(L1, L2):
    for i in range(len(L1)):
        if L1[i] != L2[i]:
            return False
    return True


def human_player(pozitii, scop):
    draw_game_window(pozitii)
    calculator = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.time.delay(100)
        zero = pozitii.index(0)
        x, y = get_x_y(zero)
        x_old = x
        y_old = y
        print(x, y, y_old, x_old)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x >= vel:
            x = x - vel
            left, right, up, down = True, False, False, False
            zero -= 1
        elif keys[pygame.K_RIGHT] and x < screen_width_height - vel:
            x = x + vel
            left, right, up, down = False, True, False, False
            zero += 1
        elif keys[pygame.K_UP] and y >= vel:
            y = y - vel
            left, right, up, down = False, False, True, False
            zero -= 3
        elif keys[pygame.K_DOWN] and y < screen_width_height - vel:
            y = y + vel
            left, right, up, down = False, False, False, True
            zero += 3
        else:
            left, right, up, down = False, False, False, False
        print(x, y)
        redraw_game_window(pozitii, x, y, x_old, y_old, zero, left, right, up, down, calculator)
        i = int((y_old / 200) * 3 + (x_old / 200))
        pozitii = rewrite_list(zero, i, pozitii)
        if is_equal(pozitii, scop):
            run = False
    start_page(win,  pozitii, scop)


def computer_player(pozitii, scop=None):
    calculator = True
    draw_game_window(pozitii)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # determine if the AI chose left, right, up or down
        list_of_moves = db.main(pozitii, scop)
        first_move = list_of_moves[0].copy()
        list_of_moves.pop(0)
        draw_game_window(first_move)
        pygame.time.delay(10)
        pos_zero_ini = first_move.index(0)
        x, y = get_x_y(pos_zero_ini)
        for move in list_of_moves:
            pygame.time.delay(1000)
            x_old, y_old = x, y
            pos_zero_new = move.index(0)
            left, right, up, down = False, False, False, False
            if pos_zero_ini - pos_zero_new == 1:
                left, right, up, down = True, False, False, False
            elif pos_zero_ini - pos_zero_new == -1:
                left, right, up, down = False, True, False, False
            elif pos_zero_ini - pos_zero_new == 3:
                left, right, up, down = False, False, True, False
            elif pos_zero_ini - pos_zero_new == -3:
                left, right, up, down = False, False, False, True
            x, y = get_x_y(pos_zero_new)

            redraw_game_window(first_move, x, y, x_old, y_old, pos_zero_ini, left, right, up, down, calculator)

            pos_zero_ini = pos_zero_new
            first_move = move.copy()
        run = False
        pygame.time.delay(1000)
    start_page(win, pozitii, scop)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None, param1=None, param2=None, param3 = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))
        if click[0] == 1 and action != None and param1 != None and param2 != None and param3 == None:
            action(param1, param2)
        elif click[0] == 1 and action != None and param1 != None and param2 != None and param3 != None:
            action(param1, param2, param3)
    else:
        pygame.draw.rect(win, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    win.blit(textSurf, textRect)


def start_page(win, pozitii, scop):
    start_page_boolean = True
    while start_page_boolean:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_page_boolean = False

        win.fill(white)

        largeText = pygame.font.SysFont("comicsansms", 30)
        smallText = pygame.font.SysFont("comicsansms", 20)
        TextSurf0, TextRect0 = text_objects("START: ", smallText)
        win.blit(TextSurf0, (0, 0))
        for i in range(3):
            string = ""
            for j in range(3):
                string +=str(pozitii[i*3+j]) + "   "
            TextSurf1, TextRect1 = text_objects(string, largeText)
            win.blit(TextSurf1, (0, 20 + i * 40))

        TextSurf0, TextRect0 = text_objects("SCOP: ", smallText)
        win.blit(TextSurf0, (0, 210))
        for i in range(3):
            string = ""
            for j in range(3):
                string += str(scop[i * 3 + j]) + "   "
            TextSurf1, TextRect1 = text_objects(string, largeText)
            win.blit(TextSurf1, (0, 240 + i * 40))

        button("Computer player", 250, 300, 300, 50, green, bright_green, computer_player, param1=pozitii, param2=scop)
        button("Human player", 250, 400, 300, 50, red, bright_red, human_player, param1=pozitii, param2=scop)
        pygame.display.update()


pozitii = [2, 4, 3, 8, 7, 5, 1, 0, 6]
scop = [1, 2, 3, 4, 5, 6, 7, 8, 0]
start_page(win, pozitii, scop)
pygame.quit()