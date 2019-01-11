from gameobjects.vector2 import Vector2
from chapter07.state_machine import StateMachine


class GameEntity(object):
    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.speed = 0.
        self.brain = StateMachine()
        self.id = 0

    def render(self, surface):
        # 中心点を表す
        x, y = self.location
        w, h = self.image.get_size()
        # XYは中心点なので画像のサイズを反映する
        surface.blit(self.image, (x - w / 2, y - h / 2))

    def process(self, time_passed):
        self.brain.think()

        # speedが0でなく、現在地と目標値が異なれば
        if self.speed > 0. and self.location != self.destination:
            # 移動するベクトルの計算
            vec_to_destination = self.destination - self.location
            # 移動する距離を取得
            distance_to_destination = vec_to_destination.get_length()
            # 正規化した移動量
            heading = vec_to_destination.get_normalized()
            # 移動距離、または時間の小さい方を取得
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            # 新しい座標を設定
            self.location += travel_distance * heading
