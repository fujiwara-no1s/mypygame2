import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *

background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'


pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

# 位置
sprite_pos = Vector2(200, 150)
# 移動速度
sprite_speed = 300.
# 回転角度
sprite_rotation = 0.
# 回転速度
sprite_rotation_speed = 360.  # Degrees per second

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0.
    movement_direction = 0.

    if pressed_keys[K_LEFT]:
        rotation_direction = +1.
    if pressed_keys[K_RIGHT]:
        rotation_direction = -1.
    if pressed_keys[K_UP]:
        movement_direction = -1.
    if pressed_keys[K_DOWN]:
        movement_direction = +1.

    screen.blit(background, (0, 0))

    # 回転させる
    rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotated_sprite.get_size()
    # 現在の位置を取得
    sprite_draw_pos = Vector2(sprite_pos.x - w / 2, sprite_pos.y - h / 2)
    # 現在の位置で回転した画像の表示
    screen.blit(rotated_sprite, sprite_draw_pos)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # キー操作に基づいて、回転角度を解散する
    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    # 回転角度に基づいて、上下の傾きを計算する
    heading_x = sin(sprite_rotation * pi / 180.)
    # 回転角度に基づいて、左右の傾きを計算する
    heading_y = cos(sprite_rotation * pi / 180.)
    heading = Vector2(heading_x, heading_y)
    # 上下左右の移動量を計算する（傾きに基づく）
    heading *= movement_direction

    # 傾きに基づく、移動先座標を計算する
    sprite_pos += heading * sprite_speed * time_passed_seconds

    pygame.display.update()
