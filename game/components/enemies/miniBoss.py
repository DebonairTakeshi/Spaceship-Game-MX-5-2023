import pygame
from game.components.enemies.enemy_2 import Enemy_2
from game.utils.constants import BOSS


class Enemy_2(Enemy_2):
    WIDTH = 200
    HEIGHT = 200


    def __init__(self):
        self.image = BOSS
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)