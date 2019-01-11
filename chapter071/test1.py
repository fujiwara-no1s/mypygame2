import pygame
from pygame.locals import *

GRID_SIZE = (160, 120)
GRID_SQUARE_SIZE = (4, 4)
ant_image_filename = "ant.png"
ITERATIONS = 1
WINDOW_SIZE = (640, 480)
WHITE_COLOR = (255,255,255)
RED_COLOR = (255,0,0)

def run():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.fill(WHITE_COLOR)
        screen.fill(RED_COLOR,(10,10,100,100))
        pygame.display.update()


if __name__ == "__main__":
    run()
