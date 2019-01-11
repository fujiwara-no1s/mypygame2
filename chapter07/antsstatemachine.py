import pygame
from pygame.locals import *
from random import randint, choice
from gameobjects.vector2 import Vector2

from chapter07.setting import *
from chapter07.world import World
from chapter07.leaf import Leaf
from chapter07.spider import Spider
from chapter07.ant import Ant


def run():
    # ゲームの初期化
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    world = World()
    w, h = SCREEN_SIZE
    clock = pygame.time.Clock()
    #画像の初期化
    ant_image = pygame.image.load("ant.png").convert_alpha()
    leaf_image = pygame.image.load("leaf.png").convert_alpha()
    spider_image = pygame.image.load("spider.png").convert_alpha()

    # アリの作成
    for ant_no in range(ANT_COUNT):
        # アリの作成
        ant = Ant(world, ant_image)
        # アリをランダムな位置に配置したいので、XとYをウィンドウ内のランダムな位置にする
        ant.location = Vector2(randint(0, w), randint(0, h))
        ant.brain.set_state("exploring")
        world.add_entity(ant)
    # 1/10の確率で葉の作成
    if randint(1, 10) == 1:
        leaf = Leaf(world, leaf_image)
        leaf.location = Vector2(randint(0, w), randint(0, h))
        world.add_entity(leaf)
    # 1/100の確率でクモの作成
    if randint(1, 100) == 1:
        spider = Spider(world, spider_image)
        spider.location = Vector2(-50, randint(0, h))
        spider.destination = Vector2(w + 50, randint(0, h))
        world.add_entity(spider)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        time_passed = clock.tick(30)

        if randint(1, 10) == 1:
            leaf = Leaf(world, leaf_image)
            leaf.location = Vector2(randint(0, w), randint(0, h))
            world.add_entity(leaf)

        if randint(1, 100) == 1:
            spider = Spider(world, spider_image)
            spider.location = Vector2(-50, randint(0, h))
            spider.destination = Vector2(w+50, randint(0, h))            
            world.add_entity(spider)

        world.process(time_passed)
        world.render(screen)
        
        pygame.display.update()


if __name__ == "__main__":    
    run()
