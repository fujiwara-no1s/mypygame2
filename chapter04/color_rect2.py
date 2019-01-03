import pygame
from pygame.locals import *
from sys import exit

from random import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255,255,255))

    screen.lock()

    color = (255,0,0)
    pos = (10,10)
    size = (10,10)
    location = (50, 50, 100, 100)
    #pygame.draw.rect(screen, color, (pos,size))
    pygame.draw.rect(screen, color, location)
    screen.unlock()

    pygame.display.update()
