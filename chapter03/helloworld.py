#!/usr/bin/env python


import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

pygame.init()

pygame.display.set_caption("Hello, World!")

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    #x -= mouse_cursor.get_width()
    #y -= mouse_cursor.get_height()
    screen.blit(mouse_cursor, (x, y))
    pygame.display.update()
