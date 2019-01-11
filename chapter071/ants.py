import pygame
from pygame.locals import *
from chapter071.ant_grid import AntGrid
from chapter071.ant import Ant

GRID_SIZE = (160, 120)
GRID_SQUARE_SIZE = (4, 4)
ant_image_filename = "ant.png"
ITERATIONS = 1


def run():
    pygame.init()
    w = GRID_SIZE[0] * GRID_SQUARE_SIZE[0]
    h = GRID_SIZE[1] * GRID_SQUARE_SIZE[1]
    # ウィンドウの作成
    screen = pygame.display.set_mode((w, h), 0, 32)
    # アリの画像作成
    ant_image = pygame.image.load(ant_image_filename).convert_alpha()    
    
    default_font = pygame.font.get_default_font()
    font = pygame.font.SysFont(default_font, 22)    
    
    ants = []
    # グリッド作成
    grid = AntGrid(*GRID_SIZE)
    running = False
    
    total_iterations = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                x /= GRID_SQUARE_SIZE[0]
                y /= GRID_SQUARE_SIZE[1]
                # アリの作成
                ant = Ant(grid, int(x), int(y), ant_image)
                # アリ管理リストに追加
                ants.append(ant)
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # スペースで開始
                    running = not running
                    
                if event.key == K_c:
                    # cでクリア
                    grid.clear()
                    total_iterations = 0
                    del ants[:]
        # GRIDを表示
        # アリがいる場所をオレンジに塗る
        grid.render(screen, ((255, 255, 255), (255, 128, 0)), GRID_SQUARE_SIZE)
    
        if running:
            for iteration_no in range(ITERATIONS):
                for ant in ants:
                    ant.move()
            total_iterations += ITERATIONS

        txt = "%i iterations"%total_iterations
        txt_surface = font.render(txt, True, (0, 0, 0))
        screen.blit(txt_surface, (0, 0))

        for ant in ants:
            ant.render(screen, GRID_SQUARE_SIZE)

        pygame.display.update()

    
if __name__ == "__main__":
    run()
