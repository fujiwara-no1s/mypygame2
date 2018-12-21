#!/usr/bin/env python


import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
SCREEN_SIZE = (640, 480)
pygame.init()

pygame.display.set_caption("Hello, World!")

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -10
            if event.key == K_RIGHT:
                move_x = 10
            if event.key == K_UP:
                move_y = -10
            if event.key == K_DOWN:
                move_y = 10
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            if event.key == K_RIGHT:
                move_x = 0
            if event.key == K_UP:
                move_y = 0
            if event.key == K_DOWN:
                move_y = 0
        x += move_x
        y += move_y

    screen.fill((0,0,0))
    screen.blit(background, (x, y))

    pygame.display.update()
