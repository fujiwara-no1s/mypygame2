#!/usr/bin/env python


import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
SCREEN_SIZE = (640, 480)
pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

message = "This is a demostration of the scrolly message script"
message = "I have a pen"

try:
    font = pygame.sysfont.SysFont("arial", 80)
except MemoryError:
    font = pygame.font.Font(pygame.font.get_default_font(), 80)
text_surface = font.render(message, True, (0,0,255))

x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height()) / 2
background = pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))

    x -= 2
    if x < -text_surface.get_width():
        x = 0
    screen.blit(text_surface, (x, y))
    screen.blit(text_surface, (x + text_surface.get_width(), y))

    pygame.display.update()
