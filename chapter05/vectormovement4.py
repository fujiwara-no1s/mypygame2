import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

# 四角形が、画面中央に徐々に移動します

WINDOW_SIZE = (640, 480)
pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

background = pygame.image.load(background_image_filename).convert()
#sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(0.0, 0.0)
heading = Vector2()
size = (100,100)
speed = 100

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen,(255,0,0),(position,size))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    destination = Vector2(*WINDOW_SIZE) / 2 - Vector2(*size) / 2
    vector_to_mouse = Vector2.from_points(position, destination)
    vector_to_mouse.normalize()

    position += vector_to_mouse * time_passed_seconds * speed
    pygame.display.update()
