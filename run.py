import sys
import pygame

# base size unit
b = 10
COLOR = {'red': (255, 0, 0),
         'green': (0, 255, 0),
         'blue': (0, 0, 255),
         'cyan': (0, 255, 255),
         'magenta': (255, 0, 255),
         'yellow': (255, 255, 0),
         'black': (0, 0, 0),
         'grey': (128, 128, 128),
         'white': (255, 255, 255)}

# screen size
screen_w = 60*b
screen_h = 40*b

screen = pygame.display.set_mode((screen_w, screen_h))


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


POS_X = {'l': ((screen_w - 10*b) / 2) - 20 * b,
         'm': (screen_w-10*b)/2,
         'r': ((screen_w-10*b)/2) + 20*b
         }

POS_Y = {'u3': ((screen_h - 5*b) / 2) - 10 * b,
         'u2': ((screen_h - 5*b) / 2) - 5 * b,
         'u1': (screen_h - 5*b) / 2,
         'm': ((screen_h - 5 * b) / 2) + 5 * b,
         'd': ((screen_h - 5*b) / 2) + 10 * b
         }


class Figure:
    width = 10 * b
    height = 5 * b

    def __init__(self, init_x, init_y):
        fig = pygame.Surface((self.width, self.height))
        fig.fill(COLOR['blue'])
        screen.blit(fig, (init_x, init_y))


player = Figure(POS_X['m'], POS_Y['u3'])

running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        #elif pygame.K_RIGHT:
            #player = POS_X['m']

    # drawing screen content
   # pygame.draw.rect(screen, COLOR["yellow"], player_rect)
    pygame.display.flip()
