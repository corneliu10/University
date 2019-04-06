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
pozitii = [2, 4, 3, 8, 7, 5, 1, 0, 6]
zero = pozitii.index(0)
#new_char = zero
# determinati coordonatele x si y la care va fi plasata placuta goala, stiind ca zero este indexul unde se afla aceasta pozitie in "pozitii"
# si stiind ca inaltilea si latimea unei placute este de width si height si ca dimensiunea ferestrei este screen_width_height
if zero < 3:
    x = zero * 200
    y = 0
elif 3 <= zero < 6:
    ...
else:
    ...

number_list = [pygame.image.load('9.png'), pygame.image.load('1.png'), pygame.image.load('2.png'),
               pygame.image.load('3.png'), pygame.image.load('4.png'), pygame.image.load('5.png'),
               pygame.image.load('6.png'), pygame.image.load('7.png'), pygame.image.load('8.png')]


def draw_game_window():
    for i in range(len(pozitii)):
        if i < 3:
			# comanda win.blit afiseaza pe ecran imaginea data ca prim argument la pozitiile date a argument secund
            win.blit(number_list[pozitii[i]], (200 * i, 0))
        elif 3 <= i < 6:
            ...
        else:
            ...


draw_game_window()


def rewrite_list(ind1, ind2, lnou):
    lnou[ind1], lnou[ind2] = lnou[ind2], lnou[ind1]
    return lnou


def redraw_game_window(pozitii, x, y, zero, left, right, up, down):
    i = int((y / 200) * 3 + (x / 200))
    print("i: ", i)

    if left:
        #print('left x,y, zero', x, y, zero)
        win.blit(number_list[0], (x, y))
        win.blit(number_list[pozitii[i]], (x_old, y_old))
    elif right:
        ...
    elif up:
        ...
    elif down:
        ...
		
    pozitii = rewrite_list(zero, i, pozitii)
    pygame.display.update()


run = True

while run:
    pygame.time.delay(100)
    zero = pozitii.index(0)
    x_old = x
    y_old = y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= vel:
        x = x - vel
        left, right, up, down = True, False, False, False
        zero -= 1

    elif keys[pygame.K_RIGHT] and x < screen_width_height - vel:
        ...

    elif keys[pygame.K_UP] and y >= vel:
        ...

    elif keys[pygame.K_DOWN] and y < screen_width_height - vel:
        ...

    else:
        left, right, up, down = False, False, False, False

    print(pozitii)
    redraw_game_window(pozitii, x, y, zero, left, right, up, down)

pygame.quit()
