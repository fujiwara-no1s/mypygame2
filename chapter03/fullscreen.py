#!/usr/bin/env python


import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
SCREEN_SIZE = (640, 480)
pygame.init()

#pygame.display.set_caption("Hello, World!")

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

background = pygame.image.load(background_image_filename).convert()

Fullscreen = False
x = y = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

    screen.fill((0,0,0))
    screen.blit(background, (x, y))

    pygame.display.update()
