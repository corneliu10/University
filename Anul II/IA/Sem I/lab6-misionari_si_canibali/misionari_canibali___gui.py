import misionari_canibali___a_star as mc_ia
import pygame

pygame.init()
screen_width = 950
screen_height = 440
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Misionari si canibali")

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)
orange = (255, 192, 0)
blue = (100, 100, 200)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
yellow = (255, 255, 0)
bright_blue = (100, 100, 255)

largeText = pygame.font.SysFont("comicsansms", 30)
smallText = pygame.font.SysFont("comicsansms", 20)

y_line1 = 0; h_line = 50
y_line2 = y_line1 + h_line + 20
y_line3 = y_line2 + h_line + 20
y_line4 = y_line3 + h_line + 20
y_line5 = y_line4 + h_line + 40
y_line6 = y_line5 + h_line + 20

x_col1=20; w_col1=120
x_col2 = x_col1 + w_col1 + 50; w_col2 = 250
x_col3 = x_col2 + w_col2 + 70; w_col3 = 250
x_col4 = x_col3 + w_col3 + 50; w_col4 = 110

#global
nr_Mis_Barca = 0
nr_Can_Barca = 0
succesor = ['', 0, 0, 0, 0]

def draw_game_window(nod_info):
    # Mal Vest
    TextSurf0, TextRect0 = text_objects("Mal Vest", largeText, black)
    win.blit(TextSurf0, (x_col1, y_line1))
    button("0 Mis ->", x_col1, y_line2, w_col1, h_line, green, bright_green, None, None, None, None)
    button("0 Can ->", x_col1, y_line3, w_col1, h_line, red, bright_red, None, None, None, None)

    # Barca Vest
    # TextSurf0, TextRect0 = text_objects("Barca (1-{} indivizi)".format(mc_ia.Nod.NR_LOCURI_BARCA), largeText, black)
    # win.blit(TextSurf0, (x_col2, y_line1))
    # button("<- 0 Mis", x_col2, y_line2, w_col2, h_line, green, bright_green, None, None, None, None)
    # button("<- 0 Can", x_col2, y_line3, w_col2, h_line, red, bright_red, None, None, None, None)
    # button("muta barca ->", x_col2, y_line4, w_col2, h_line, orange, yellow, None, None, None, None)

    # Barca Est
    TextSurf0, TextRect0 = text_objects("Barca (1-{} indivizi)".format(mc_ia.Nod.NR_LOCURI_BARCA), largeText, black)
    win.blit(TextSurf0, (x_col3, y_line1))
    button("0 Mis ->", x_col3, y_line2, w_col3, h_line, green, bright_green, None, None, None, None)
    button("0 Can ->", x_col3, y_line3, w_col3, h_line, red, bright_red, None, None, None, None)
    button("<- muta barca", x_col3, y_line4, w_col3, h_line, orange, yellow, None, None, None, None)

    # Mal Est
    TextSurf0, TextRect0 = text_objects("Mal Est", largeText, black)
    win.blit(TextSurf0, (x_col4, y_line1))
    button("<- {} Mis".format(mc_ia.Nod.NR_MISIONARI), x_col4, y_line2, w_col4, h_line, green, bright_green, None, None, None, None)
    button("<- {} Can".format(mc_ia.Nod.NR_CANIBALI), x_col4, y_line3, w_col4, h_line, red, bright_red, None, None, None, None)

    # buton Computer Player
    button("Computer Player", x_col1, y_line6, 2 * w_col1, h_line, blue, bright_blue, computer_player, nod_start, nod_scop, mc_ia.Nod.NR_LOCURI_BARCA)

    pygame.display.update()


