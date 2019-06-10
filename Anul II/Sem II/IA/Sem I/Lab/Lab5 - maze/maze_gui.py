import maze_ai as db
import pygame
import time
import random
import configuratii as cf

pygame.init()
screen_width_height = 500
win = pygame.display.set_mode((screen_width_height, screen_width_height))
pygame.display.set_caption("Maze")


black = (0, 0, 0)
white = (255, 255, 255)

dark_slate_blue = (24, 152, 255)
cornflower_blue = (100, 149, 237)


def get_x_y(ind):
    j_elem = ind // 20
    i_elem = ind % 20
    return i_elem, j_elem


number_list = [pygame.image.load('cube_move.png'), pygame.image.load('cube_goal.png'),
               pygame.image.load('cube_free_pass.png'), pygame.image.load('cube_obstacle.png'),
               pygame.image.load('cube_path.png')]


def draw_game_window(pozitii, scop):
    for ind in range(len(pozitii)):
        j_elem = ind // 20
        i_elem = ind % 20
        if pozitii[ind] == 0:
            win.blit(number_list[2], (i_elem * 25, j_elem * 25))
        elif pozitii[ind] == 1:
            win.blit(number_list[0], (i_elem * 25, j_elem * 25))
        elif pozitii[ind] == 2:
            win.blit(number_list[3], (i_elem * 25, j_elem * 25))
    ind = scop.index(1)
    j_elem = ind // 20
    i_elem = ind % 20
    win.blit(number_list[1], (i_elem * 25, j_elem * 25))

    # print(str(i_elem*20) +" "+ str(j_elem*20))
    pygame.display.update()


def rewrite_list(ind1, ind2, lnou):
    lnou[ind1], lnou[ind2] = lnou[ind2], lnou[ind1]
    return lnou


def redraw_game_window(x, y, x_old, y_old):
    pygame.time.delay(10)
    win.blit(number_list[0], (x*25, y*25))
    win.blit(number_list[4], (x_old*25, y_old*25))
    pygame.display.update()


def computer_player(list_of_moves=None):
    run = True
    if list_of_moves is None:
        list_of_moves = db.asd()

    first_move = list_of_moves[0].copy()
    list_of_moves.pop(0)
    last_move = list_of_moves[-1]
    draw_game_window(first_move, last_move)
    pygame.time.delay(10)
    pos_unu_ini = first_move.index(1)
    x, y = get_x_y(pos_unu_ini)
    pygame.event.get()
    time.sleep(0.4)
    while run:
        # determine if the AI chose left, right, up or down
        for move in list_of_moves:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
            x_old, y_old = x, y
            pos_unu_new = move.index(1)
            x, y = get_x_y(pos_unu_new)
            print(x,y, y_old, x_old)
            redraw_game_window(x, y, x_old, y_old)

            pos_unu_ini = pos_unu_new
            pygame.time.delay(100)

        run = False
    pygame.time.delay(1500)
    start_page(win)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(win, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w // 2)), (y + (h // 2)))
    win.blit(textSurf, textRect)


def get_pozitii(nr_obstacole):
    pozitii = random.sample(range(0, 399), nr_obstacole)
    lista_pozitii_start = cf.empty_window_start[:]
    lista_pozitii_scop = cf.empty_window_scop[:]
    for i in pozitii:
        if i != 19 and i != 380:
            lista_pozitii_start[i] = 2
            lista_pozitii_scop[i] = 2
    return lista_pozitii_start, lista_pozitii_scop


def new_maze():
    nr_obstacole = 100
    pozitii, scop = get_pozitii(nr_obstacole)
    list_of_moves = db.main(pozitii, scop)
    while len(list_of_moves) == 0:
        pozitii, scop = get_pozitii(nr_obstacole)
        list_of_moves = db.main(pozitii, scop)
    computer_player(list_of_moves)


def start_page(win):
    start_page_boolean = True
    while start_page_boolean:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_page_boolean = False
                pygame.quit()

        win.fill(white)

        largeText = pygame.font.SysFont("comicsansms", 30)
        smallText = pygame.font.SysFont("comicsansms", 20)

        button("New Maze", 50, 200, 300, 50, dark_slate_blue, cornflower_blue, new_maze)
        button("Computer Player", 50, 300, 300, 50, dark_slate_blue, cornflower_blue, computer_player)
        pygame.display.update()


start_page(win)
# pygame.quit()