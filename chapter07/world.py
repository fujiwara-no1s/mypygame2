import pygame
from gameobjects.vector2 import Vector2
from chapter07.setting import *


class World:
    def __init__(self):
        self.entities = {}
        self.entity_id = 0
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.background.fill((255, 255, 255))
        pygame.draw.circle(self.background, (200, 255, 200), NEST_POSITION, int(NEST_SIZE))

    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def process(self, time_passed):
        time_passed_seconds = time_passed / 1000.0
        # 個別のエンティティに動作させる
        for entity in list(self.entities.values()):
            entity.process(time_passed_seconds)

    def render(self, surface):
        # ウィンドウ全体を表すSurfaceに背景を描く
        surface.blit(self.background, (0, 0))
        # 個別のエンティティを描く
        for entity in list(self.entities.values()):
            entity.render(surface)

    def get_close_entity(self, name, location, range=100.):
        location = Vector2(*location)

        for entity in self.entities.values():
            if entity.name == name:
                distance = location.get_distance_to(entity.location)
                if distance < range:
                    return entity
        return None