def redraw_game_window_COMPUTER(nod): ###def redraw_game_window_COMPUTER(nod, nr_Mis_Barca, nr_Can_Barca):
    global nr_Mis_Barca
    global nr_Can_Barca
    # Mal Vest
    button("{} Mis ->".format(nod[3]), x_col1, y_line2, w_col1, h_line, green, bright_green, None, None, None, None)
    button("{} Can ->".format(nod[4]), x_col1, y_line3, w_col1, h_line, red, bright_red, None, None, None, None)

    if nod[0] == 'vest':
        # Barca Vest
        TextSurf0, TextRect0 = text_objects("Barca (1-{} indivizi)".format(mc_ia.Nod.NR_LOCURI_BARCA), largeText, black)
        win.blit(TextSurf0, (x_col2, y_line1))
        button("<- {} Mis".format(nr_Mis_Barca), x_col2, y_line2, w_col2, h_line, green, bright_green, None, None, None, None)
        button("<- {} Can".format(nr_Can_Barca), x_col2, y_line3, w_col2, h_line, red, bright_red, None, None, None, None)
        button("muta barca ->", x_col2, y_line4, w_col2, h_line, orange, yellow, None, None, None, None)
        # la Est (coloana 3) acopar cu alb
        pygame.draw.rect(win, white, (x_col3, y_line1, w_col3+10, y_line4+h_line))

    elif nod[0] == 'est':
        # la Vest (coloana 2) acopar cu alb
        pygame.draw.rect(win, white, (x_col2, y_line1, w_col2+10, y_line4 + h_line))
        # Barca Est
        TextSurf0, TextRect0 = text_objects("Barca (1-{} indivizi)".format(mc_ia.Nod.NR_LOCURI_BARCA), largeText, black)
        win.blit(TextSurf0, (x_col3, y_line1))
        button("{} Mis ->".format(nr_Mis_Barca), x_col3, y_line2, w_col3, h_line, green, bright_green, None, None, None, None)
        button("{} Can ->".format(nr_Can_Barca), x_col3, y_line3, w_col3, h_line, red, bright_red, None, None, None, None)
        button("<- muta barca", x_col3, y_line4, w_col3, h_line, orange, yellow, None, None, None, None)

    # Mal Est
    TextSurf0, TextRect0 = text_objects("Mal Est", largeText, black)
    win.blit(TextSurf0, (x_col4, y_line1))
    button("<- {} Mis".format(nod[1]), x_col4, y_line2, w_col4, h_line, green, bright_green, None, None, None, None)
    button("<- {} Can".format(nod[2]), x_col4, y_line3, w_col4, h_line, red, bright_red, None, None, None, None)

    pygame.display.update()


def computer_player(nod_initial, nod_scop, nr_loc_barca):
    run = True
    configuratii = mc_ia.main()
    global nr_Mis_Barca
    global nr_Can_Barca

    nr_Mis_Barca = 0; nr_Can_Barca = 0
    redraw_game_window_COMPUTER(nod_initial) ###(nod_initial, 0, 0)
    pygame.time.delay(1000)

    while run:
        for i in range(0, len(configuratii)-1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            # nod = [mal in ['est', 'vest'], nr_Mis_Est, nr_Can_Est, nr_Mis_Vest, nr_Can_Vest]
            nod_vechi = list(configuratii[i])
            nod_nou = list(configuratii[i+1])
            nr_Mis_Barca = abs(nod_vechi[1] - nod_nou[1])
            nr_Can_Barca = abs(nod_vechi[2] - nod_nou[2])

            nod_inter = nod_vechi.copy()
            if nod_vechi[0] == 'est':
                nod_inter[1] -= nr_Mis_Barca; nod_inter[2] -= nr_Can_Barca
            elif nod_vechi[0] == 'vest':
                nod_inter[3] -= nr_Mis_Barca; nod_inter[4] -= nr_Can_Barca

            redraw_game_window_COMPUTER(nod_inter) ### (nod_inter, nr_Mis_Barca, nr_Can_Barca)
            pygame.time.delay(1500)

            nr_Mis_Barca = 0; nr_Can_Barca = 0
            redraw_game_window_COMPUTER(nod_nou) ###(nod_nou, 0, 0)
            pygame.time.delay(1500)

        run = False
    pygame.time.delay(2000)
    start_page(win, nod_start, nod_scop)



def text_objects(text, font, color=black):
    # color = white
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None, param1=None, param2=None, param3 = None):
    # add paramentru pt textcolor
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))
        if click[0] == 1 and action != None and param1 != None and param2 != None and param3 != None:
            action(param1, param2, param3) # muta_barca(nod_info, nr_mis, nr_can)
    else:
        pygame.draw.rect(win, ic, (x, y, w, h))
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    win.blit(textSurf, textRect)


def start_page(win, nod_info, nod_scop_info):
    start_page_boolean = True
    while start_page_boolean:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_page_boolean = False
                pygame.quit()
        win.fill(white)

        draw_game_window(nod_start)
        pygame.display.update()


# main
mc_ia.Nod.NR_MISIONARI = mc_ia.Nod.NR_CANIBALI = int(str(input("Nr misionari = Nr canibali = ")))
mc_ia.Nod.NR_LOCURI_BARCA = int(str(input("Nr locuri barca = ")))

# mc_ia.Nod.NR_MISIONARI = mc_ia.Nod.NR_CANIBALI = 3
# mc_ia.Nod.NR_LOCURI_BARCA = 2

nod_start = ['est', mc_ia.Nod.NR_MISIONARI, mc_ia.Nod.NR_CANIBALI, 0, 0]
nod_scop = ['vest', 0, 0, mc_ia.Nod.NR_MISIONARI, mc_ia.Nod.NR_CANIBALI]

start_page(win, nod_start, nod_scop)
