import random

class Ant(object):
    directions = ((0, -1), (+1, 0), (0, +1), (-1, 0))

    def __init__(self, grid, x, y, image, direction=1):
        #座標クラス
        self.grid = grid
        # 現在のX座標
        self.x = x
        # 現在のY座標
        self.y = y
        # 画像
        self.image = image
        # 移動方向
        self.direction = direction

    def move(self):
        # 現在位置をGRIDないでTrueにする
        self.grid.swap(self.x, self.y)

        rand_x = random.randint(0,3)
        rand_y = random.randint(0,3)
        self.x = (self.x + Ant.directions[rand_x][0]) % self.grid.width
        self.y = (self.y + Ant.directions[rand_y][1]) % self.grid.height
        #self.x = (self.x + Ant.directions[self.direction][0]) % self.grid.width
        #self.y = (self.y + Ant.directions[self.direction][1]) % self.grid.height

        if self.grid.get(self.x, self.y):
            self.direction = (self.direction - 1) % 4
        else:
            self.direction = (self.direction + 1) % 4

    def render(self, surface, grid_size):
        grid_w, grid_h = grid_size
        ant_w, ant_h = self.image.get_size()
        render_x = self.x * grid_w - ant_w / 2
        render_y = self.y * grid_h - ant_h / 2
        surface.blit(self.image, (render_x, render_y))
