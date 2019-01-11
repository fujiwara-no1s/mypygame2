import pygame
from pygame.locals import *
from sys import exit

pygame.init()
surface = pygame.display.set_mode((640,480), 0, 32)
ant_image = pygame.image.load("ant.png").convert_alpha()
# 画像のサイズ
print(ant_image.get_rect().size)
# 画像の幅
print(ant_image.get_width())
# 画像の高さ
print(ant_image.get_height())

# 画像の作成
ant_image2 = pygame.image.load("ant.png").convert_alpha()
# 画像のサイズを変更
ant_image2 = pygame.transform.scale(ant_image2, (64, 36))
print(ant_image2.get_rect().size)
# 画像の幅
print(ant_image2.get_width())
# 画像の高さ
print(ant_image2.get_height())

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    surface.fill((255,255,255))
    surface.blit(ant_image2,(0-32,0-18))
    pygame.display.update()

